# Changelog

All notable downstream changes are recorded here.

## [5.1.0] - 2026-09-22

### Added

- Review derived filesystem targets by their source, resolved containment, protected ownership evidence and check/use safety; reject unsafe cleanup without broadening its target.
- Preserve restartable task evidence and existing authorization when summarizing context; reuse established specification systems instead of creating duplicate documents.
- Add conditional visual-reference guidance, rendered UI completion checks, explicit log entry-point attribution, compact runbooks and project-defined error-budget release checks.

### Changed

- Move security implementation examples into a Skill-local reference loaded for the relevant risk, retaining deployment-wide rate limiting and supply-chain safeguards.
- Selectively adapt the registered upstream update while retaining all 27 Skill descriptions, existing interview/Goal/architecture boundaries and the skills-only plugin surface. See the [sync review](upstreams/addyosmani-agent-skills/reviews/2026-09-22.md) for accepted and rejected artifacts and validation limits.

## [5.0.1] - 2026-09-16

### Fixed

- Compare a proposed decision with existing acceptance and execution authorization before pausing. Reuse same-scope acceptance across sessions; distinguish delegated technical implementation from changes to business meaning or acceptance criteria.
- Expose known human decisions during readiness preparation. For an unresolved architecture brief, present one concrete, scoped decision using a permitted native choice or text fallback; acceptance does not expand implementation authorization.
- Reuse pending questions and valid evidence during Goal waits. Continue independent work, avoid unchanged full-history scans and repeated requests, and obey host blocking/resume rules without synthetic turns or a second state ledger.
- Preserve the four architecture routes, their existing acceptance/write boundaries, Goal tool contracts and discovery metadata. This patch clarifies their application; it does not add a trigger, universal approval step or runtime hook.

## [5.0.0] - 2026-09-10

### Changed

- Assess the entire delegated delivery scope before sustained execution with reduced human decisions. Manual checks and current-task automatic handoffs share one planning-owned assessment; substantial module and refactor work can use it without inheriting milestone-only roadmap or model requirements.
- Define milestones as delivery acceptance nodes. Check consequential decisions, actual dependencies and environment, decision delegation, verification/recovery, and expected human checkpoints; a runnable first task or all-DONE task list cannot establish delivery acceptance.
- Prefer explicitly authorized Goal execution after a passing assessment. Inspect and reuse a compatible unfinished Goal, preserve conflicts and uncertain outcomes, and keep Goal lifecycle separate from the canonical business queue. Goal completion requires the actual agreed endpoint and acceptance evidence.
- Enable bounded parallel execution of independent READY module tasks under one controller, Goal and queue. Partition shared write/resource ownership, respect host/project limits, and require integration evidence before dependent dispatch or milestone acceptance.

### Performance

- Load readiness assessment separately from execution choices and Goal lifecycle. Keep milestone-specific detail in its existing reference; check-only and insufficient-readiness paths avoid execution-only instructions. Preserve admission and acceptance rules, with context-size measurements and targeted behavior regressions recorded in the [delivery report](evals/planning-and-task-breakdown/execution-handoff-5.0.0.md).

### Migration

- Replace the 4.2 first-task readiness check with the whole delegated-scope assessment and scoped Goal choice. This revises the admission and handoff contract, so the plugin uses a major version.
- Preserve existing plans, queue states, accepted decisions and ordinary execution authorization. Do not infer Goal consent from a plain start request; existing explicit Goal preferences remain applicable. Check-only, planning-only, decline and view-plan choices retain their limits.
- The plugin remains skills-only. Automatic detection and selection-card rendering are host-dependent; missing Goal support is disclosed without silent substitution. Source validation does not install or publish the plugin.

## [4.2.0] - 2026-09-10

### Added

- Add a scoped execution choice after a current-task milestone handoff is complete and implementation authorization is the only missing prerequisite. Prefer a permitted native selection card with execute, view-plan, and defer options; fall back to a concise text question when no suitable host tool is available.
- Keep eligibility with `planning-and-task-breakdown`; specification, milestone documentation, and explicit routing link to that owner after completing their requested work. Document existence alone never establishes executable readiness.
- Preserve READY's authorization contract, single queue ownership, prior authorization, explicit planning-only scope, decline suppression, and stale-reply rechecks. The compatible trigger addition does not add a hook, watcher, runtime dependency, automatic model switch, or background task.

## [4.1.0] - 2026-09-10

### Fixed

- Made internal producer-consumer contract changes discoverable by `modular-architecture-design`, including contained changes with stable owners. Its existing `BOUNDARY_NOTE` route remains sufficient; private helpers and edits with unchanged boundaries and contracts remain outside implicit triage.
- Added the corresponding API/router handoff so a general interface-design match does not hide an existing inter-module contract change; documenting an accepted unchanged API stays with its explicit owner.
- Reconciled the architecture entry description with its existing routing reference. This compatible trigger correction uses a minor version; the four paths, implementation authorization, and gate exit conditions are unchanged.

### Evaluation

- Completed the original 73 behavior cases, preserved all first-pass results, independently graded factual and routing followups, and verified all 15 primary coding runs. See the [evaluation report](evals/planning-and-task-breakdown/model-evaluation-2026-09-10.md) for the final audit and sample limits.

- Retained the frozen 4.0.0 behavioral baseline and added separate affected-case reruns for this correction. Supplemented missing facts in planning and summary fixtures without replacing original results or relaxing their invariants.
- Corrected an overstrict discovery owner assertion after independent adjudication, preserving legitimate initial intent interviews and adding explicit-interview and settled-intent specification contrasts. Original FAIL records remain intact; no interview/specification runtime change was made.
- Kept model-comparison contract revisions and independent grading separate from Skill behavior results. The evaluation report records executed coverage and remaining evidence limits.

## [4.0.0] - 2026-09-10

### Changed

- Organize milestone delivery around five core responsibilities: control, solution/task planning, implementation/integration, verification, and independent review. Permit compatible roles to share an owner, with dedicated investigation, integration, or recovery only when needed; preserve one queue owner and existing decision/acceptance authority.
- Admit Astra xhigh as the first implementation choice and Sol xhigh as the second. Keep Terra ultra as the minimum admitted execution baseline, Sol ultra as an enhanced execution option, and Astra ultra for control, planning, key independent review, and high-uncertainty work. These are named role choices, not a cross-model performance ranking.
- Add responsibility, integration ownership, decision scope, verification/review evidence, and project acceptance responsibility to task cards and launch/resume handoffs. Self-tests and component success cannot substitute for required independent review or working integration.
- Evaluate configuration availability per role. An execution host can use admitted xhigh workers under compliant ultra control/review elsewhere; missing required-role settings block affected work only. Preserve effective-configuration checks and prohibit silent retry substitutions even between admitted pairs.

### Migration

- This major version revises the execution configuration and handoff output contract. Replace universal ultra checks with the exact admitted pairs and their role constraints; Astra xhigh and Sol xhigh are now explicit choices, while unlisted efforts or models remain unapproved.
- Preserve existing assignments and state ownership. Do not create five agents or new human approval gates to populate role fields; use the project's acceptance and release rules. Initial second-choice selection does not authorize changing an already selected worker due to cost, latency, rate limits, or failure.
- The three document prerequisites and authorized work scope remain unchanged. Source updates do not install the plugin, change active models, or launch project implementation.

## [3.0.0] - 2026-09-10

### Changed

- Replaced the milestone workflow's economical/balanced profiles with the approved quality-first policy: Terra ultra is the hard configuration floor, Astra ultra the default controller and key reviewer, and Sol ultra an option for complex implementation.
- Applied the floor to all participating roles, including subagents, reviewers, retries, and fallback workers. Availability, token cost, and speed do not authorize a lower model, lower effort, another provider, or an unverified equivalent.
- Require supported/effective configurations to be established before worker dispatch, including inherited settings. Preserve planning artifacts and explicit execution blockers when no compliant executor is available; do not silently map Codex ultra to API max.
- Kept the three document prerequisites, one task-state authority, and actual acceptance evidence. Stronger models and subscription access do not establish quality or unlimited capacity.

### Migration

- This major version changes model recommendations and the execution configuration contract. Replace old economic/medium task profiles and inspect child-agent, retry, and fallback settings before continuing the milestone queue.
- The approved named combinations are `gpt-5.6-terra`, `gpt-5.6-sol`, and `gpt-6-astra`, each with `ultra`. Future replacements require an explicit policy update. This instruction-only change does not install a plugin, switch the active model, or launch implementation.

## [2.0.0] - 2026-09-10

### Changed

- Require three existing inputs before entering the milestone execution workflow: a current authoritative document, at least one detailed development document, and an explicit milestone roadmap with outcomes, dependency/order information, and exit conditions.
- Prepare or repair missing inputs within authorized documentation work before deriving task cards and the executable queue. Do not count an outline, command list, vague phase list, or newly generated task cards as satisfying the entry prerequisites.
- Derive execution work from the existing roadmap and maintain its identities and gates; retain model-strength recommendations and the single state target. Existing valid documents do not require repeated approval.

### Migration

- This major version changes the milestone workflow's entry and pause contract. Provide the three input references or complete prerequisite preparation first. They need not be three separate files; an explicit roadmap section in a detailed development document is sufficient.
- Ordinary compact planning and existing implementation authorization retain their prior scope. A milestone request cannot bypass its prerequisites by being relabeled as compact planning. No plugin installation or model switch is implied by this source update.

## [1.1.0] - 2026-09-10

### Added

- Extended the existing planning Skill with an optional authority-grounded milestone roadmap, detailed development cards, one executable queue, and a bounded launch/resume contract.
- Added four model-strength profiles with separate reasoning effort, task-fit and escalation guidance; concrete model mappings are verified and dated when a plan needs them.
- Added 12 planning behavior cases and four discovery cases for the milestone package and adjacent workflow boundaries.

### Changed

- Kept compact planning, existing output locations, accepted authorization, and project gates; the roadmap references task IDs instead of duplicating mutable queue progress.
- Recorded the planning extension as a downstream adaptation. The updated local upstream planning Skill is unchanged from the already recorded source revision; no upstream commit state was advanced.

### Fixed

- Made architecture route actions explicitly subordinate to task authorization, including analysis-only and planning-only requests; preserved all four routes and acceptance gates.
- Removed redundant approval for verified, authorized dead-code cleanup while keeping review-only tasks read-only and uncertain deletions protected.
- Kept review findings scoped to the change instead of requiring unrelated cleanup or unrequested issue creation and assignment.
- Added five behavior regression cases for these existing 1.0.0 authorization boundaries. No trigger or output contract changed.

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
