# Changelog

All notable downstream changes are recorded here.

## [Unreleased]

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
