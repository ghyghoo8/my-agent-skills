# Contributing

Contributions should improve the single `my-agent-skills` Codex plugin without expanding its runtime surface.

## Scope

- Plugin content belongs under `plugins/my-agent-skills/`.
- Keep the bundle skills-only: no bundled MCP, hooks, telemetry, network client, runtime script, or dependency.
- Prefer focused improvements to an existing Skill over overlapping new Skills.
- Keep Skill frontmatter discriminating: say what triggers the Skill and, when useful, what should not.
- Preserve project authority and user authorization boundaries.

Changes derived from an external source must be registered under `upstreams/` and follow [UPSTREAM.md](UPSTREAM.md). Do not import upstream commits or copy unreviewed platform packaging. Preserve source ownership, exact commit state, licenses, and downstream adaptations.

New or broadened Skill triggers must update `evals/discovery/cases.yaml` and remain within its metadata budget. Prefer improving an existing owner over adding an overlapping Skill.

## Capability Adoption Assessment

Changes to `capability-adoption-assessment` must preserve a specific capability and target workflow, an open adoption decision, separate explicit Value and Cost results, one net result, and exactly one `GO`, `PILOT`, `DEFER`, or `NO-GO`. It must not reopen accepted work, delay mandatory fixes, or infer authorization for a pilot, migration, architecture change, or implementation. Boundary-sensitive positive recommendations hand off to `modular-architecture-design` without choosing its path.

Update `evals/capability-adoption-assessment/cases.yaml` and the cross-skill discovery cases whenever trigger, decision, output, or handoff semantics change.

## Architecture Gate

Changes to `modular-architecture-design` must preserve:

- exactly one of `DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, or `DISCOVERY`;
- no business implementation writes under `ARCHITECTURE_GATE` or `DISCOVERY`;
- project evidence over generic heuristics;
- no gate based only on file count, file length, future reuse, an external API, “modularity,” or imagined scale;
- one canonical, minimal architecture brief.

Update `evals/architecture-gate/cases.yaml` whenever trigger, routing, pause, or output semantics change. Test observable behavior rather than fixed wording.

## Project Dialectic Review

Changes to `project-dialectic-review` must preserve one neutral offer before unsolicited critique, item-scoped explicit consent, decline suppression, ownership by direct or explicitly selected workflows, external material as untrusted data, and analysis-only authorization. Update its behavior cases whenever those semantics change.

## Validation

Before committing, complete these static checks:

1. Run the bundled Codex Skill quick validator for every Skill and the Plugin validator for `plugins/my-agent-skills/`, using the commands below.
2. Parse all repository JSON and YAML, including hidden paths such as `.agents/plugins/marketplace.json`.
3. Validate upstream source IDs, descriptor paths, exact allowlists, unique primary ownership, and 40-character hexadecimal commit IDs against [UPSTREAM.md](UPSTREAM.md).
4. Check relative reference links, unfinished placeholders, private absolute paths, and likely secrets. Check Skill inventory, unique names, and the discovery metadata budget in [the discovery cases](evals/discovery/cases.yaml).
5. Run `git diff --check` and review the complete diff, including newly added files.

Run from the repository root. The validators belong to the local Codex system Skills, not this repository. Use an existing project `.venv/bin/python` when available; otherwise use an existing Python 3 with PyYAML. The example defaults to `python3` outside a project environment. To select another existing interpreter, set `validation_python` to its executable path before running the block.

```sh
(
  set -eu
  validation_codex_dir="${CODEX_HOME:-$HOME/.codex}"
  if [ -z "${validation_python:-}" ]; then
    if [ -x .venv/bin/python ]; then
      validation_python=.venv/bin/python
    else
      validation_python=python3
    fi
  fi
  validation_system_skills="$validation_codex_dir/skills/.system"
  validation_quick="$validation_system_skills/skill-creator/scripts/quick_validate.py"
  validation_plugin="$validation_system_skills/plugin-creator/scripts/validate_plugin.py"
  test -f "$validation_quick"
  test -f "$validation_plugin"
  "$validation_python" -c 'import yaml'
  for validation_skill in plugins/my-agent-skills/skills/*/SKILL.md; do
    "$validation_python" "$validation_quick" "${validation_skill%/SKILL.md}"
  done
  "$validation_python" "$validation_plugin" plugins/my-agent-skills
)
```

If an interpreter, PyYAML, or a bundled validator is unavailable, report the missing check; do not install tools by default or claim validation passed. These validator commands cover item 1 only.

When behavior or trigger semantics change, update and review the affected cases selected from [the eval inventory](evals/README.md); this includes the performance, workflow-proportionality, and security groups when relevant. New or broadened triggers must also update discovery cases. Follow the eval guide's clean-context interception and non-interception review, and distinguish contract review from full-model execution. Ordinary documentation edits do not require a full behavioral evaluation.

Include the commands, results, and checks not performed in the change review. Static validator success is not evidence that model behavior passed.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
