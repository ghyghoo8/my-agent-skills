# Contributing

Contributions should improve the single `my-agent-skills` Codex plugin without expanding its runtime surface.

## Scope

- Plugin content belongs under `plugins/my-agent-skills/`.
- Keep the bundle skills-only: no bundled MCP, hooks, telemetry, network client, runtime script, or dependency.
- Prefer focused improvements to an existing Skill over overlapping new Skills.
- Keep Skill frontmatter discriminating: say what triggers the Skill and, when useful, what should not.
- Preserve project authority and user authorization boundaries.

Changes derived from `addyosmani/agent-skills` must follow [UPSTREAM.md](UPSTREAM.md). Do not import upstream commits or copy unreviewed platform packaging. Record source and adaptations in [PROVENANCE.md](PROVENANCE.md).

## Architecture Gate

Changes to `modular-architecture-design` must preserve:

- exactly one of `DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, or `DISCOVERY`;
- no business implementation writes under `ARCHITECTURE_GATE` or `DISCOVERY`;
- project evidence over generic heuristics;
- no gate based only on file count, file length, future reuse, an external API, “modularity,” or imagined scale;
- one canonical, minimal architecture brief.

Update `evals/architecture-gate/cases.yaml` whenever trigger, routing, pause, or output semantics change. Test observable behavior rather than fixed wording.

## Validation

Run the current bundled Codex validators against every Skill and the plugin root, parse JSON and YAML, check links and private data, and review `git diff --check` before committing. Include the commands and results in the change review.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
