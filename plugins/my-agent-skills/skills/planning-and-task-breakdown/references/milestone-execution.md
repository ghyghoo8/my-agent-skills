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
- Role configurations: [exact admitted model/effort per assigned role; Astra xhigh first / Sol xhigh second for implementation]
- Controller / planner / key independent reviewer: [Astra ultra; named owner and review scope]
- Other eligible execution options: [Terra ultra for explicit bounded tasks; Sol ultra for enhanced execution; Astra ultra for high uncertainty]
- Configuration evidence: [link to supported/effective settings in the execution record; unresolved availability/inheritance]
- Escalate when: [material ambiguity, cross-module failure or conflicting evidence; role-appropriate approved setting and question to resolve]
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

Delivery trustworthiness and quality come first; token usage and speed are secondary. **Terra ultra remains the minimum admitted execution baseline.** Apply the exact model/effort combinations below rather than treating effort names as a cross-model quality scale. Astra xhigh and Sol xhigh are explicitly admitted execution choices; this is not a requirement that every model use ultra, nor permission to infer other equivalents. Do not reopen the accepted baseline or introduce an economical tier.

### Core Responsibilities

Map these responsibilities to existing project owners before dispatch. They do not require five separate agents or a fixed sequence of five approvals:

| Responsibility | Ownership and deliverable | Configuration |
|---|---|---|
| Control | Maintain authority context, reconcile the single queue, coordinate dependencies/assignments, retain blockers, and integrate delivery status | Astra ultra |
| Solution and task planning | Analyze technical choices within granted scope; derive cards, interfaces, dependencies, and acceptance checks from the existing authority and roadmap | Astra ultra |
| Implementation and integration | Own scoped changes, self-tests, ordinary debugging, and the combined working result; return actual changes and unresolved issues | Astra xhigh first choice; Sol xhigh second choice; other admitted execution options below |
| Verification | Run and interpret reproducible checks, failure/recovery paths, and integration demonstrations; state what evidence proves and what remains uncovered | Astra xhigh for a separately assigned verifier; Astra ultra for complex evidence conflicts |
| Independent review | Challenge material assumptions, omissions, boundary violations, and evidence sufficiency; return findings and remaining risks separately from check results | Astra ultra in fresh context for key decisions and final delivery judgments |

Control may also perform planning. Implementers must self-test; a separate verifier is needed only when required by the project or justified by risk. Self-testing is valid evidence but is not independent verification or independent review. A checker may perform both verification and review of others' work, with separate conclusions for observed results and material omissions. Keep key review independent of the implementation or consequential decision under review; a second call without the raw inputs and actual evidence is insufficient. Do not add a review gate to each trivial substep.

The controller reconciles the canonical queue through its designated owner; workers return evidence or update only fields already assigned to them by the project's state contract. Neither additional roles nor specialist notes create another state ledger. Role names and stronger models confer no extra authority: planners may make technical decisions within granted scope, but normative scope, contract, milestone-exit, or acceptance changes follow existing project decision rules. Do not invent a universal human approval step for routine authorized choices.

Record the project's acceptance responsibility separately from agent roles. A person or an established automated mechanism may perform acceptance according to existing rules. Required Owner testing cannot be replaced by model review; acceptance alone does not authorize release or external writes.

### Optional Dedicated Responsibilities

Assign a specialist only when it resolves a concrete ownership or evidence gap:

- **Investigation:** For missing facts or conflicting documents/implementation, gather sources and unknowns, then return them to planning/control. Fact gathering does not decide normative changes.
- **Integration ownership:** When multiple implementers contribute, name one owner for the combined result. Component tests do not establish integration; if no specialist is needed, the implementation owner keeps this responsibility.
- **Diagnosis and recovery:** For recurring failures, cross-module faults, or difficult recovery, assign a bounded question and repair scope. Ordinary debugging remains with the implementer; a failure does not automatically create a new agent or external blocker.

Select the specialist's configuration by its actual work: bounded implementation/investigation can use admitted execution options, while consequential planning and key review retain Astra ultra. An integration failure holds the affected task and dependent acceptance; preserve unrelated completed evidence and continue independent authorized work.

### Admitted Model and Effort Pairs

| Exact configuration | Role-fit policy |
|---|---|
| `gpt-6-astra` + `ultra` | Control, solution/task planning, key independent review, and direct execution of high-uncertainty or consequential work |
| `gpt-6-astra` + `xhigh` | First implementation choice under established scope/contracts; separately assigned verification |
| `gpt-5.6-sol` + `xhigh` | Second implementation choice when assigning suitable work |
| `gpt-5.6-sol` + `ultra` | Retained enhanced execution option for demanding implementation/integration |
| `gpt-5.6-terra` + `ultra` | Minimum admitted executor for explicit inputs, ownership, steps, and acceptance |

This is an approved selection policy, not an empirical performance ranking or guarantee. Being in the table does not make a configuration appropriate for every role: an admitted xhigh executor cannot replace required Astra ultra control or key review. Do not start every task at Terra and wait for failure before using stronger settings. Begin consequential or high-uncertainty work with Astra ultra when warranted; carry material ambiguity, cross-module failures, and conflicting evidence into escalation rather than discarding the context. Escalation cannot create missing facts, approve contracts, or replace actual tests and acceptance.

### Configuration, Availability, and Substitution

Apply the role-appropriate admitted pairs to **all participants**, including investigation subagents, reviewers, inherited settings, retries, and fallback workers. Before dispatch, verify host support and set both model and effort explicitly when the tool allows; otherwise establish the effective inherited pair. A model name, missing effort, default, or requested setting alone does not prove the effective configuration. Record the source and date of support/configuration evidence; label observations unavailable when they cannot be established.

Availability is specific to the assigned role. A target without ultra can still run authorized Astra/Sol xhigh implementation under verified Astra ultra control and required review elsewhere, if access and handoff are sufficient. Absence of ultra on that execution target is not a blanket blocker. Conversely, supported xhigh workers do not resolve unavailable required ultra control/review; hold the affected operation or final acceptance, retaining independent authorized work and its evidence. Do not mark a task READY when its immediate required configuration is unresolved. No admitted role-appropriate executor means an execution blocker; a compliant planner may still prepare authorized documents.

**No silent substitution:** initial selection from this table, including Sol xhigh as second choice, differs from changing a selected executor during retry. Rate limits, latency, token cost, or a failed attempt do not authorize switching a selected Astra ultra task to xhigh, changing providers, or using Luna/medium/unlisted pairs. Honor explicit assignments; change them only within existing selection/fallback authorization, with the reason and new effective pair recorded, or surface the necessary decision. A preauthorized fallback must still fit the role and table. Never fabricate `ultra` for an API that exposes only `max`, equate Astra max with an admitted pair, or infer future replacements from names.

The configurations are the user's approved policy, not evergreen availability claims. Official evidence checked on 2026-09-10 includes [Codex effort and inheritance guidance](https://learn.chatgpt.com/docs/agent-configuration/subagents#choosing-models-and-reasoning), [Astra's supported API efforts](https://developers.openai.com/api/docs/models/gpt-6-astra), and [Sol xhigh in Codex Security CLI](https://learn.chatgpt.com/docs/security/cli#choose-a-model-and-reasoning-effort). These document support or specific usage, not comparative quality in this workflow. The [Terra API page](https://developers.openai.com/api/docs/models/gpt-5.6-terra) lists API settings separately from Codex ultra; verify the actual executing surface rather than translating labels.

Recommendations do not activate models, launch paid workers, or authorize implementation or external actions. When execution is authorized, use admitted pairs appropriate to the assigned roles and retain conforming explicit user choices. Subscription access does not prove unlimited capacity or delivery quality. Judge trustworthiness through authority adherence, actual verification, independent findings where required, recovery evidence, and acceptance.

## 7. Supply a Bounded Launch and Resume Contract

For sustained execution, include a short launch prompt or packet linking canonical files:

```text
Deliver [milestone/task IDs and observable endpoint] within [accepted scope].
Read [entry] -> [single queue] -> selected card -> named inputs.
Recheck actual authority revisions, exact dependencies and existing authorization.
Assign control, planning, implementation/integration, verification and key review
to named owners; combine compatible responsibilities without extra agents.
Use Astra ultra for control, planning and key independent review; choose
implementation from the admitted pairs (Astra xhigh first, Sol xhigh second;
Terra ultra minimum baseline). Keep decision, write and acceptance authority explicit.
Verify effective role settings before dispatch; no silent retry substitution.
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

1. Reconcile the queue with current authority, evidence, dependencies, worktree changes, named responsibility/decision boundaries, and the approved effective model/effort for each dispatched role.
2. Select an authorized READY task, or a mutually independent READY set for approved parallel execution; implement, diagnose ordinary failures, repair within scope, and verify. Respect bounded write ownership and actual host capacity.
3. Record actual commands, results, configuration evidence, limitations, and changed files; distinguish verification facts from review findings. Mark DONE only when integration and the project's required acceptance hold.
4. Re-evaluate eligible tasks, refine the next DRAFT card when inputs suffice, and continue within accepted scope.

On a local blocker, retain evidence, record the resolution condition and direct/transitive dependents, request necessary input early, and continue independent authorized work. A first test/tool failure is not automatically an external blocker. Missing environments may allow authorized fixture work, but fixture success cannot replace real-service acceptance. Use only an already permitted fallback; do not change source, provider, or scope to keep moving.

Do not undo completed milestones because a later gate is waiting. Reopen only work invalidated by new evidence, retaining the original result and reason. Stop at the defined endpoint or when executable work is exhausted; leave a precise resumable handoff for the latter. Do not spin on blockers, expand scope, or declare unfinished goals complete. Task and host Goal states are separate contracts.

## 8. Review Before Handoff

Check the three entry inputs, then trace authority clause -> development detail -> existing milestone outcome -> task ID -> acceptance evidence. Verify links/revisions, unique IDs, acyclic dependencies, one state owner, and sufficient detail for the next card. Identify control/planning, implementation/integration, verification, key review, and project acceptance responsibility without unnecessary agents. Check role-appropriate admitted pairs for all participants, inheritance, retries, and fallbacks. Walk through a missing prerequisite, unavailable required-role configuration, successful completion, component tests passing with integration failing, a local blocker with independent work, and an authority change. Each must give a clear next owner/action while preserving scope and acceptance.

Report artifacts, recommended first task/profile, unresolved inputs, and checks actually run. Document consistency review proves the plan is coherent; it does not prove product behavior, model performance, or release readiness.
