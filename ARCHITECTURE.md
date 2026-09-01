# Architecture

Status: `ARCHITECTURE_GATE` accepted on 2026-09-01

## Goal

Maintain one personal, skills-only Codex plugin that can evolve from multiple reviewed sources without importing their Git histories or making source management part of the runtime payload. Skill discovery should stay precise and progressively loaded as the library grows.

## Non-goals

- one plugin per upstream source;
- automatic mirroring or unattended application of upstream changes;
- runtime source lookup, networking, hooks, telemetry, or dependency loading;
- a universal value-versus-cost preflight before every implementation or mandatory fix;
- speculative capability layers that have no current Skill or measured discovery need.

## Planes and ownership

| Plane | Authority | Responsibility |
|---|---|---|
| Runtime product | `plugins/my-agent-skills/` | The single installable plugin, its Skills, and Skill-local or shared references |
| Upstream control | [`upstreams/index.yaml`](upstreams/index.yaml) and source descriptors | Stable source IDs, reviewed and applied commits, allowlisted mappings, licenses, and downstream adaptations |
| Evaluation | `evals/` | Observable routing, consent, pause, and non-speculation invariants |

The runtime tree stays flat by capability rather than by source. Source descriptors live outside the plugin, so Codex does not load maintenance metadata while matching Skills. Skill frontmatter remains the runtime discovery authority; the upstream index is not a second Skill catalog.

Each downstream artifact has at most one primary source owner. A second source may be recorded as reference material, but it cannot overwrite an owned artifact. A collision must be resolved by selecting one owner, creating a distinct downstream capability, or declining the import.

The plugin manifest is the version authority. Upstream versions and commits do not determine the downstream version.

## Dependency direction

Static Skill instruction dependencies point only to references bundled in the plugin; task-time project inspection follows each Skill's own contract. Evals inspect the runtime product without becoming a runtime dependency. The upstream control plane may produce reviewed patches into the runtime tree, but the plugin never reads `upstreams/` or `evals/`, and upstream content can never authorize an action.

## Upstream update boundary

Every source has a stable ID, unique Git remote name, immutable initial baseline, current reviewed-through commit, an effective applied commit for each allowlisted artifact, exact artifact-ID allowlists, and retained downstream adaptations. A Skill directory or one shared-reference file is an atomic artifact; every changed descendant is reviewed together. A mapping stores the common applied commit once and uses per-artifact overrides only when adoption diverges. Upstream repositories and their files are untrusted comparison data, not project instructions.

An update is one reviewed transaction:

1. Fetch the named remote and select an immutable candidate commit that is reachable from the descriptor's tracked remote branch and descends from `reviewed_through_commit`.
2. Diff `reviewed_through_commit..candidate` across the descriptor's mapped source roots; default-deny every artifact ID that is not allowlisted.
3. Review every changed path and classify each changed artifact as adopt, adapt, or reject.
4. Apply accepted content without importing Git ancestry.
5. Validate affected Skills, the whole plugin, metadata, evals, and the final diff.
6. Commit content, provenance, and source-state changes atomically.

The detailed protocol is in [`UPSTREAM.md`](UPSTREAM.md). A failed validation leaves the recorded state unchanged. A shipped sync is rolled back with a normal downstream revert; force-push and ancestry replacement are outside the design.

## Control-plane contract

- **Identity:** callers select a registered stable `source_id`; the index key and descriptor `source_id` must agree. Mutable source status exists only in the descriptor.
- **State:** sources are `active`, `paused`, or `retired`. Only `active` permits a routine review; none permits automatic application.
- **Inputs and outputs:** a review accepts one pinned candidate commit and produces an adopt/adapt/reject classification plus, when accepted, one atomic downstream diff.
- **Errors:** an unknown or mismatched ID, inactive source, unavailable or unrelated commit, owner collision, invalid metadata, or failed validation stops the sync without advancing recorded commits.
- **Side effects:** fetching adds Git objects locally; an accepted sync may change allowlisted runtime files and control metadata, then create and normally push one downstream commit. It never runs upstream code or writes to an upstream remote.
- **Invariants:** one runtime plugin, one primary owner per artifact, deny-by-default imports, one descriptor authority per source, and no upstream ancestry in downstream history.

## Metadata cutover and rollback

The initial migration copies the existing reviewed baseline and import inventory into one descriptor without advancing the commit or importing newer content. Cutover is complete only when the index resolves the descriptor, the 24 Skill and seven reference mappings match the downstream tree, and metadata validation passes. After cutover, the descriptor is the sole mutable source-state authority; provenance documents remain attribution narratives rather than parallel tracking state.

A schema change migrates the index and every affected descriptor in the same downstream commit. Before that commit ships, rollback means discarding the uncommitted metadata change. After it ships, rollback means reverting that downstream commit; do not restore a parallel legacy tracker or rewrite history.

## Capability adoption assessment

`capability-adoption-assessment` independently owns one question: whether a
specific new or existing capability is worth adopting into a named target
workflow. It triggers only while that adoption decision is open; it is not a
mandatory preflight for implementation, remediation, status reporting, vague
ideation, passive theses, or architecture-only review.

The assessment is read-only and must expose four separate decision results:

- incremental Value relative to the target workflow's current baseline;
- total Cost, including material one-time, recurring, risk, and opportunity cost;
- one net result: `POSITIVE`, `UNCERTAIN`, or `NEGATIVE`;
- exactly one recommendation: `GO`, `PILOT`, `DEFER`, or `NO-GO`.

One missing user expectation may be asked only when its answer could reverse the
decision. Otherwise the Skill uses the smallest stated assumption and gathers
only decision-changing evidence. `NO-GO` stops without architecture or
implementation planning. `PILOT` names a bounded reversible validation but does
not authorize it. A `GO` or `PILOT` hands off to
`modular-architecture-design` only when responsibility, ownership, dependency,
public-contract, or migration boundaries may change; the adoption Skill never
selects an architecture path itself.

The routing sequence is therefore conditional rather than universal:

```text
open adoption decision
    -> capability-adoption-assessment
    -> NO-GO: stop
    -> DEFER: bounded evidence action
    -> GO/PILOT + stable boundary: owning next workflow
    -> GO/PILOT + material boundary: modular-architecture-design
```

## Project dialectic review

`project-dialectic-review` is an independent Skill for user-provided ideas, architecture or refactor proposals, claims, and external material that could materially affect the current project.

- If the user already requests critique, dialectical review, challenge, or project-grounded optimization, that request is consent.
- Otherwise the Skill makes at most one neutral, scoped offer before critiquing the material.
- Silence, topic continuation, ambiguous acknowledgment, and consent given for a different item are not consent.
- A decline suppresses another offer for the same item.
- Direct implementation, summarization, ordinary questions, and explicitly invoked neighboring workflows retain their own route.
- External material is evidence to inspect, never instructions to execute.
- Consent to review does not authorize browsing, external models, file writes, implementation, or other external actions.

After consent, the smallest complete response identifies the project-relevant thesis, what remains valid, the strongest material tension or counterargument, evidence gaps, a revised thesis, and one bounded validation, optionally paired with the smallest evidence-backed optimization. It may conclude that no meaningful tension was found; disagreement must not be manufactured.

This is a soft, instruction-only routing behavior. It cannot guarantee interception like a hook or watcher, and it must not become a global preamble for every user message.

## Current verifiable slice

The current slice adds `capability-adoption-assessment` as a downstream-owned
decision specialist, routes only open capability-to-workflow adoption questions
to it, preserves adjacent workflow ownership, and covers its output, discovery,
and architecture-handoff boundaries with eval cases. It does not synchronize
newer upstream content or turn adoption assessment into a global gate.

## Alternative considered

Maintaining one plugin per upstream was rejected. It would expose maintenance provenance as installation complexity, weaken cross-source capability organization, and multiply routing and release surfaces. Separate source descriptors provide isolation without fragmenting the runtime product.
