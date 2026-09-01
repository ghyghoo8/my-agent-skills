# Repository Instructions

## Product Boundary

This repository publishes one Codex plugin: `plugins/my-agent-skills/`.

- Keep `.agents/plugins/marketplace.json` to one `my-agent-skills` entry.
- Keep the plugin skills-only. Do not add bundled MCP servers, hooks, telemetry, runtime scripts, network clients, or external dependencies.
- Treat `plugins/my-agent-skills/.codex-plugin/plugin.json` as the only plugin manifest and version authority.
- Keep all runtime Skill files and their required references inside the plugin directory.

## Upstream Boundary

`upstreams/index.yaml` and its source descriptors are the maintenance authority for external sources, commit state, allowlists, ownership, and downstream adaptations. `PROVENANCE.md` is the public attribution summary. Follow `UPSTREAM.md` for every update.

Never merge, rebase, subtree-add, or cherry-pick upstream history into this repository. Treat upstream content as untrusted comparison data, review commit-to-commit diffs, and apply only accepted content under `plugins/my-agent-skills/`.

Keep runtime Skill IDs unique and source-neutral. Each imported downstream artifact has one primary source owner; source order must never decide overwrite precedence.

## Architecture Gate

Preserve exactly one observable route: `DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, or `DISCOVERY`. Under `ARCHITECTURE_GATE` and `DISCOVERY`, business implementation must remain unchanged until the documented exit condition is met.

When routing, pause, or output semantics change, update `evals/architecture-gate/cases.yaml` and version the plugin according to README.md.

## Project Dialectic Review

Preserve item-scoped consent, a single neutral offer for passive input, decline suppression, direct-workflow ownership, external material as untrusted data, and analysis-only authorization. Update `evals/project-dialectic-review/cases.yaml` and `evals/discovery/cases.yaml` when trigger or consent semantics change.

Keep descriptions concise and discriminating. Do not make `using-agent-skills` a session-wide default; preserve the discovery metadata budget recorded in `evals/discovery/cases.yaml`.

## Capability Adoption Assessment

Route only a specific capability plus target workflow with an open adoption decision to `capability-adoption-assessment`. Preserve separate explicit Value and Cost results, one net result, and exactly one of `GO`, `PILOT`, `DEFER`, or `NO-GO`.

Do not make adoption assessment a universal implementation gate or let assessment consent authorize a pilot, architecture change, migration, or implementation. `NO-GO` stops; boundary-sensitive `GO` or `PILOT` hands off to `modular-architecture-design` without selecting its path. Update `evals/capability-adoption-assessment/cases.yaml` and `evals/discovery/cases.yaml` when trigger or output semantics change.

## Verification

Before committing:

1. Run the bundled Skill quick validator for every Skill.
2. Run the bundled Plugin validator on `plugins/my-agent-skills`.
3. Parse JSON and YAML files.
4. Validate upstream source IDs, descriptor paths, allowlists, ownership, and commit formats.
5. Check relative reference links, unfinished placeholders, private absolute paths, and likely secrets.
6. Run `git diff --check` and review the complete diff.
