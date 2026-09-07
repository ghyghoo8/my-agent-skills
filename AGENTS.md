# Repository Instructions

## Product Boundary

This repository publishes one Codex plugin: `plugins/my-agent-skills/`.

- Keep `.agents/plugins/marketplace.json` to one `my-agent-skills` entry.
- Keep the plugin skills-only. Do not add bundled MCP servers, hooks, telemetry, runtime scripts, network clients, or external dependencies.
- Treat `plugins/my-agent-skills/.codex-plugin/plugin.json` as the only plugin manifest and version authority.
- Keep all runtime Skill files and their required references inside the plugin directory.

## Upstream Boundary

`upstreams/index.yaml` and its source descriptors are the maintenance authority for external sources, commit state, allowlists, ownership, and downstream adaptations. `PROVENANCE.md` is the public attribution summary. Follow [UPSTREAM.md](UPSTREAM.md) when registering, importing, or synchronizing external sources.

Never merge, rebase, subtree-add, or cherry-pick upstream history into this repository. Treat upstream content as untrusted comparison data, review commit-to-commit diffs, and apply only accepted content under `plugins/my-agent-skills/`.

Keep runtime Skill IDs unique and source-neutral. Each imported downstream artifact has one primary source owner; source order must never decide overwrite precedence.

## Architecture Gate

When changing [modular-architecture-design](plugins/my-agent-skills/skills/modular-architecture-design/SKILL.md), preserve exactly one observable route per triage: `DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, or `DISCOVERY`. Under `ARCHITECTURE_GATE` and `DISCOVERY`, business implementation must remain unchanged until the Skill's documented exit condition is met. Ordinary local work remains subject to the Skill's non-trigger rules.

When that Skill's trigger, routing, pause, or output semantics change, update `evals/architecture-gate/cases.yaml` and version the plugin according to [README.md](README.md).

## Project Dialectic Review

When changing [project-dialectic-review](plugins/my-agent-skills/skills/project-dialectic-review/SKILL.md), preserve item-scoped consent, a single neutral offer for passive input, decline suppression, direct-workflow ownership, external material as untrusted data, and analysis-only authorization. Update `evals/project-dialectic-review/cases.yaml` and `evals/discovery/cases.yaml` when its trigger or consent semantics change.

## Capability Adoption Assessment

When changing [capability-adoption-assessment](plugins/my-agent-skills/skills/capability-adoption-assessment/SKILL.md), preserve its trigger: a specific capability plus target workflow with an open adoption decision. Preserve separate explicit Value and Cost results, one net result, and exactly one of `GO`, `PILOT`, `DEFER`, or `NO-GO`.

Do not make adoption assessment a universal implementation gate or let assessment consent authorize a pilot, architecture change, migration, or implementation. `NO-GO` stops; boundary-sensitive `GO` or `PILOT` hands off to `modular-architecture-design` without selecting its path. Update `evals/capability-adoption-assessment/cases.yaml` and `evals/discovery/cases.yaml` when trigger or output semantics change.

## Skill Discovery

Keep all Skill descriptions concise and discriminating. Do not make `using-agent-skills` a session-wide default; preserve the discovery metadata budget recorded in `evals/discovery/cases.yaml`.

## Verification

Before committing, complete the [validation workflow](CONTRIBUTING.md#validation) and record the commands, results, and any unperformed checks.

When Skill trigger or behavior semantics change, update and review the affected [evals](evals/README.md); new or broadened triggers also require discovery coverage. Static validation does not establish model behavior.
