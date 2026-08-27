# My Agent Skills

A personal Codex plugin marketplace containing a traced snapshot of Agent Skills plus the original Architecture Gate plugin.

## Included Plugins

| Plugin | Version | Purpose |
|---|---:|---|
| `agent-skills` | `0.6.7` | 24 engineering workflow skills covering define, plan, build, verify, review, and ship. |
| `architecture-gate` | `0.1.0` | Evidence-led architecture triage before boundary-sensitive implementation. |

The `agent-skills` files come from a recorded source snapshot; upstream Git history is not imported into this repository. See [PROVENANCE.md](PROVENANCE.md) for the exact commit and license attribution.

For the upstream project's complete documentation, see [addyosmani/agent-skills README](https://github.com/addyosmani/agent-skills/blob/main/README.md).

## Install

```bash
codex plugin marketplace add ghyghoo8/my-agent-skills --ref main
codex plugin add agent-skills@my-agent-skills
codex plugin add architecture-gate@my-agent-skills
```

Start a new Codex session after installation so the skills are discovered.

## Architecture Gate

`$modular-architecture-design` performs read-only triage when a feature or structural refactor may change module responsibility, data or side-effect ownership, dependency direction, public contracts, or migration boundaries.

It selects exactly one path:

| Path | Result |
|---|---|
| `DIRECT` | Boundaries remain stable; implementation may proceed. |
| `BOUNDARY_NOTE` | Record a short local boundary note, then implement. |
| `ARCHITECTURE_GATE` | Stop business implementation until one canonical architecture brief is accepted. |
| `DISCOVERY` | Gather bounded missing evidence, then run triage again. |

File count, file length, possible reuse, an external API, or hypothetical scale are not sufficient reasons to trigger an architecture gate.

Explicit invocation:

```text
$modular-architecture-design Triage this change before implementation.
```

Implicit invocation is enabled but remains a soft gate. Projects that need deterministic enforcement can add this rule to their own `AGENTS.md`; the plugin never edits project rules automatically.

```markdown
Before a change that may alter responsibility, ownership, dependency direction,
public contracts, or migration boundaries, invoke `$modular-architecture-design`.
For `ARCHITECTURE_GATE` or `DISCOVERY`, do not modify business implementation
until the required acceptance or discovery-and-retriage step is complete.
```

## Repository Layout

```text
skills/                                      # vendored Agent Skills snapshot
agents/, commands/, hooks/, references/      # vendored supporting capabilities
plugins/architecture-gate/                   # original skills-only plugin
.agents/plugins/marketplace.json             # Codex marketplace
evals/architecture-gate/cases.yaml           # 14 routing cases
PROVENANCE.md                                 # source commit and attribution
UPSTREAM.md                                   # commit-id diff update workflow
```

## Upstream Updates

Updates do not merge or cherry-pick upstream history. Maintainers:

1. read the recorded baseline commit from [PROVENANCE.md](PROVENANCE.md);
2. compare it with a selected newer upstream commit;
3. review and apply the source diff;
4. update provenance and the changelog;
5. validate and commit the result in this repository.

See [UPSTREAM.md](UPSTREAM.md) for the exact workflow.

## Evaluation and Privacy

[evals/architecture-gate/cases.yaml](evals/architecture-gate/cases.yaml) contains positive, negative, boundary, and adversarial cases. Score the selected path and observable invariants, not fixed wording.

Architecture Gate is instruction-only: no MCP server, hooks, runtime scripts, network client, telemetry, or external dependency. Host sandbox and approval rules remain authoritative.

## Versioning and Contribution

Architecture Gate follows semantic versioning: PATCH preserves routing semantics, MINOR adds compatible capabilities or trigger scenarios, and MAJOR changes path meanings, pause behavior, or the output contract.

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [CHANGELOG.md](CHANGELOG.md). Licensed under the [MIT License](LICENSE). This repository is not affiliated with or endorsed by OpenAI.
