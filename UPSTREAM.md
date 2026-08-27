# Upstream Snapshot Updates

This repository vendors the capabilities of [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) without importing its Git history. [PROVENANCE.md](PROVENANCE.md) records the exact upstream commit used by the current snapshot.

An update compares the recorded baseline commit with a newer upstream commit, reviews that source diff, and applies only the accepted file changes in a new commit owned by this repository. Do not merge, rebase, subtree-add, or cherry-pick upstream commits into `main`.

The downstream `architecture-gate` plugin lives under `plugins/architecture-gate/`. Its files, marketplace entry, evaluation cases, and routing contract are outside upstream snapshot ownership.

## Configure a Fresh Clone

The `upstream` remote is local Git configuration and is not transferred by cloning. Add it once:

```bash
git remote add upstream https://github.com/addyosmani/agent-skills.git
git fetch upstream --tags
```

The inherited version validator uses the latest upstream release tag, so a fresh clone needs those tags locally. Fetched upstream commits and tags are comparison inputs only. Do not push them to `origin` or create a downstream release during routine synchronization.

Confirm the remotes before updating:

```bash
git remote -v
git status --short --branch
```

Expected ownership:

- `origin` points to `ghyghoo8/my-agent-skills`;
- `upstream` points to `addyosmani/agent-skills`.

## Apply an Upstream Commit Diff

Start from a clean downstream `main` branch. Read the current baseline commit ID from [PROVENANCE.md](PROVENANCE.md), fetch upstream, and choose the new commit explicitly:

```bash
git switch main
git fetch upstream --tags
git rev-parse upstream/main
git log --oneline <recorded-baseline>..<new-upstream-commit>
git diff --name-status <recorded-baseline>..<new-upstream-commit>
git diff --stat <recorded-baseline>..<new-upstream-commit>
```

Review the full name-status and content diff before changing the working tree. Create a downstream update branch, then apply the accepted changes for inherited paths:

```bash
git switch -c chore/sync-agent-skills-<upstream-version>
git diff --binary <recorded-baseline>..<new-upstream-commit> -- \
  .claude .claude-plugin .codex-plugin .gemini .gitattributes .github \
  .gitignore .opencode AGENTS.md CLAUDE.md LICENSE agents commands docs evals \
  hooks plugin.json references scripts skills \
  | git apply --index
```

Three inherited files contain intentional downstream edits and must be reconciled manually from the same upstream diff:

- `.agents/plugins/marketplace.json`;
- `README.md`;
- `CONTRIBUTING.md`.

Retain the `my-agent-skills` marketplace identity and both plugin entries. Preserve the downstream distribution section in the README and the Architecture Gate contribution rules while accepting compatible upstream improvements. Review any newly added upstream top-level path separately; the name-status check above is the guard against silently missing one.

After applying the source changes:

1. update the baseline commit ID and capture date in [PROVENANCE.md](PROVENANCE.md);
2. record the old and new upstream commit IDs in [CHANGELOG.md](CHANGELOG.md);
3. run the current upstream validation suite plus the Architecture Gate validators and eval-data checks;
4. review the complete downstream diff;
5. commit the update as one auditable snapshot-sync commit.

Push only after local validation succeeds:

```bash
git push origin main
```

Routine snapshot updates use a normal push. They never require a force-push because upstream history is not part of the downstream branch.

## Update Boundary

An accepted upstream source diff may update the vendored 24-skill pack, its agents, commands, hooks, references, scripts, documentation, or evals. It does not implicitly change the routing contract of `architecture-gate`; make those changes separately and version them according to the Architecture Gate rules in the README.
