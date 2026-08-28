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

Run the current bundled Codex validators against every Skill and the plugin root, parse JSON and YAML, check links and private data, and review `git diff --check` before committing. Include the commands and results in the change review.

By contributing, you agree that your contribution is licensed under the repository's MIT License.
