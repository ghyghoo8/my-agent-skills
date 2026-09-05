---
name: planning-and-task-breakdown
description: Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when a task feels too large to start, when you need to estimate scope, or when parallel work is possible.
---

# Planning and Task Breakdown

## Overview

Decompose work into small, verifiable tasks with explicit acceptance criteria. Good task breakdown is the difference between an agent that completes work reliably and one that produces a tangled mess. Every task should be small enough to implement, test, and verify in a single focused session.

## When to Use

- You have a spec and need to break it into implementable units
- A task feels too large or vague to start
- Work needs to be parallelized across multiple agents or sessions
- You need to communicate scope to a human
- The implementation order isn't obvious

**When NOT to use:** Bounded changes with obvious scope, regardless of file count, or when the spec already contains well-defined tasks.

## The Planning Process

### Step 1: Establish the Plan

During initial evidence gathering, operate in read-only mode:

- Read the spec and relevant codebase sections
- Identify existing patterns and conventions
- Map dependencies between components
- Note risks and unknowns

For a planning-only request, keep business implementation unchanged and deliver the plan. When planning is part of an authorized implementation task, complete this preparation and continue without asking again unless a material unresolved decision or an applicable project gate requires acceptance. This Skill does not switch the host's collaboration mode. Preserve `ARCHITECTURE_GATE` and `DISCOVERY` write boundaries and their exit conditions.

### Step 2: Identify the Dependency Graph

Map what depends on what:

```
Database schema
    │
    ├── API models/types
    │       │
    │       ├── API endpoints
    │       │       │
    │       │       └── Frontend API client
    │       │               │
    │       │               └── UI components
    │       │
    │       └── Validation logic
    │
    └── Seed data / migrations
```

Implementation order follows the dependency graph bottom-up: build foundations first.

### Step 3: Slice Vertically

Instead of building all the database, then all the API, then all the UI — build one complete feature path at a time:

**Bad (horizontal slicing):**
```
Task 1: Build entire database schema
Task 2: Build all API endpoints
Task 3: Build all UI components
Task 4: Connect everything
```

**Good (vertical slicing):**
```
Task 1: User can create an account (schema + API + UI for registration)
Task 2: User can log in (auth schema + API + UI for login)
Task 3: User can create a task (task schema + API + UI for creation)
Task 4: User can view task list (query + API + UI for list view)
```

Each vertical slice delivers working, testable functionality.

### Step 4: Write Tasks

Each task follows this structure, whether it lands in the markdown task list or as an item in an external tracker (see Output Files):

```markdown
## Task [N]: [Short descriptive title]

**Description:** One paragraph explaining what this task accomplishes.

**Acceptance criteria:**
- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]

**Verification (include only applicable checks and project requirements):**
- [ ] Tests pass: [the repository's focused-test command]
- [ ] Build succeeds: [the repository's build command]
- [ ] Manual check: [description of what to verify]

**Dependencies:** [Task numbers this depends on, or "None"]

**Files likely touched:**
- `src/path/to/file.ts`
- `tests/path/to/test.ts`

**Estimated scope:** [Complexity, uncertainty, and independently verifiable outcomes]
```

### Step 5: Order and Checkpoint

Arrange tasks so that:

1. Dependencies are satisfied (build foundation first)
2. Each task leaves the system in a working state
3. Verification checkpoints cover meaningful integration or risk boundaries
4. High-risk tasks are early (fail fast)

Add explicit checkpoints to the task list target:

```markdown
## Checkpoint: After Tasks 1-3
- [ ] Relevant tests and project-required checks pass
- [ ] Affected integration or user flow is verified
- [ ] Any required acceptance is satisfied, including existing approval for this scope
```

## Task Sizing Guidelines

Split work when outcomes can be verified independently, uncertainty needs a bounded experiment, or integration risk makes a single change difficult to review or recover. Keep coherent mechanical changes together even when they span many files. File counts, line counts, elapsed-time estimates, and the word "and" are hints to inspect scope, not automatic splitting rules.

## Output Files

- **Plan document:** Use the project's designated plan location; otherwise use `.codex/agent-state/plan.md`. Keep one canonical plan for this task.
- **Task list:** Record each task in the **task list target** (defined below).

Create the designated parent directory only when a durable plan is useful for the task.

**Preserve incomplete plans.** Inspect the plan and task target before writing. For the same work being revised, update in place within the user's request. For different work, preserve the existing files and open tracker items. Use a distinct task-scoped path under the project-designated state directory when allowed; ask only if the fixed target conflicts and no permitted separate location exists. Continue independent work while that conflict is resolved. Never delete, rename, overwrite, or bulk-close another task's work to make room without authorization.

### Task List Target

The task list target is where tasks and checkpoints are recorded. It is defined once, here; every other reference in this skill defers to it.

- **Default: a checklist-style markdown file at `.codex/agent-state/todo.md`.** Project instructions and an existing task-specific location take precedence.
- **External tracker:** if project rules or the user designate and authorize an issue tracker, record each task there instead of creating a duplicate markdown checklist. Map acceptance criteria, verification, and dependencies onto the tracker's fields. Record applicable checkpoints there too, or in the plan if the tracker has no natural equivalent.

When using an authorized external tracker, note it in the canonical plan so downstream steps know where to look, and keep an ordered index of item IDs or links rather than a duplicate checklist. A tracker example does not authorize sending messages or creating external items.

## Plan Document Template

```markdown
# Implementation Plan: [Feature/Project Name]

## Overview
[One paragraph summary of what we're building]

## Architecture Decisions
- [Key decision 1 and rationale]
- [Key decision 2 and rationale]

## Task List

### Phase 1: Foundation
- [ ] Task 1: ...
- [ ] Task 2: ...

### Checkpoint: Foundation
- [ ] Tests pass, builds clean

### Phase 2: Core Features
- [ ] Task 3: ...
- [ ] Task 4: ...

### Checkpoint: Core Features
- [ ] End-to-end flow works

### Phase 3: Polish
- [ ] Task 5: ...
- [ ] Task 6: ...

### Checkpoint: Complete
- [ ] All acceptance criteria met
- [ ] Ready for review

## Risks and Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk] | [High/Med/Low] | [Strategy] |

## Open Questions
- [Question needing human input]
```

When tasks live in an external tracker, keep the Task List section above as an ordered index of tracker item IDs or links instead of a duplicate checklist.

## Parallelization Opportunities

When delegation is available and authorized, assign bounded independent tasks with non-overlapping write ownership; keep dependencies and final reconciliation in the main session:

- **Safe to parallelize:** Independent feature slices, tests for already-implemented features, documentation
- **Must be sequential:** Database migrations, shared state changes, dependency chains
- **Needs coordination:** Features that share an API contract (define the contract first, then parallelize)

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "I'll figure it out as I go" | That's how you end up with a tangled mess and rework. 10 minutes of planning saves hours. |
| "The tasks are obvious" | Write them down anyway. Explicit tasks surface hidden dependencies and forgotten edge cases. |
| "Planning is overhead" | Planning is the task. Implementation without a plan is just typing. |
| "I can hold it all in my head" | Context windows are finite. Written plans survive session boundaries and compaction. |

## Red Flags

- Starting implementation without a written task list
- Overwriting another task's incomplete plan or scattering duplicate checklists across files and a tracker
- Tasks that say "implement the feature" without acceptance criteria
- No verification steps in the plan
- Independent outcomes bundled into one task with no useful verification boundary
- No checkpoints between tasks
- Dependency order isn't considered

## Verification

Before starting implementation, confirm:

- [ ] Every task has acceptance criteria
- [ ] Every task has a verification step
- [ ] Task dependencies are identified and ordered correctly
- [ ] Tasks are recorded in the designated task list target
- [ ] Existing incomplete plans and unrelated tracker items are preserved
- [ ] Each task has a coherent scope and a useful verification boundary
- [ ] Checkpoints exist between major phases
- [ ] Required approvals are satisfied; already accepted scope is not reopened without new material evidence

## See Also

Acceptance criteria are per-task and answer "did we build the right thing?". They sit on top of the project-wide Definition of Done, the standing bar every task clears before it counts as done. See `../../references/definition-of-done.md`.
