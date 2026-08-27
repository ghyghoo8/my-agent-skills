# Upstream Updates

This repository tracks `addyosmani/agent-skills` by commit ID, not by Git ancestry. The recorded baseline is in [PROVENANCE.md](PROVENANCE.md).

## Mapping

| Upstream | Downstream |
|---|---|
| `skills/<name>/**` | `plugins/my-agent-skills/skills/<name>/**` |
| `references/*.md` | `plugins/my-agent-skills/references/*.md` |
| upstream manifests and host adapters | not imported |
| `modular-architecture-design` | downstream-only; never overwritten by upstream |

The downstream plugin version is independent of the upstream release version.

## Configure a Clone

```bash
git remote add upstream https://github.com/addyosmani/agent-skills.git
git fetch upstream --tags
git remote -v
```

Fetched refs are comparison inputs only. Never push upstream refs to `origin`.

## Review an Update

Start from a clean `main`, fetch upstream, select the new commit explicitly, and compare it with the baseline recorded in `PROVENANCE.md`:

```bash
git fetch upstream --tags
git log --oneline <recorded-baseline>..<selected-upstream-commit>
git diff --name-status <recorded-baseline>..<selected-upstream-commit> -- skills references
git diff <recorded-baseline>..<selected-upstream-commit> -- skills references
```

Review the complete diff before changing downstream files. Apply only accepted Skill and reference changes through the mapping above. Do not merge, rebase, subtree-add, or cherry-pick upstream commits.

Always reconcile these downstream boundaries manually:

- `skills/idea-refine/SKILL.md`: remain instruction-only; do not restore its shell helper.
- `skills/browser-testing-with-devtools/SKILL.md`: keep Codex MCP setup optional and user-authorized.
- `skills/context-engineering/SKILL.md`, `skills/code-simplification/SKILL.md`, and `skills/documentation-and-adrs/SKILL.md`: keep `AGENTS.md` as the primary Codex rule file.
- `skills/planning-and-task-breakdown/SKILL.md` and `skills/spec-driven-development/SKILL.md`: keep Skill-to-Skill handoffs; do not restore deleted slash-command dependencies.
- `skills/doubt-driven-development/SKILL.md` and `references/orchestration-patterns.md`: keep Codex subagent semantics.
- plugin manifest, Marketplace, README, licenses, provenance, changelog, and Architecture Gate files: downstream-owned.

New upstream files require an explicit decision. Do not import executables, hooks, MCP configuration, telemetry, network clients, dependencies, or other host-specific packaging merely because they appeared upstream.

## Finish the Sync

1. Update the baseline commit and capture date in `PROVENANCE.md` and `plugins/my-agent-skills/THIRD_PARTY_NOTICES.md`.
2. Choose the downstream SemVer change and update the plugin manifest and changelog.
3. Update affected eval cases.
4. Run all validation described in `AGENTS.md`.
5. Review and commit one auditable downstream snapshot-sync diff.
6. Push normally to `origin/main`; never force-push for routine upstream updates.
