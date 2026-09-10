# Execution Handoff and Goal Lifecycle

Read after the [whole-scope readiness assessment](execution-readiness-choice.md)
passes and a start decision is open, or when starting/resuming its authorized
execution. Assessment-only and insufficient-readiness paths do not need this
reference. Reuse current evidence and authorization; ordinary implementation
stays with `incremental-implementation` without a new admission ritual.

## 1. Offer One Scope-Bound Choice

Show the assessment and links before the question. Resolve and link the actual
handoff deliverables; bare filenames do not provide that reviewable entry.
Name the actual delegated
scope and endpoint, including expected human checkpoints. When Goal support is
available, prefer these choices in the user's language:

| Choice | Meaning |
|---|---|
| Execute with Goal (Recommended) | Explicitly authorize a Goal and execution for the displayed scope under the stated boundaries. |
| View assessment and plan | Inspect existing evidence, scope and steps; authorize no execution or Goal. |
| Not now | Defer this scope and suppress another unsolicited offer. |

Goal preference in the Skill is a recommendation, not user consent. A user's
explicit applicable preference or conditional instruction to use Goal can
already supply that authorization; preserve it across turns. An ordinary
execution request or a legacy reply such as “execute T1” grants only the scope
and facilities actually requested. Never hide publishing, external messages,
model changes, extra milestones or a Goal inside an unlabeled start option.

Use a structured host user-input tool only when its current rules permit this
decision. Prefer `request_user_input_async` with `options` if available; otherwise
use a permitted equivalent. Do not use a Plan-only tool outside Plan mode or a
tool that forbids authorization questions. Do not switch modes to obtain UI.
If no suitable tool exists, ask one concise plain-text question including the
Goal choice, scope and endpoint. Do not fabricate a widget or add runtime code.
Tool acceptance confirms question submission, not the user's answer.

Preselection, silence, elapsed time, viewing the plan and unrelated replies
grant no authorization. Keep dependent execution pending; independent authorized
work may continue. After a matching explicit answer, recheck scope, authority,
dependencies, gates, effective configurations and Goal state before dispatch.
A stale answer cannot authorize a changed scope. Viewing displays the existing
assessment without replanning or immediately repeating the offer; a decline
preserves evidence and stays suppressed until the user reopens the decision.

## 2. Start or Resume the Authorized Goal

Use actual host Goal tools and their current contracts. Before offering Goal
execution, establish availability and inspect current Goal state when a read tool
is available. Recheck on startup/resume:

- **No active Goal:** With explicit applicable Goal authorization, create one
  whose objective identifies the agreed scope, delivery/acceptance endpoint and
  canonical execution entry. Set a token budget only when explicitly requested.
- **Same unfinished Goal:** Reuse its compatible scope and acceptance endpoint;
  do not duplicate it. Follow host rules to resume a blocked/paused Goal.
- **Different unfinished Goal:** Report the conflict. Do not overwrite it,
  falsely mark it complete, clear it, or silently switch to ordinary execution.
  Continue unrelated authorized preparation while the required choice is pending.
- **Missing, failed or uncertain Goal support:** Report what is known. Do not
  claim activation, repeat uncertain creation blindly, or silently substitute a
  mechanism. With a read tool, reconcile actual state first. Offer ordinary
  execution explicitly when suitable; selecting it does not weaken project
  requirements. Existing ordinary-execution authorization stays valid.

When Goal is unavailable or conflicting, do not present an unqualified
recommended Goal-start option. Explain the limitation and request only the
necessary scoped choice through a permitted host mechanism. A user's explicit
conditional “if ready, execute scope X with Goal” needs no second approval after
the assessment passes, but still obeys Goal availability and conflicts.

Record the matching authorization and Goal association in the existing queue
when state writes are allowed. Transition a task to READY only when its current
contract holds. Hand execution to `incremental-implementation` within the
selected scope; routine authorized steps need no repeated start approval.

For independent modules, apply the shared [parallel execution contract](../../../references/orchestration-patterns.md#parallel-module-execution):
one controller and Goal, one business queue, bounded independent worker tasks,
and controller-owned integration/acceptance. A list of modules alone does not
prove their writes, shared resources or contracts can run concurrently.

## 3. Preserve Readiness and Acceptance During Execution

Bind the assessment to scope/authority revisions and evidence in the existing
entry/queue. Reassess affected work when consequential requirements, contracts,
dependencies, environment, authorization or Goal scope change. Editorial changes
alone do not invalidate readiness, reset a decline or reopen accepted decisions.
Preserve completed evidence and independent authorized work.

Ordinary test failures call for diagnosis and repair. Repeating the same failure
without new evidence is not progress: retain the blocker and resolution condition
instead of looping, weakening checks or changing provider/scope. Stop affected
business work immediately at an unmet authority boundary; update Goal state only
under the host's actual lifecycle rules. A tool's blocking threshold never grants
permission to continue prohibited work.

At each milestone, reconcile deliverables and required verification, independent
review and acceptance evidence. Missing Owner acceptance or required integration
evidence remains pending. Mark a Goal complete only when its actual agreed
endpoint is achieved; do not redefine it as “coding finished” or “awaiting
acceptance.” A budget limit or blocked dependency is not completion.

Keep one business state authority. Use conversation context for the offer/reply;
persist only needed offer, authorization, Goal association and evidence in the
existing queue for durable handoff. The first real run may record unexpected
human decisions and preparation-related rework there to improve these rules;
do not add telemetry or claim a measured reduction without observations.
This flow creates no automation, watcher or separate conversation.
