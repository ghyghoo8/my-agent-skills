---
name: planning-and-task-breakdown
description: Plans accepted specs into tasks and checks substantial development handoffs for autonomous execution. Milestones require authority, development docs, and a roadmap. Skip local edits and routine authorized execution.
---

# Planning and Task Breakdown

Turn accepted requirements into verifiable outcomes, exact dependencies, and a clear next executable task. Keep the plan subordinate to project authority and proportional to the work.

## Choose the Planning Depth

- **Compact plan:** For a bounded feature needing decomposition, use a short plan and the task list target below. Several changed files do not require a document hierarchy.
- **Milestone execution package:** For delivery against a milestone roadmap, read [Milestone Execution](references/milestone-execution.md) and verify its three entry inputs before deriving the package. Use it to derive task cards, the executable queue, and model-strength options from those documents. Detail near-term tasks; keep distant milestones coarse until their inputs stabilize. Sustained execution or a multi-session handoff alone does not require a milestone structure.
- **Already executable:** Reuse a valid plan and queue; do not replan for authorized work, status or local edits. Ordinary authorized execution goes to `incremental-implementation` without loading readiness, handoff or milestone references. Only new material evidence triggers affected reassessment.
- **Execution readiness:** For a requested readiness check or a completed development handoff for a substantial module, refactor, or milestone, read [Execution Readiness](references/execution-readiness-choice.md), following its execution handoff reference only when the assessment passes and execution is in scope. Assess the entire delegated scope for sustained execution with reduced human decision-making; a runnable first task is insufficient. This owner handles manual/automatic entry, a scoped native choice, and explicitly authorized Goal startup. Routine authorized execution continues without another offer.

When core outcomes or requirements are unresolved, use `spec-driven-development` for that uncertainty; do not invent requirements in task cards. `incremental-implementation` owns execution of approved slices. `documentation-and-adrs` records normative decisions; a delivery plan links accepted decisions rather than making new architecture policy. These are scoped handoffs, not a mandatory Skill sequence.

## Milestone-Specific Rules

Only requested milestone work loads [Milestone Execution](references/milestone-execution.md).
It requires current authority, a substantive development document and an explicit
roadmap before queue derivation; their content matters, not file count. Missing
inputs stay in authorized preparation. Do not bypass this requirement by calling
the same milestone work a compact plan; valid inputs need no ritual re-approval.

That reference owns the five core responsibilities and model policy: GPT-6 Sol
ultra controls delivery and selects subagent models/efforts with quality first;
GPT-6 Luna is limited to low-risk, checkable work. Astra is
limited to one scoped consultation after an evidenced Sol impasse, shared across
the entire authorized delivery scope. Read the full policy before assigning a
milestone participant or retry. Preserve acceptance quality; recommendations
never activate models or authorize work. General module/refactor handoffs do not
inherit these milestone-only requirements.

## Establish Authority and Scope

Start with read-only evidence gathering: project instructions, designated specification, development guide, current plan/task target, and relevant code, types, tests, and commands.

- Identify the designated primary authority, its actual revision/status, and governing sections. Record which subordinate docs it accepts and what each governs. Follow existing project precedence rather than imposing a new hierarchy.
- Bind derived tasks to that authority and minimum section references. A newer plan, status note, chat, or backup does not supersede the specification. Expected versions in the queue detect drift; they never select the authoritative version.
- If authority is absent, contradictory, or materially out of date, expose the exact gap and affected tasks. For milestone work, remain in prerequisite preparation until the entry conditions hold; independent document repair may continue within scope. For compact planning, keep independent plan sections explicit about assumptions. Do not rewrite normative requirements to fit the roadmap.
- Distinguish requested outcomes, accepted scope, observed implementation, unverified claims, and deferred capabilities. Design acceptance is not runtime or release evidence.

For planning-only requests, write the requested planning artifacts and keep business implementation unchanged. For planning within authorized implementation, continue after preparation without re-asking for the same scope. Preserve `ARCHITECTURE_GATE` and `DISCOVERY` write boundaries and exit conditions. Planning does not switch the host's collaboration mode, create a Goal or automation, launch another task, change models, or authorize external writes.

Document prerequisites permit milestone queue planning; sustained execution has
the separate whole-scope readiness check above. General module/refactor handoffs
use their accepted requirements, plan, and executable development documentation
without inheriting milestone-only roadmap or model requirements. Do not relabel
an explicitly requested milestone workflow to bypass its prerequisites.

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

- For milestone work, the three required input content roles are identified, sufficient for the selected scope, and consistent before queue derivation.
- Authority links, expected revisions, source obligations, and existing acceptance are consistent.
- Each near-term executable task has an observable outcome, sufficient inputs, exact dependencies, scoped steps, and applicable verification commands.
- Dependencies are acyclic and resolvable. Optional enhancements are not hidden prerequisites for the accepted baseline.
- One mutable queue/status target and a concrete next action exist; unrelated work is preserved.
- Integration, human acceptance, and release evidence remain distinct from implementation and automated checks.
- Planning depth fits the request; no unnecessary hierarchy, full-suite gate, or repeated approval was added.
- Milestone cards identify responsibility, permitted decisions, integration ownership, verification/review evidence, and the project's acceptance responsibility without creating mandatory extra agents or approval steps.
- Milestone assignments use role-appropriate Sol/Luna settings and carry the shared Astra allowance across workers and resumptions. Model changes respect explicit user locks; support, requested settings and observed effective settings remain distinct. Missing required capabilities block only affected work.

Acceptance criteria describe each task's outcome and supplement applicable project-wide completion rules. See [Definition of Done](../../references/definition-of-done.md).
