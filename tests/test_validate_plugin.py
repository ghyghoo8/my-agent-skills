"""Exercise the repository Plugin validator through its CLI."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPOSITORY = Path(__file__).resolve().parents[1]
VALIDATOR = REPOSITORY / "scripts" / "validate_plugin.py"


class PluginValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "plugin"
        self.manifest = self.root / ".codex-plugin" / "plugin.json"
        self.manifest.parent.mkdir(parents=True)
        self.skill = self.root / "skills" / "example" / "SKILL.md"
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text(
            "---\nname: example\ndescription: Example workflow.\n---\n\nUse it.\n",
            encoding="utf-8",
        )
        self.metadata = {
            "name": "example-plugin",
            "version": "1.0.0",
            "description": "Example skills-only plugin.",
            "author": {"name": "Example"},
            "skills": "./skills/",
            "interface": {
                "displayName": "Example",
                "shortDescription": "Example workflows.",
                "longDescription": "A reusable engineering workflow.",
                "developerName": "Example",
            },
        }
        self.write_manifest()

    def write_manifest(self):
        self.manifest.write_text(json.dumps(self.metadata), encoding="utf-8")

    def run_validator(self, root=None):
        return subprocess.run(
            [sys.executable, str(VALIDATOR), str(root or self.root)],
            capture_output=True,
            text=True,
        )

    def assert_rejected(self, field):
        result = self.run_validator()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(field, result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_current_repository_plugin_is_valid(self):
        result = self.run_validator(REPOSITORY / "plugins" / "my-agent-skills")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_valid_plugin_needs_no_submission_assets(self):
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_semver_release_prerelease_and_build_are_supported(self):
        for version in ("0.0.0", "1.2.3-rc.1", "1.2.3+build.007", "1.2.3-rc.1+build.9"):
            with self.subTest(version=version):
                self.metadata["version"] = version
                self.write_manifest()
                result = self.run_validator()
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_versions_are_rejected(self):
        for version in ("1.2", "v1.2.3", "01.2.3", "1.2.3-01", "1.2.3-", 123):
            with self.subTest(version=version):
                self.metadata["version"] = version
                self.write_manifest()
                self.assert_rejected("version")

    def test_required_identity_and_listing_fields_are_checked(self):
        for field in ("name", "version", "description", "author", "interface", "skills"):
            with self.subTest(field=field):
                value = self.metadata.pop(field)
                self.write_manifest()
                self.assert_rejected(field)
                self.metadata[field] = value

    def test_wrong_metadata_types_are_rejected(self):
        for field, value in (("name", 7), ("author", []), ("interface", []), ("keywords", "skills")):
            with self.subTest(field=field):
                previous = self.metadata.get(field)
                self.metadata[field] = value
                self.write_manifest()
                self.assert_rejected(field)
                if previous is None:
                    del self.metadata[field]
                else:
                    self.metadata[field] = previous

    def test_listing_fields_and_limits_use_package_rules(self):
        self.metadata["interface"]["shortDescription"] = "x" * 80
        self.write_manifest()
        self.assertEqual(self.run_validator().returncode, 0)
        for field, value in (("displayName", " "), ("shortDescription", "a\nb"),
                             ("shortDescription", "x" * 241), ("capabilities", "Read"),
                             ("defaultPrompt", [7])):
            with self.subTest(field=field):
                previous = self.metadata["interface"].get(field)
                self.metadata["interface"][field] = value
                self.write_manifest()
                self.assert_rejected(field)
                if previous is None:
                    del self.metadata["interface"][field]
                else:
                    self.metadata["interface"][field] = previous

    def test_unreadable_or_malformed_manifest_is_reported(self):
        for content in (b"{", b"[]", b"\xff"):
            with self.subTest(content=content):
                self.manifest.write_bytes(content)
                self.assert_rejected("plugin.json")
        self.manifest.unlink()
        self.assert_rejected("plugin.json")

    def test_duplicate_json_keys_are_rejected(self):
        self.manifest.write_text('{"name":"first","name":"second"}', encoding="utf-8")
        self.assert_rejected("duplicate")

    def test_non_json_numeric_constants_are_rejected(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                content = json.dumps(self.metadata)[:-1] + ', "unknown": ' + constant + '}'
                self.manifest.write_text(content, encoding="utf-8")
                self.assert_rejected("plugin.json")

    def test_extra_manifest_authority_is_rejected(self):
        (self.root / "plugin.json").write_text("{}", encoding="utf-8")
        self.assert_rejected("plugin.json")

    def test_skills_path_must_be_the_root_skills_directory(self):
        for value in ("skills", "../skills", "./../skills", str(self.skill.parent), "./elsewhere", []):
            with self.subTest(value=value):
                self.metadata["skills"] = value
                self.write_manifest()
                self.assert_rejected("skills")

    def test_at_least_one_direct_skill_is_required(self):
        self.skill.unlink()
        self.skill.parent.rmdir()
        self.assert_rejected("skills")

    def test_nested_or_missing_skill_manifest_is_rejected(self):
        self.skill.unlink()
        nested = self.skill.parent / "nested" / "SKILL.md"
        nested.parent.mkdir()
        nested.write_text("Example", encoding="utf-8")
        self.assert_rejected("SKILL.md")

    def test_skill_manifest_must_be_utf8(self):
        self.skill.write_bytes(b"\xff")
        self.assert_rejected("SKILL.md")

    def test_declared_assets_exist_and_stay_inside_plugin(self):
        assets = self.root / "assets"
        assets.mkdir()
        (assets / "logo.svg").write_text("<svg/>", encoding="utf-8")
        self.metadata["interface"]["logo"] = "./assets/logo.svg"
        self.write_manifest()
        self.assertEqual(self.run_validator().returncode, 0)
        for value in ("assets/logo.svg", "./assets/missing.svg", "./../outside.svg", "./assets"):
            with self.subTest(value=value):
                self.metadata["interface"]["logo"] = value
                self.write_manifest()
                self.assert_rejected("logo")

    def test_asset_symlink_escape_is_rejected(self):
        outside = self.root.parent / "outside.svg"
        outside.write_text("<svg/>", encoding="utf-8")
        assets = self.root / "assets"
        assets.mkdir()
        (assets / "logo.svg").symlink_to(outside)
        self.metadata["interface"]["logo"] = "./assets/logo.svg"
        self.write_manifest()
        self.assert_rejected("logo.svg")

    def test_symlinks_in_the_bundle_are_rejected(self):
        for target in (self.skill, self.root.parent / "missing", self.root / "loop"):
            with self.subTest(target=target):
                link = self.root / "loop"
                link.symlink_to(target)
                try:
                    self.assert_rejected("loop")
                finally:
                    link.unlink()

    def test_runtime_manifest_fields_are_rejected_even_when_empty(self):
        for field in ("apps", "mcpServers", "hooks"):
            with self.subTest(field=field):
                self.metadata[field] = {}
                self.write_manifest()
                self.assert_rejected(field)
                del self.metadata[field]

    def test_undeclared_runtime_files_are_rejected(self):
        for relative in ("hooks/hooks.json", ".mcp.json", "mcp.json", ".app.json",
                         "skills/example/helper.py", "skills/example/package.json"):
            with self.subTest(relative=relative):
                path = self.root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("{}", encoding="utf-8")
                self.assert_rejected(path.name)
                path.unlink()
                if path.parent.name == "hooks":
                    path.parent.rmdir()

    def test_supporting_docs_and_agent_metadata_are_allowed(self):
        references = self.skill.parent / "references"
        references.mkdir()
        (references / "example.md").write_text("Example.", encoding="utf-8")
        agents = self.skill.parent / "agents"
        agents.mkdir()
        (agents / "openai.yaml").write_text("interface: {}\n", encoding="utf-8")
        self.assertEqual(self.run_validator().returncode, 0)


if __name__ == "__main__":
    unittest.main()
