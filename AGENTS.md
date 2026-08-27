# Repository Instructions

## Product Boundary

This repository publishes one Codex plugin: `plugins/my-agent-skills/`.

- Keep `.agents/plugins/marketplace.json` to one `my-agent-skills` entry.
- Keep the plugin skills-only. Do not add bundled MCP servers, hooks, telemetry, runtime scripts, network clients, or external dependencies.
- Treat `plugins/my-agent-skills/.codex-plugin/plugin.json` as the only plugin manifest and version authority.
- Keep all runtime Skill files and their required references inside the plugin directory.

## Upstream Boundary

The 24 inherited workflows are a reviewed content snapshot of `addyosmani/agent-skills`. `PROVENANCE.md` records the baseline commit and downstream adaptations. Follow `UPSTREAM.md` for updates.

Never merge, rebase, subtree-add, or cherry-pick upstream history into this repository. Review commit-to-commit source diffs and apply accepted content under `plugins/my-agent-skills/`.

## Architecture Gate

Preserve exactly one observable route: `DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, or `DISCOVERY`. Under `ARCHITECTURE_GATE` and `DISCOVERY`, business implementation must remain unchanged until the documented exit condition is met.

When routing, pause, or output semantics change, update `evals/architecture-gate/cases.yaml` and version the plugin according to README.md.

## Verification

Before committing:

1. Run the bundled Skill quick validator for every Skill.
2. Run the bundled Plugin validator on `plugins/my-agent-skills`.
3. Parse JSON and YAML files.
4. Check relative reference links, unfinished placeholders, private absolute paths, and likely secrets.
5. Run `git diff --check` and review the complete diff.
