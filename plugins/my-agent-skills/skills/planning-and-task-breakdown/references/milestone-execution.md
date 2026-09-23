# Milestones and an Executable Task Queue

Use this reference to turn an existing milestone roadmap into a development execution package another session can execute from minimal context. Entry requires an authoritative document, at least one detailed development document, and an explicit milestone roadmap. Reuse project names, IDs, authority, and state vocabulary; the layout below is an example, not a required framework.

## 0. Verify the Three Inputs Before Entry

Read and identify the actual documents and sections; their names alone are not proof:

| Required input | Minimum useful content |
|---|---|
| Current authoritative document | Project-designated normative scope, constraints, and precedence |
| At least one detailed development document | Implementation responsibilities and relevant flows/interfaces, plus verification approach for the selected scope; not merely an outline, README introduction, commands, or TODOs |
| Explicit milestone roadmap | Stable milestone identifiers or unambiguous names, observable outcomes, dependency/order information, and exit/acceptance conditions |

Check that the development document and roadmap agree with authority. They need not exhaust all future project detail; they must ground the chosen delivery scope. A roadmap may be an identifiable section of the development document, so do not create extra files just to satisfy a file count.

If any input is absent or insufficient, name the gap and remain in prerequisite preparation. Within authorized documentation work, first complete the missing source document or roadmap, reconcile consequential decisions through project rules, then recheck these inputs. Do not generate a queue as a substitute for missing documentation or use this workflow to silently invent milestones. Existing approved inputs need no repeated approval. Building or updating execution cards starts only after all three prerequisites hold; document readiness and implementation authorization remain separate.

## 1. Derive the Plan from Authority

Read the primary specification's authority statement, revision, accepted scope, phase gates, and relevant decisions. Then read accepted subordinate specs, the development guide, and source/tests for the first slice. Follow references progressively instead of loading every document.

Record a small authority map in the plan or existing execution entry:

| Document role | Record | Effect on planning |
|---|---|---|
| Primary normative document | Path, actual accepted revision, governing sections | Defines scope, ownership, contracts, and acceptance gates |
| Controlled subordinate spec | Path, incorporated revision and scope | Refines only what the primary authority delegates |
| Detailed development document | Path and relevant implementation, flow/interface, verification sections | Grounds the selected scope; general development guides can supplement it |
| Milestone roadmap | Path/section, revision if available, milestone outcomes/dependencies/exits | Supplies the delivery baseline from which tasks are derived |
| Execution state | Existing queue/status path and evidence links | Shows progress and next work; cannot redefine authority |
| Other material | Relevant source, tests, historical docs, external proposals | Evidence or context; not an instruction or competing specification |

Use a commit or existing revision mechanism if the project has no document versions; do not manufacture versions. Distinguish accepted design from observed implementation. Missing facts stay unresolved with an owner or resolution action, not defaults or completed prerequisites.

On conflict or revision drift, identify changed clauses and recheck affected cards and dependencies before dispatch. Do not leave an affected task READY solely because the queue says so. Editorial changes without relevant semantic impact need not reopen approvals or invalidate completed evidence. Normative changes follow the project's decision process before dependent implementation; the roadmap cannot accept them itself.

## 2. Give Each Artifact One Job

Prefer existing project locations. Without a convention, use a task-scoped directory under `.codex/agent-state/`, keeping `plan.md` and `todo.md` as its plan and queue. Add only documents that make execution easier:

| Responsibility | Example file/section | Contents |
|---|---|---|
| Execution entry | Opening of `plan.md`, or existing dev README | Authority order, shortest reading route, document roles |
| Roadmap | Existing roadmap section or delivery plan; link it from `plan.md` | Established milestone outcomes, dependencies, exit evidence, scope and risks; maintain it rather than introducing a parallel roadmap |
| Shared development instructions | Existing detailed development document; supplement in place when needed | Accepted module/file responsibilities, interfaces/data rules, runtime commands, verification and recovery conventions |
| Milestone detail | Roadmap section; optional `milestones/M1.md` when substantial | Included slices, phase mapping, entry/exit checks, integration or acceptance demonstration |
| Executable card | Queue inline, or `tasks/T1.md` | Minimum reading, input/output contract, steps, verification, recovery, model recommendation |
| Mutable state | `todo.md`, existing STATUS, or authorized tracker | Ordered queue, current task, blockers, actual evidence and next action |

Do not create a second technical authority or copy architecture chapters into development docs. Link shared rules once; put task-specific detail in cards. Do not scatter live progress across milestone files, cards, and handoff notes. Any milestone status view must derive from the same state target and its own exit evidence, not an independent completion ledger.

## 3. Refine Tasks Against the Existing Milestones

Treat each milestone as a delivery acceptance node: define the deliverables,
observable criteria, dependency evidence and responsible acceptance mechanism.
Preparation stages are not milestones unless their documents are agreed
deliverables. A Goal may span several milestones; task completion alone does
not establish a node's acceptance or the Goal's completion.

Read the existing roadmap and preserve its milestone identities, outcomes, and gates. Start task refinement at its first relevant demonstrable value. Respect supplied dates and capacity; otherwise order by dependencies and evidence without inventing calendar commitments. Product maturity phases and delivery milestones differ: map between them without renaming or weakening product gates.

For an existing milestone mapping, preserve equivalent project fields or use this view; task IDs are added as decomposition proceeds:

| ID / outcome | Product-phase mapping | Scope and exclusions | Exact entry dependencies | Task IDs | Exit evidence / next entry |
|---|---|---|---|---|---|
| M1: [first useful end-to-end result] | [existing phase, if any] | [accepted slice] | [required contracts, tasks and acceptance] | [stable IDs/links] | [observable demonstration, failure/recovery checks and applicable approval] |

Milestones must close with evidence, not activities such as “finish backend.” If that baseline is missing, return to prerequisite preparation to clarify the roadmap before deriving tasks. A later material change may require an in-place roadmap revision under project authority; do not silently add a readiness milestone or change exits in a task card. Do not place every future infrastructure component ahead of the first value slice.

Milestone numbers are labels, not blanket barriers: independent authorized tasks can proceed once their exact prerequisites are met. If a project permits a limited branch, name its allowed tasks, retained gates, exclusions, and route back to the full path. Do not invent a reduced path as a fallback. Local task completion does not imply a whole phase, live integration, optional capability, or release is complete.

Detail near-term tasks with stable inputs. Leave later milestones with outcome, dependency, risk, and activation conditions until their contracts are ready. Do not pre-generate empty modules, speculative interfaces, or dozens of distant cards.

## 4. Make Ready Cards Executable

Populate this structure for the upcoming queue using actual paths and evidence. A task should be actionable without reconstructing prior conversation:

```markdown
# [Task ID]: [Observable result]

## Context and entry
- Milestone / accepted scope: [ID, result and exclusions]
- Authority: [actual revision, precise sections/decisions]
- Minimum reading: [entry -> queue -> card -> relevant guide/spec/source/tests]
- Dependencies and inputs: [exact IDs, required evidence, fixtures/contracts]
- Unresolved inputs: [fact/decision, owner or resolution action, affected work]

## Implementation contract
- Allowed change surface: [modules/files/interfaces; ownership boundary]
- Inputs and outputs: [accepted fields, semantics, errors and constraints]
- Steps: [ordered concrete changes using an existing local pattern]
- Required edge paths: [applicable empty/error/conflict/retry/recovery behavior]
- Deliverables: [code/docs/test/evidence paths; label proposed new paths]

## Responsibilities and authority
- Control / planning owner: [existing owner; scope of permitted technical decisions]
- Implementation / integration owner: [who delivers the combined result; assigned write scope]
- Verification: [who runs which checks; self-test versus required independent verification]
- Independent review: [owner/context and material questions; project-required or risk-based scope]
- Acceptance: [existing responsible person or mechanism and required evidence; release authority if relevant]
- Optional specialist: [specific unknown, integration boundary or recovery problem; omit when unnecessary]

## Acceptance and verification
- Outcome: [observable pass/fail conditions]
- Commands: [verified runtime, working directory, focused and required checks]
- Integration/manual evidence: [what fixture/static tests cannot establish]
- Evidence destination: [single queue entry or linked artifact; separate verification facts and review findings]
- Stop/recovery: [material boundary or missing input; rollback/disable if applicable]

## Execution recommendation
- Role configurations: [GPT-6 Sol ultra by default for the controller; controller-selected worker model/effort with quality and risk rationale]
- Bounded worker: [GPT-6 Luna only when low risk, clear inputs and reliable outcome checks justify it; otherwise use Sol]
- Astra allowance: [link to the delivery scope's single allowance record; never a separate allowance per card]
- Configuration evidence: [link to supported/effective settings in the execution record; unresolved availability/inheritance]
- Escalate when: [actual Sol attempt, unresolved reasoning problem, evidence and one bounded question; missing facts/authority/environment have their own resolution path]
- Selection boundary: [initial selection rationale; existing explicit assignment and permitted fallback, if any]
- Handoff: [required output, review responsibility and exact next action]
```

Avoid “implement module and add tests.” State the input, owning module/interface, behavior, and checks. Verify commands against project configuration; otherwise label them unavailable and give a bounded resolution task. Proposed file paths are allowed but must not appear to be existing files. Do not invent contracts.

Choose applicable fields by risk. Reversible docs do not need a migration checklist. Production transitions still follow the project's migration/release workflow. Preserve outcome-based testing without manufacturing tests for low-impact edits or requiring a full suite per task.

Reuse existing assignments and role names. One person or agent may hold compatible responsibilities; do not create agents or empty sections merely to fill the template. Cards record responsibility and required settings; actual configuration observations, verification results, and review outcomes belong in the canonical execution record.

## 5. Keep One Executable Queue

Keep stable task IDs across revision and handoff. Record mutable task status only in the designated queue/tracker:

| Order | Task / milestone | State | Exact prerequisites or blocker | Evidence / next action |
|---|---|---|---|---|
| [priority] | [card link / milestone ID] | [project state] | [IDs, inputs or acceptance] | [actual result link; next step] |

Use existing project states. If none exist, these meanings suffice:

- **DRAFT:** Dependencies, scope, inputs, or card detail are incomplete.
- **READY:** Exact dependencies and inputs are satisfied, authority matches, and execution is authorized for this scope.
- **IN_PROGRESS:** Actively owned execution within the allowed scope.
- **BLOCKED:** A named condition prevents required progress or acceptance; record evidence, affected dependents, and the condition for unblocking.
- **DONE:** Acceptance criteria and required verification/acceptance evidence are satisfied.
- **SUPERSEDED:** Replaced with an explicit pointer; retained for traceability when needed.

A planning-only request may produce complete execution specifications without dispatch authorization: record the pending implementation authorization explicitly and do not mark them READY. Readiness is not inferred from document existence. Code plus unit tests cannot close a task that requires missing real integration or human acceptance.

For a manual readiness check or a completed current-task handoff, use
[Execution Readiness Choice](execution-readiness-choice.md) to assess the whole
delegated scope before offering sustained execution. Three documents permit
queue planning; a READY first task does not prove the whole delivery path is
feasible. Explicit check/planning-only scope suppresses the offer; already
authorized execution continues within its scope. Keep READY's authorization
requirement unchanged.

Use one controller and one canonical queue. For authorized parallel module work,
dispatch independent READY tasks to distinct subagents under the
[parallel execution contract](../../../references/orchestration-patterns.md#parallel-module-execution).
Respect project concurrency limits and observed host capacity. Each active task
has one owner; an existing `current_task` can remain a navigation focus without
becoming a global serial lock. Do not create a second active-task ledger.
Coupled changes to shared contracts, migrations, generated output or release
activation retain one writer or run serially.

## 6. Assign Roles and Apply the Quality-First Model Policy

**Delivery quality is the first priority. The single controller defaults to GPT-6 Sol ultra and decides each subagent's model and reasoning effort.** Sol is the normal model ceiling; Luna is a bounded worker option, and Astra is a single-consultation exception. Reduce cost through appropriate delegation, focused context and avoiding duplicate work, without trading away trustworthy acceptance. This replaces the former Terra floor and mandatory Astra roles; model names and effort labels are not measured quality rankings.

### Core Responsibilities

Map these responsibilities to existing project owners before dispatch. They do not require five separate agents or a fixed sequence of five approvals:

| Responsibility | Ownership and deliverable | Configuration |
|---|---|---|
| Control | Maintain authority context, reconcile the single queue, coordinate dependencies/assignments, retain blockers, and integrate delivery status | Sol ultra |
| Solution and task planning | Derive cards, interfaces, dependencies, and acceptance checks within granted scope | Sol at controller-selected effort; control may combine planning at ultra |
| Implementation and integration | Own scoped changes, self-tests, ordinary debugging, and the combined working result | Sol at effort suited to the task; eligible Luna work below |
| Verification | Run and interpret reproducible checks and recovery/integration evidence | Controller-selected setting; Luna may run a bounded deterministic check |
| Independent review | Challenge material assumptions, boundaries, omissions and evidence sufficiency | Separate fresh-context Sol for key/final review, at effort the controller judges sufficient |

Control may also perform planning at its assigned ultra setting; a separate planner uses the planning row. Implementers must self-test; a separate verifier is needed only when required by the project or justified by risk. Self-testing is valid evidence but is not independent verification or independent review. A checker may perform both verification and review of others' work, with separate conclusions for observed results and material omissions. Keep key review independent of the implementation or consequential decision under review; a second call without the raw inputs and actual evidence is insufficient. Do not add a review gate to each trivial substep.

The controller reconciles the canonical queue through its designated owner; workers return evidence or update only fields already assigned to them by the project's state contract. Neither additional roles nor specialist notes create another state ledger. Role names and stronger models confer no extra authority: planners may make technical decisions within granted scope, but normative scope, contract, milestone-exit, or acceptance changes follow existing project decision rules. Do not invent a universal human approval step for routine authorized choices.

Record the project's acceptance responsibility separately from agent roles. A person or an established automated mechanism may perform acceptance according to existing rules. Required Owner testing cannot be replaced by model review; acceptance alone does not authorize release or external writes.

### Optional Dedicated Responsibilities

Assign a specialist only when it resolves a concrete ownership or evidence gap:

- **Investigation:** For missing facts or conflicting documents/implementation, gather sources and unknowns, then return them to planning/control. Fact gathering does not decide normative changes.
- **Integration ownership:** When multiple implementers contribute, name one owner for the combined result. Component tests do not establish integration; if no specialist is needed, the implementation owner keeps this responsibility.
- **Diagnosis and recovery:** For recurring failures, cross-module faults, or difficult recovery, assign a bounded question and repair scope. Ordinary debugging remains with the implementer; a failure does not automatically create a new agent or external blocker.

Select a specialist's configuration by its actual work, using the same policy below. An integration failure holds the affected task and dependent acceptance; preserve unrelated completed evidence and continue independent authorized work.

### Controller-Selected Worker Settings

| Model / setting | Selection guidance |
|---|---|
| `gpt-6-sol` + `ultra` | Default controller, including planning it performs itself |
| `gpt-6-sol` workers | Choose a host-supported effort for complexity, uncertainty, failure impact and required evidence. Medium may fit routine work; high or xhigh may fit difficult work/review; max or ultra may be justified for demanding work. These are references, not a fixed role whitelist or required ladder. |
| `gpt-6-luna` workers | Only low-risk work with complete inputs and reliable independent checks. High is a starting reference; the controller chooses supported effort for the actual task. Luna has no Ultra support. |
| `gpt-6-astra` consultant | Only the bounded consultation below; select a supported single-agent effort for the question, without Ultra or subdelegation |

Luna fits bounded extraction, mechanical edits, fixture work and isolated checks when those conditions hold. It does not own control, consequential planning, cross-module integration decisions or key/final independent review. If quality or verifiability is uncertain, choose Sol directly; no task must try Luna or a lower effort first. Do not routinely have Sol redo a valid Luna result. Verify the outcome proportionately and promote a struggling Luna task to Sol with its evidence rather than repeating blind attempts.

Ultra can create subagents and is not merely deeper single-agent reasoning. The controller may select it for a suitable demanding worker, but should make the choice explicitly rather than blindly propagate its own setting to every worker. Use bounded ownership and observed capacity; do not create a second fan-out over already assigned tasks or extra workers for serial work. If a full-history fork cannot override settings, pass minimum task context through an override-capable path or establish that inherited settings are appropriate. Record selection reasons in the existing task assignment, not a new scoring system. A speed setting is separate from reasoning quality. Shared effort names never prove cross-model equivalence.

### One Astra Consultation per Delivery Scope

Use Astra only after a substantive Sol attempt leaves a material reasoning or solution impasse. First inspect the actual failure and distinguish missing facts, unavailable permissions, environment faults and rate limits; those need their own resolution, not a stronger model. Try a concrete repair or justified Sol effort increase when it has a plausible benefit; do not exhaust an effort ladder or repeat unchanged attempts to manufacture eligibility.

The user's accepted conditional allowance authorizes **one bounded read-only consultation for the entire authorized delivery scope**, including all its milestones, workers and resumptions. It is not one per error, card, agent or session. A matching Goal shares this scope; creating, resuming or replacing a Goal does not replenish it. If allowance or execution authority was never granted, a recommendation does not grant either. Reuse valid authorization without asking again when its conditions hold.

The controller owns the allowance in the existing canonical queue: scope, grant/source, not-granted/unused/reserved/used/uncertain status, Sol evidence, question, consultation identity and result link. Reconcile existing authorization and any prior use before recording an unused allowance; an absent record is not a fresh grant. Reserve it before dispatch so parallel workers cannot each spend it. Pass only the contract, relevant artifacts, failed approach/checks and one question with a finite deliverable. Give Astra no implementation writes, subdelegation, Goal control or follow-up assignment; one agent turn may inspect bounded evidence and returns advice to Sol. No automatic second turn, re-dispatch or retry. An uncertain launch counts as unavailable until its receipt is reconciled; only proof that it never started permits releasing the reservation. Context compaction and handoff preserve this record.

Sol evaluates the advice against actual code and checks, implements within existing authority, and retains required independent review and acceptance. Astra output is not completion evidence. If unresolved, preserve the blocker and continue independent work; additional Astra use requires a new explicit allowance. Never consume the exception just because a task is important or to add a ceremonial final review.

### Configuration, Availability, and Substitution

Apply the policy to all participants, including nested workers, reviewers, inherited settings and retries. Pass the controller's model ceiling, quality priority and shared Astra allowance to workers; worker-created subagents remain within those assignments. Before dispatch, verify current host support and explicitly request model and effort when supported. Inspect the actual inherited settings when an override is unavailable. Keep supported, requested and observed effective settings distinct; an echoed request or model self-report is not a runtime receipt. With supported explicit selection, authorized work can start, recording effective settings as unverified if the host cannot expose them; do not claim verified model compliance. If the host cannot enforce the required selection, or the project requires an effective receipt before execution, hold that affected dispatch.

Model availability is local to the role. Missing Astra or Ultra on a worker host does not block its ordinary Sol/Luna work under supported Sol ultra control elsewhere. Missing the required Sol ultra controller or suitable review holds only affected work or acceptance; a lower-effort controller or Luna worker cannot silently fill those roles. Preserve authorized preparation and independent work. If the current main task uses a different model or effort, disclose that the Skill cannot switch it; use an exposed authorized host control or a user-selected model for execution instead of pretending a switch occurred. Do not create another user-owned task or edit global configuration to work around this.

For assignments made under this policy, the controller may reassign role-appropriate Sol/Luna settings within the same provider and scope as evidence changes, keeping quality first and recording the reason and new selection. Preserve a user's explicitly locked model/effort or narrower fallback limit unless the user changes it. Do not silently substitute legacy models, providers or endpoints, reinterpret effort labels, or use rate limits to justify Astra. Changing this default does not silently relabel past receipts or override separately locked assignments; reconcile conflicts before the affected dispatch.

Official [model guidance](https://learn.chatgpt.com/docs/models) and [credit rates](https://learn.chatgpt.com/docs/pricing#token-rates), checked 2026-09-23, inform this cost-aware policy; actual availability remains host-specific. They do not establish task-specific quality or savings. Track already available usage, elapsed time, rework and acceptance evidence when comparing outcomes; do not add telemetry or benchmark every task.

Recommendations do not activate models, launch paid workers, or authorize implementation or external actions. When execution is authorized, use controller-selected role-appropriate settings and retain explicit user choices. Subscription access does not prove unlimited capacity or delivery quality. Judge trustworthiness through authority adherence, actual verification, independent findings where required, recovery evidence, and acceptance.

## 7. Supply a Bounded Launch and Resume Contract

For sustained execution, include a short launch prompt or packet linking canonical files:

```text
Deliver [milestone/task IDs and observable endpoint] within [accepted scope].
Read [entry] -> [single queue] -> selected card -> named inputs.
Recheck actual authority revisions, exact dependencies and existing authorization.
Assign control, planning, implementation/integration, verification and key review
to named owners; combine compatible responsibilities without extra agents.
Default the single controller to GPT-6 Sol ultra; let it explicitly select worker
models/efforts with delivery quality first and Luna only for eligible bounded work.
Carry the one shared Astra allowance in [state target] across workers/resumptions;
use it only for one bounded consultation after an evidenced Sol impasse.
Keep decision, write and acceptance authority explicit. Verify host selection
support, record requested/observed settings and respect explicit model locks.
Execute the next authorized READY task, verify it, record evidence in [state target],
then continue to the next eligible task until the endpoint or no executable work.
Retain blockers and completed evidence; request only materially blocking inputs.
Respect [named decision/release boundaries]; return [evidence and next action].
```

This packet does not create a host Goal, automation, monitor, or new task. Use those facilities only when explicitly requested and follow their tool/state rules. In authorized execution, task boundaries and context handoffs do not create new approval requirements.

For explicitly authorized Goal execution, apply the readiness reference's
[Goal startup and resume contract](execution-handoff.md#2-start-or-resume-the-authorized-goal)
before dispatch. Reuse a matching unfinished Goal; do not replace a conflicting
one or infer Goal authorization from a planning request. The Goal describes the
delegated acceptance endpoint; the queue remains the business progress authority.

Preserve this execution loop:

1. Reconcile the queue with current authority, evidence, dependencies, worktree changes, named responsibility/decision boundaries, approved requested model/effort, host selection support and observed effective status for each dispatched role.
2. Select an authorized READY task, or a mutually independent READY set for approved parallel execution; implement, diagnose ordinary failures, repair within scope, and verify. Respect bounded write ownership and actual host capacity.
3. Record actual commands, results, configuration evidence, limitations, and changed files; distinguish verification facts from review findings. Mark DONE only when integration and the project's required acceptance hold.
4. Re-evaluate eligible tasks, refine the next DRAFT card when inputs suffice, and continue within accepted scope.

On a local blocker, retain evidence, record the resolution condition and direct/transitive dependents, request necessary input early, and continue independent authorized work. A first test/tool failure is not automatically an external blocker. Missing environments may allow authorized fixture work, but fixture success cannot replace real-service acceptance. Use only an already permitted fallback; do not change source, provider, or scope to keep moving.

Do not undo completed milestones because a later gate is waiting. Reopen only work invalidated by new evidence, retaining the original result and reason. Stop at the defined endpoint or when executable work is exhausted; leave a precise resumable handoff for the latter. Do not spin on blockers, expand scope, or declare unfinished goals complete. Task and host Goal states are separate contracts.

## 8. Review Before Handoff

Check the three entry inputs, then trace authority clause -> development detail -> existing milestone outcome -> task ID -> acceptance evidence. Verify links/revisions, unique IDs, acyclic dependencies, one state owner, and sufficient detail for the next card. Identify control/planning, implementation/integration, verification, key review, and project acceptance responsibility without unnecessary agents. Check controller-selected role-appropriate settings and the shared Astra allowance for all participants, inheritance, retries, and fallbacks. Walk through a missing prerequisite, unavailable required-role configuration, successful completion, component tests passing with integration failing, a local blocker with independent work, and an authority change. Each must give a clear next owner/action while preserving scope and acceptance.

Report artifacts, recommended first task/profile, unresolved inputs, and checks actually run. Document consistency review proves the plan is coherent; it does not prove product behavior, model performance, or release readiness.
