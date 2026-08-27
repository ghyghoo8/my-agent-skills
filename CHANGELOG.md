# Changelog

All notable downstream changes are recorded here. Upstream Agent Skills releases keep their own version in `.codex-plugin/plugin.json`; this changelog also tracks the separately versioned Architecture Gate plugin.

## [Unreleased]

## Architecture Gate [0.1.0] - 2026-08-27

### Added

- Added the instruction-only `architecture-gate` Codex plugin and `modular-architecture-design` skill.
- Added four observable routes: `DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, and `DISCOVERY`.
- Added minimal triage guidance, a canonical architecture brief template, and routing evaluation cases.
- Added repo marketplace entries for both the imported `agent-skills` plugin and `architecture-gate`.
- Added public provenance, security, versioning, and upstream synchronization documentation.

### Distribution

- Vendored the `addyosmani/agent-skills` capability snapshot at upstream commit `7cb7a20bb38b199728d456999c725a0488490ab6` without importing upstream Git history. Future updates use reviewed diffs between recorded commit IDs.
- Adapted version validation for snapshot history by comparing each marketplace entry with its canonical plugin manifest instead of requiring an upstream tag in the downstream ancestry.
