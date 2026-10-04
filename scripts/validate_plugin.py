#!/usr/bin/env python3
"""Static checks for this repository's skills-only Codex compatibility plugin.

Uses only Python's standard library and never executes bundle content. This is
repository maintenance tooling, not the official plugin-creator validator.
Skill frontmatter, repository metadata and model behavior have separate checks.
"""

import argparse
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys


NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
SEMVER = re.compile(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
    r"(?:\+([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?"
)
CONTENT_SUFFIXES = {
    ".md", ".txt", ".json", ".yaml", ".yml",
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico",
}
RUNTIME_FILES = {
    ".mcp.json", "mcp.json", ".app.json", "hooks.json", "package.json",
    "package-lock.json", "requirements.txt", "pyproject.toml", "uv.lock",
}


def unique_object(pairs):
    """Do not silently accept conflicting manifest keys."""
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError(f"invalid JSON numeric constant: {value}")


def validate_plugin(root):
    """Return actionable errors; an empty list means these static checks passed."""
    errors = []
    if not root.is_dir():
        return ["plugin root must be an existing directory"]
    root = root.resolve(strict=True)

    def text_field(mapping, key, owner, limit=None, required=False, multiline=False):
        if key not in mapping and not required:
            return
        value = mapping.get(key)
        label = f"{owner}.{key}"
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: expected a non-empty string")
        elif limit is not None and len(value) > limit:
            errors.append(f"{label}: maximum length is {limit}")
        elif any(ord(c) < 32 and not (multiline and c in "\n\r\t") for c in value):
            errors.append(f"{label}: unsupported control character")

    def string_list(mapping, key, owner, count_limit=None, item_limit=None):
        if key not in mapping:
            return
        value = mapping[key]
        if not isinstance(value, list):
            errors.append(f"{owner}.{key}: expected a list of strings")
            return
        if count_limit is not None and len(value) > count_limit:
            errors.append(f"{owner}.{key}: maximum item count is {count_limit}")
        for index, item in enumerate(value):
            text_field({"value": item}, "value", f"{owner}.{key}[{index}]", item_limit)

    def resource(value, label, directory=False):
        if (not isinstance(value, str) or not value.startswith("./")
                or ".." in PurePosixPath(value).parts or "\\" in value):
            errors.append(f"{label}: expected a ./ path without parent components")
            return None
        path = root / value
        try:
            resolved = path.resolve(strict=True)
            resolved.relative_to(root)
        except (OSError, RuntimeError, ValueError):
            errors.append(f"{label}: path must exist and stay inside the plugin")
            return None
        if (directory and not path.is_dir()) or (not directory and not path.is_file()):
            errors.append(f"{label}: expected a {'directory' if directory else 'file'}")
            return None
        return path

    manifest = root / ".codex-plugin" / "plugin.json"
    if not manifest.is_file():
        errors.append(".codex-plugin/plugin.json: expected a regular manifest file")
        metadata = None
    else:
        try:
            metadata = json.loads(
                manifest.read_text(encoding="utf-8"),
                object_pairs_hook=unique_object,
                parse_constant=reject_constant,
            )
            if not isinstance(metadata, dict):
                raise ValueError("top level must be a JSON object")
        except (OSError, UnicodeError, ValueError) as error:
            errors.append(f".codex-plugin/plugin.json: {error}")
            metadata = None

    if metadata is not None:
        for field, limit in (("name", 64), ("version", 64), ("description", 1024)):
            text_field(metadata, field, "manifest", limit, required=True, multiline=field == "description")
        name = metadata.get("name")
        if isinstance(name, str) and not NAME.fullmatch(name):
            errors.append("manifest.name: use ASCII letters, digits, _ or -, starting with a letter or digit")
        version = metadata.get("version")
        if isinstance(version, str):
            match = SEMVER.fullmatch(version)
            if not match or (match[4] and any(
                item.isdigit() and len(item) > 1 and item.startswith("0")
                for item in match[4].split(".")
            )):
                errors.append("manifest.version: expected a semantic version")
        for field in ("id", "homepage", "repository", "license"):
            text_field(metadata, field, "manifest")
        string_list(metadata, "keywords", "manifest")
        author = metadata.get("author")
        if not isinstance(author, dict):
            errors.append("manifest.author: expected an object")
        else:
            text_field(author, "name", "author", 120, required=True)
            text_field(author, "email", "author", 320)
            text_field(author, "url", "author", 2048)

        interface = metadata.get("interface")
        if not isinstance(interface, dict):
            errors.append("manifest.interface: expected an object")
        else:
            for field, limit in (("displayName", 80), ("shortDescription", 240),
                                 ("longDescription", 4000), ("developerName", 120)):
                text_field(interface, field, "interface", limit, required=True,
                           multiline=field == "longDescription")
            for field in ("category", "websiteURL", "privacyPolicyURL", "termsOfServiceURL",
                          "supportURL", "brandColor"):
                text_field(interface, field, "interface")
            string_list(interface, "capabilities", "interface", 20, 120)
            string_list(interface, "defaultPrompt", "interface", 3)
            for field in ("composerIcon", "logo"):
                if field in interface:
                    resource(interface[field], f"interface.{field}")
            if "screenshots" in interface:
                screenshots = interface["screenshots"]
                if not isinstance(screenshots, list):
                    errors.append("interface.screenshots: expected a list of paths")
                else:
                    for index, path in enumerate(screenshots):
                        resource(path, f"interface.screenshots[{index}]")

        for field in ("apps", "mcpServers", "hooks", "extensions"):
            if field in metadata:
                errors.append(f"manifest.{field}: outside this repository's skills-only boundary")
        skills = resource(metadata.get("skills"), "manifest.skills", directory=True)
        if skills is not None:
            if skills.resolve() != root / "skills":
                errors.append("manifest.skills: must point to the root skills/ directory")
            children = sorted(skills.iterdir())
            if not children:
                errors.append("skills/: at least one direct Skill directory is required")
            for child in children:
                skill_manifest = child / "SKILL.md"
                if child.name.startswith(".") or child.is_symlink() or not child.is_dir():
                    errors.append(f"skills/{child.name}: expected a visible, real Skill directory")
                elif not skill_manifest.is_file() or skill_manifest.is_symlink():
                    errors.append(f"skills/{child.name}/SKILL.md: expected a regular file")
                else:
                    try:
                        if not skill_manifest.read_text(encoding="utf-8").strip():
                            errors.append(f"skills/{child.name}/SKILL.md: empty instructions")
                    except (OSError, UnicodeError) as error:
                        errors.append(f"skills/{child.name}/SKILL.md: {error}")

    # Do not follow symlinks or execute content. A closed content surface also
    # catches undeclared runtime files that a host could discover automatically.
    def walk_error(error):
        errors.append(f"plugin content: {error}")

    for directory, directories, filenames in os.walk(root, onerror=walk_error, followlinks=False):
        for name in sorted(directories + filenames):
            path = Path(directory) / name
            relative = path.relative_to(root)
            label = relative.as_posix()
            if path.is_symlink():
                errors.append(f"{label}: symbolic links are not allowed in the bundle")
            elif relative.parts[0] not in {".codex-plugin", "skills", "references", "assets"} and path.is_dir():
                errors.append(f"{label}: directory is outside the skills-only content layout")
            elif (relative.parts[0] == ".codex-plugin" and len(relative.parts) > 1
                  and label != ".codex-plugin/plugin.json"):
                errors.append(f"{label}: only .codex-plugin/plugin.json belongs in the manifest directory")
            elif path.is_file():
                if name == "plugin.json" and path != manifest:
                    errors.append(f"{label}: additional plugin manifest authority is not allowed")
                elif name in RUNTIME_FILES or (path.suffix.lower() not in CONTENT_SUFFIXES and name != "LICENSE"):
                    errors.append(f"{label}: runtime or dependency files are outside the skills-only boundary")
                elif path.stat().st_mode & 0o111:
                    errors.append(f"{label}: executable bundle content is not allowed")
            elif not path.is_dir():
                errors.append(f"{label}: expected a regular file or directory")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plugin", type=Path, help="plugin root (for example plugins/my-agent-skills)")
    arguments = parser.parse_args()
    try:
        errors = validate_plugin(arguments.plugin)
    except (OSError, RuntimeError, ValueError) as error:
        errors = [f"plugin content could not be checked: {error}"]
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("PASS: Plugin manifest, resources, Skill layout and skills-only boundary")
    return 0


if __name__ == "__main__":
    sys.exit(main())
