# Provenance

## Downstream Plugin

`my-agent-skills` is a new Codex plugin maintained in this repository. It is not a GitHub fork, does not reuse the upstream plugin identity or version, and does not contain upstream Git history.

The plugin manifest, Marketplace entry, Codex-specific packaging, `capability-adoption-assessment`, `modular-architecture-design`, and `project-dialectic-review` Skills, their contracts, and their evals were authored for this repository.

## Upstream Skill Snapshot

The plugin includes adapted material from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills), licensed under MIT. Its initial imported snapshot was upstream commit [`7cb7a20bb38b199728d456999c725a0488490ab6`](https://github.com/addyosmani/agent-skills/commit/7cb7a20bb38b199728d456999c725a0488490ab6), captured on 2026-08-27. Current reviewed and applied commit state and the exact allowlist live only in [`upstreams/addyosmani-agent-skills/source.yaml`](upstreams/addyosmani-agent-skills/source.yaml).

Imported scope:

- 24 upstream Skill workflows and their Markdown support files;
- shared references required by those Skills.

Codex adaptations:

- moved all Skill content under the single downstream plugin root;
- narrowed selected frontmatter descriptions for precise Codex discovery without changing their workflow ownership;
- removed the `idea-refine` initializer script and expressed its behavior as instructions;
- removed active dependencies on host-specific tools, slash commands, rule files, personas, and orchestration, while retaining compatibility mentions where they are useful context;
- kept Chrome DevTools MCP optional and user-configured rather than bundling it.

Not imported as product surface: upstream history, identity/version manifests, Claude/Gemini/OpenCode packaging, slash commands, personas, hooks, CI, runtime helpers, repository documentation, or upstream eval infrastructure.

Traceability comes from the stable source ID, exact commit state, retained MIT notices, descriptor mapping, and reviewable downstream sync commits. Inherited text is not represented as original downstream authorship.

Public format references used for downstream packaging:

- [Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex MCP](https://developers.openai.com/codex/mcp)
- [Codex AGENTS.md](https://developers.openai.com/codex/guides/agents-md)

Use of public documentation and bundled validators does not make this an OpenAI product or imply endorsement by OpenAI or the upstream project.
