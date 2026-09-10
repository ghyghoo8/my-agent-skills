---
name: planning-and-task-breakdown
description: Plans tasks from accepted specs. Milestone queues require an authoritative document, a detailed development document, and an explicit milestone roadmap. Skip obvious edits and already executable plans.
---

# Planning and Task Breakdown

Turn accepted requirements into verifiable outcomes, exact dependencies, and a clear next executable task. Keep the plan subordinate to project authority and proportional to the work.

## Choose the Planning Depth

- **Compact plan:** For a bounded feature needing decomposition, use a short plan and the task list target below. Several changed files do not require a document hierarchy.
- **Milestone execution package:** For delivery against a milestone roadmap, sustained execution, or multi-session handoff, first verify all three entry prerequisites below. Then read [Milestone Execution](references/milestone-execution.md) to derive task cards, the executable queue, and model-strength options from those documents. Detail near-term tasks; keep distant milestones coarse until their inputs stabilize.
- **Already executable:** Reuse an adequate plan and queue. Do not replan before authorized implementation, a status query, or an obvious local edit unless new evidence invalidates the relevant plan.

When core outcomes or requirements are unresolved, use `spec-driven-development` for that uncertainty; do not invent requirements in task cards. `incremental-implementation` owns execution of approved slices. `documentation-and-adrs` records normative decisions; a delivery plan links accepted decisions rather than making new architecture policy. These are scoped handoffs, not a mandatory Skill sequence.

## Milestone Workflow Entry Prerequisites

Enter the milestone execution workflow only when all three already exist and are usable for the selected scope:

1. **An authoritative document:** The project identifies the current normative document, its applicable scope, and precedence.
2. **At least one detailed development document:** In addition to the authority, a document explains relevant implementation responsibilities, flows or interfaces, and verification for the selected scope. A title, outline, high-level README, command list, or bare TODO list does not qualify.
3. **An explicit milestone roadmap:** Identifiable milestones have observable outcomes, dependency/order information, and exit or acceptance conditions. A vague sequence such as “foundation -> features -> polish” does not qualify.

Record paths and relevant sections for all three, and check consistency with authority. These are three content requirements, not a demand for three new files; a clearly identified roadmap section may live in an existing development document.

If an input is missing, insufficient, or materially conflicting, stay in prerequisite preparation: identify the exact gap and complete or repair the source documents within existing documentation authorization before rechecking entry. Resolve missing requirements through the appropriate specification/decision workflow. Do not derive an executable queue first, count its generated cards as the missing input, or bypass this entry condition by calling the same requested milestone work a compact plan. Existing valid documents do not require ritual re-approval. Once the prerequisites are met, continue within the user's scope; entry itself does not authorize implementation.

For this milestone workflow, prioritize delivery quality and trustworthiness over token usage and speed. Assign five core responsibilities: control, solution/task planning, implementation/integration, verification, and independent review. These are responsibilities, not five mandatory agents; add dedicated investigation, integration, or recovery ownership only when needed. **Terra ultra remains the minimum admitted execution baseline; Astra ultra owns control, planning, and key independent review.** Prefer Astra xhigh for implementation, with Sol xhigh as the second choice; retain Sol ultra for enhanced execution and Astra ultra for high uncertainty. Read the reference's [role and model policy](references/milestone-execution.md#6-assign-roles-and-apply-the-quality-first-model-policy) for role boundaries, verification, exact admitted pairs, and configuration checks. Apply it to all participants and retries; do not equate effort labels across models, introduce an economical tier, or silently substitute a selected configuration. Recommendations do not themselves switch the active model or grant decision authority.

## Establish Authority and Scope

Start with read-only evidence gathering: project instructions, designated specification, development guide, current plan/task target, and relevant code, types, tests, and commands.

- Identify the designated primary authority, its actual revision/status, and governing sections. Record which subordinate docs it accepts and what each governs. Follow existing project precedence rather than imposing a new hierarchy.
- Bind derived tasks to that authority and minimum section references. A newer plan, status note, chat, or backup does not supersede the specification. Expected versions in the queue detect drift; they never select the authoritative version.
- If authority is absent, contradictory, or materially out of date, expose the exact gap and affected tasks. For milestone work, remain in prerequisite preparation until the entry conditions hold; independent document repair may continue within scope. For compact planning, keep independent plan sections explicit about assumptions. Do not rewrite normative requirements to fit the roadmap.
- Distinguish requested outcomes, accepted scope, observed implementation, unverified claims, and deferred capabilities. Design acceptance is not runtime or release evidence.

For planning-only requests, write the requested planning artifacts and keep business implementation unchanged. For planning within authorized implementation, continue after preparation without re-asking for the same scope. Preserve `ARCHITECTURE_GATE` and `DISCOVERY` write boundaries and exit conditions. Planning does not switch the host's collaboration mode, create a Goal or automation, launch another task, change models, or authorize external writes.

## Decompose and Order

1. Name observable outcomes and the first useful end-to-end slice. Build only its required foundations, not every database table, then every API, then every screen.
2. Map exact task dependencies and the integration evidence each consumer needs. Put a bounded experiment early when it resolves a material unknown; give it a decision-changing exit condition.
3. Size tasks by independently verifiable results, uncertainty, and recovery impact. File counts, lines, fixed hours, and session boundaries are not splitting rules. Keep coherent mechanical changes together.
4. Add checkpoints at meaningful integration, acceptance, or risk boundaries. Use project-required checks plus the smallest checks that establish affected behavior.
5. Identify the next executable task and why its prerequisites are satisfied; otherwise record the missing input and independent work that remains possible.

Parallelize bounded independent work only when delegation is available and authorized. Fix shared contracts first, assign non-overlapping write ownership, and keep dependent operations and final reconciliation sequential. Parallel branches in a graph do not authorize concurrent dispatch or external actions.

## Compact Task Contract

Keep each definition in one place: the task list target or a linked task card. Populate applicable details:

```markdown
## T1: [Observable result]

- Authority and input: [spec revision/sections; relevant guide/code/tests]
- Scope: [included behavior; exclusions; likely files/interfaces]
- Dependencies: [exact task IDs and required evidence, or none]
- Implementation: [concrete ordered steps following existing project patterns]
- Acceptance: [testable outcome, including relevant failure paths]
- Verification: [repository commands and working directory; required manual checks]
- Evidence and recovery: [deliverables, evidence location, rollback/stop condition if applicable]
- Open inputs: [unresolved fact/decision, affected work and resolution owner, or none]
```

The queue owns mutable task status. Cards contain specifications, not another set of live progress fields. Acceptance checklists express criteria; actual results belong in the queue's evidence entry. Do not mark checks as passed while planning them.

## Output Files and Task List Target

Use project-designated locations and existing task IDs. Otherwise:

- **Canonical plan:** `.codex/agent-state/plan.md`, holding scope, authority links, outcome/dependency order, risks, and a link to the task list target.
- **Task list target:** `.codex/agent-state/todo.md`, holding ordered tasks/checkpoints and their progress. This is the default queue/status authority for this task. The plan uses links or task IDs rather than copying live checkboxes.

Create parent directories only when durable artifacts are useful. Compact plans can use inline task definitions in the queue; milestone packages may use linked development cards as described in the reference.

**Preserve incomplete plans.** Inspect targets before writing. Revise the same work in place within the user's request. Preserve other tasks' incomplete files and tracker items; use a permitted task-scoped location under the project state directory when available. Ask only if a mandatory fixed target conflicts and no permitted separate location exists. Do not delete, rename, overwrite, or bulk-close unrelated work to make room.

**External tracker:** If designated and authorized by the user or project rules, it replaces the Markdown queue. Map tasks, acceptance, dependencies, checkpoints, evidence, and status into its fields. Keep an ordered link/ID index in the plan without a second checklist. A tracker example or planning request alone does not authorize external item creation or messages.

## Review the Plan

- For milestone work, all three entry documents/content roles are identified, sufficient for the selected scope, and consistent before queue derivation.
- Authority links, expected revisions, source obligations, and existing acceptance are consistent.
- Each near-term executable task has an observable outcome, sufficient inputs, exact dependencies, scoped steps, and applicable verification commands.
- Dependencies are acyclic and resolvable. Optional enhancements are not hidden prerequisites for the accepted baseline.
- One mutable queue/status target and a concrete next action exist; unrelated work is preserved.
- Integration, human acceptance, and release evidence remain distinct from implementation and automated checks.
- Planning depth fits the request; no unnecessary hierarchy, full-suite gate, or repeated approval was added.
- Milestone cards identify responsibility, permitted decisions, integration ownership, verification/review evidence, and the project's acceptance responsibility without creating mandatory extra agents or approval steps.
- Milestone model options preserve the named Terra ultra baseline and role-appropriate admitted pairs, including approved Astra/Sol xhigh execution. Required Astra ultra control and key review remain distinct. Subagents and retries cannot silently substitute configurations; unsupported or unverified role settings block only affected work.

Acceptance criteria describe each task's outcome and supplement applicable project-wide completion rules. See [Definition of Done](../../references/definition-of-done.md).
