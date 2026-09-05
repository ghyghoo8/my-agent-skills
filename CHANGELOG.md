# Changelog

All notable downstream changes are recorded here.

## [Unreleased]

## [1.0.0] - 2026-09-05

### Changed

- Accepted contextual confirmation and scoped delegation in ordinary workflows; reused settled requirements and approvals instead of asking again at every phase.
- Chose implementation slices and verification by complexity, affected behavior, and project-required checks, removing blanket file-count, full-suite, and per-increment commit requirements.
- Preserved architecture routing, no-write gates, adoption decision contracts, and item-scoped dialectical-review consent.
- Adapted upstream shared rate-limit guidance, performance regression guards, incomplete-plan protection, and production-schema / dependency-audit discovery vocabulary through `1c760d643497e9da289300e5eb2f5aca861503f7`.
- Kept the 27-Skill inventory; did not import the new constraint workflow, tooling, or packaging. See the [sync review](upstreams/addyosmani-agent-skills/reviews/2026-09-05.md).

### Migration

- Projects requiring repeated human checkpoints or full-suite tests must state those requirements explicitly. Existing mandatory gates remain binding.
- Plan and task files follow project authority; new defaults are `.codex/agent-state/plan.md` and `.codex/agent-state/todo.md`. Existing incomplete plans are preserved, not moved automatically.
- This major version changes ordinary pause semantics; it is a model-neutral instruction update, not a GPT-6 runtime adapter.

## [0.4.0] - 2026-09-01

### Added

- Added the original `capability-adoption-assessment` Skill with explicit Value, Cost, net-result, and `GO`/`PILOT`/`DEFER`/`NO-GO` output semantics.
- Added 13 adoption behavior cases, six cross-skill discovery cases, and one architecture-handoff case.

### Changed

- Routed open capability-to-workflow adoption decisions through the new specialist without making it a universal implementation gate.
- Added a compact default decision card and preserved the discovery metadata budget for 27 Skills.

## [0.3.0] - 2026-08-28

### Added

- Expanded performance guidance for query plans, index decisions, connection pools, and cache correctness.
- Added four downstream performance behavior cases.

### Changed

- Added pull-request lifecycle routing to `git-workflow-and-versioning` while preserving code-review ownership.
- Reviewed and adapted upstream changes through `f63ec56a3cc936408d792956ae583c3c96a825bd` without importing upstream history.

## [0.2.0] - 2026-08-28

### Added

- Added the original `project-dialectic-review` Skill with an explicit consent boundary and 16 behavior cases.
- Added a maintenance-only multi-upstream index and source descriptor without synchronizing newer upstream content.
- Added a canonical architecture brief and 22 cross-skill discovery cases.

### Changed

- Narrowed broad Skill descriptions and the meta-router while keeping all 26 capabilities in one Plugin.
- Established a checked-in discovery metadata budget below the v0.1 baseline.
- Clarified one-Plugin installation, migration from the legacy split identities, updating, and rollback.
- Generalized upstream updates to one review protocol with independent source IDs and commit state.

## [0.1.0] - 2026-08-27

### Added

- Published one new skills-only Codex plugin named `my-agent-skills`.
- Included 24 attributed engineering workflow Skills from upstream snapshot `7cb7a20bb38b199728d456999c725a0488490ab6`.
- Added the original `modular-architecture-design` Skill with four observable routing paths and 14 evaluation cases.
- Added commit-id-based upstream comparison and update guidance without importing upstream Git history.

### Changed

- Reorganized all installed content under `plugins/my-agent-skills/`.
- Replaced upstream host-specific packaging and instructions with Codex-native plugin, project-rule, MCP, and subagent boundaries.
- Reduced installation to one Marketplace registration and one Plugin installation.
