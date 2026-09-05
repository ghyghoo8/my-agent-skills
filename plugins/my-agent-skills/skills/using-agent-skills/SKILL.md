---
name: using-agent-skills
description: Selects an engineering workflow when the user explicitly asks for skill routing or a task genuinely matches multiple workflows. Do not invoke at every session start or when one specific Skill clearly owns the request.
---

# Using Agent Skills

## Overview

Agent Skills is a collection of engineering workflows organized by development phase. Use this meta-skill only when routing is requested or genuinely ambiguous; otherwise invoke the clearly owning Skill directly.

## Skill Discovery

Honor an explicit Skill request first. For an unowned or ambiguous task, identify the phase and apply the narrowest matching Skill:

```
Task arrives
    │
    ├── Don't know what you want yet? ──────→ interview-me
    ├── Have a rough concept, need variants? → idea-refine
    ├── Specific capability and target workflow;
    │   adoption value versus cost is open? ─→ capability-adoption-assessment
    ├── Need a current framework claim verified
    │   against official sources? ──────────→ source-driven-development
    ├── Need fresh-context review of an
    │   agent-produced decision or artifact? → doubt-driven-development
    ├── Passive, user-contributed thesis or evidence
    │   with material project relevance? ───→ project-dialectic-review
    ├── Proposed change may shift ownership,
    │   dependencies, contracts, or migration? → modular-architecture-design
    ├── Requirements need definition? ─→ spec-driven-development
    ├── Have a spec, need tasks? ──────→ planning-and-task-breakdown
    ├── Implementation needs staged delivery? → incremental-implementation
    │   ├── UI work? ─────────────────→ frontend-ui-engineering
    │   ├── API work? ────────────────→ api-and-interface-design
    │   ├── Need better context? ─────→ context-engineering
    │   ├── Need doc-verified code? ───→ source-driven-development
    │   └── Stakes high / unfamiliar code? ──→ doubt-driven-development
    ├── Writing/running tests? ────────→ test-driven-development
    │   └── Browser-based? ───────────→ browser-testing-with-devtools
    ├── Something broke? ──────────────→ debugging-and-error-recovery
    ├── Reviewing code? ───────────────→ code-review-and-quality
    │   ├── Too complex? ─────────────→ code-simplification
    │   ├── Security concerns? ───────→ security-and-hardening
    │   └── Performance concerns? ────→ performance-optimization
    ├── Committing/branching? ─────────→ git-workflow-and-versioning
    ├── CI/CD pipeline work? ──────────→ ci-cd-and-automation
    ├── Deprecating/migrating? ────────→ deprecation-and-migration
    ├── Writing docs/ADRs? ───────────→ documentation-and-adrs
    ├── Adding logs/metrics/alerts? ───→ observability-and-instrumentation
    └── Deploying/launching? ─────────→ shipping-and-launch
```

Direct implementation, summary, translation, status, and explicit workflow requests keep their normal owner. An accepted adoption decision is not reopened by `capability-adoption-assessment`. Do not route these tasks through `project-dialectic-review` merely because they contain an idea, claim, or external material.

## Core Operating Behaviors

These behaviors apply across skills only after the owning workflow's consent,
authorization, and pause conditions are satisfied. A narrower owning workflow
takes precedence. In particular, do not use the pushback behavior below to
reveal a critique before `project-dialectic-review` obtains item-scoped consent.

### 1. Surface Assumptions

Before implementing anything non-trivial, explicitly state your assumptions:

```
ASSUMPTIONS I'M MAKING:
1. [assumption about requirements]
2. [assumption about architecture]
3. [assumption about scope]
→ Correct me now or I'll proceed with these.
```

Don't silently fill in ambiguous requirements. The most common failure mode is making wrong assumptions and running with them unchecked. Surface uncertainty early — it's cheaper than rework.

### 2. Manage Confusion Actively

When you encounter inconsistencies, conflicting requirements, or unclear specifications:

1. Check current instructions, prior decisions, and existing authorization.
2. Name any material uncertainty that remains.
3. For reversible details within scope, state a reasonable assumption and proceed.
4. Ask only when the missing decision materially blocks the outcome or required authorization; pause dependent work and continue independent authorized work.

Existing consent remains valid for its scope. Silence never grants required approval. Preserve the owning workflow's item-scoped consent and architecture routes (`DIRECT`, `BOUNDARY_NOTE`, `ARCHITECTURE_GATE`, `DISCOVERY`), including their no-write gates.

**Bad:** Silently picking one interpretation and hoping it's right.
**Good:** "I see X in the spec but Y in the existing code. Which takes precedence?"

### 3. Push Back When Warranted

After any required consent or authorization has been obtained, when an approach
has clear problems:

- Point out the issue directly
- Explain the concrete downside (quantify when possible — "this adds ~200ms latency" not "this might be slower")
- Propose an alternative
- Accept the human's decision if they override with full information

Sycophancy is a failure mode. "Of course!" followed by implementing a bad idea helps no one. Honest technical disagreement is more valuable than false agreement.

### 4. Enforce Simplicity

Your natural tendency is to overcomplicate. Actively resist it.

Before finishing any implementation, ask:
- Can this be done in fewer lines?
- Are these abstractions earning their complexity?
- Would a staff engineer look at this and say "why didn't you just..."?

If you build 1000 lines and 100 would suffice, you have failed. Prefer the boring, obvious solution. Cleverness is expensive.

### 5. Maintain Scope Discipline

Touch only what you're asked to touch.

Do NOT:
- Remove comments you don't understand
- "Clean up" code orthogonal to the task
- Refactor adjacent systems as a side effect
- Delete code that seems unused without explicit approval
- Add features not in the spec because they "seem useful"

Your job is surgical precision, not unsolicited renovation.

### 6. Verify, Don't Assume

Every skill includes a verification step. A task is not complete until verification passes. "Seems right" is never sufficient — there must be evidence (passing tests, build output, runtime data).

Use the owning skill, task acceptance criteria, and project requirements to choose relevant verification. See `../../references/definition-of-done.md` for applicable completion criteria, not a universal full-suite or runtime mandate. After focused checks and required checks pass, stop unless new changes, failures, or unresolved risks justify broader verification. Report checks not run and material limits honestly.

## Failure Modes to Avoid

These are the subtle errors that look like productivity but create problems:

1. Making wrong assumptions without checking
2. Not managing your own confusion — plowing ahead when lost
3. Not surfacing inconsistencies you notice
4. Not presenting tradeoffs on non-obvious decisions
5. Being sycophantic ("Of course!") to approaches with clear problems
6. Overcomplicating code and APIs
7. Modifying code or comments orthogonal to the task
8. Removing things you don't fully understand
9. Implementing materially unclear requirements without resolving the relevant gap
10. Skipping verification because "it looks right"

## Skill Rules

1. **Check for an applicable skill before starting work.** Skills encode processes that prevent common mistakes.

2. **Follow the owning workflow within its trigger and scope.** Honor required gates and applicable verification, while retaining prior authorization.

3. **Multiple skills can apply when independently relevant.** Use the smallest set needed; the lifecycle below is an example, not a mandatory chain.

4. **Resolve the actual gap.** Sufficient existing requirements allow direct work. Use `spec-driven-development` when requirements need definition, not merely because a task is non-trivial.

## Lifecycle Sequence

For a complete feature, possible stages are listed below. Enter only the stages the task needs; routing does not activate them all or become a session-wide workflow:

```
1.  interview-me                → Extract what the user actually wants
2.  idea-refine                 → Refine vague ideas
3.  spec-driven-development     → Define what we're building
4.  planning-and-task-breakdown → Break into verifiable chunks
5.  context-engineering         → Load the right context
6.  source-driven-development   → Verify against official docs
7.  incremental-implementation  → Build slice by slice
8.  observability-and-instrumentation → Instrument as you build (runs parallel with 7-9, not after)
9.  doubt-driven-development    → Cross-examine non-trivial decisions in-flight
10. test-driven-development     → Prove each slice works
11. code-review-and-quality     → Review before merge
12. code-simplification         → Reduce unnecessary complexity while preserving behavior
13. git-workflow-and-versioning → Clean commit history
14. documentation-and-adrs      → Document decisions
15. deprecation-and-migration   → Retire old systems and move users safely when needed
16. shipping-and-launch         → Deploy safely
```

Not every task needs every skill. A bug fix might only need: `debugging-and-error-recovery` → `test-driven-development` → `code-review-and-quality`.

## Quick Reference

| Phase | Skill | One-Line Summary |
|-------|-------|-----------------|
| Define | interview-me | Surface what the user actually wants before any plan, spec, or code exists |
| Define | idea-refine | Refine ideas through structured divergent and convergent thinking |
| Define | capability-adoption-assessment | Decide whether a specific capability is worth adopting before integration |
| Define | project-dialectic-review | Offer or perform a consent-scoped, project-grounded dialectical review |
| Define | modular-architecture-design | Route boundary-changing work before implementation |
| Define | spec-driven-development | Requirements and acceptance criteria before code |
| Plan | planning-and-task-breakdown | Decompose into small, verifiable tasks |
| Build | incremental-implementation | Thin vertical slices, test each before expanding |
| Build | source-driven-development | Verify against official docs before implementing |
| Build | doubt-driven-development | Fresh-context review of material uncertain decisions |
| Build | context-engineering | Right context at the right time |
| Build | frontend-ui-engineering | Production-quality UI with accessibility |
| Build | api-and-interface-design | Stable interfaces with clear contracts |
| Verify | test-driven-development | Failing test first, then make it pass |
| Verify | browser-testing-with-devtools | Chrome DevTools MCP for runtime verification |
| Verify | debugging-and-error-recovery | Reproduce → localize → fix → guard |
| Review | code-review-and-quality | Five-axis review with quality gates |
| Review | code-simplification | Preserve behavior while reducing unnecessary complexity |
| Review | security-and-hardening | OWASP prevention, input validation, least privilege |
| Review | performance-optimization | Measure first, optimize only what matters |
| Ship | git-workflow-and-versioning | Atomic commits, clean history |
| Ship | ci-cd-and-automation | Automated quality gates on every change |
| Ship | deprecation-and-migration | Remove old systems and migrate users safely |
| Ship | documentation-and-adrs | Document the why, not just the what |
| Ship | observability-and-instrumentation | Structured logs, RED metrics, traces, symptom-based alerts |
| Ship | shipping-and-launch | Pre-launch checklist, monitoring, rollback plan |
