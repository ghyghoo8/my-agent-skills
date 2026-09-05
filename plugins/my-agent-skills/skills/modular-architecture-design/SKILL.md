---
name: modular-architecture-design
description: Performs read-only architecture triage when explicitly requested or when a feature or structural refactor may change responsibility, ownership, dependency direction, public contracts, or migration boundaries. Do not invoke implicitly for local fixes, presentation edits, mechanical file moves, stable multi-file changes, or speculative scale alone; if triage is already active, route them DIRECT.
---

# Modular Architecture Design

## Overview

Route architecture-sensitive work before implementation. Gather only enough project evidence to choose one path, then either proceed, record a small boundary note, pause for an accepted architecture brief, or run bounded discovery.

This is a proportional gate, not a rule that every change needs design work. Project authority and observed code take precedence over generic heuristics.

Ordinary local work is not an implicit trigger. If the user explicitly requests this workflow, or triage is already active, stable-boundary evidence still receives the `DIRECT` path rather than an unnecessary gate.

## Operating Boundary

Use this workflow when a proposed feature or structural refactor may materially change at least one of these dimensions:

- module responsibility;
- ownership of data or critical side effects;
- dependency direction, including a new cycle;
- a public or cross-team contract, including errors and state semantics;
- a live migration, replacement, cutover, or rollback boundary.

The following facts are not sufficient by themselves: many files, a long file, a request for "modularity," possible future reuse, an external API, or imagined future scale.

## Workflow

### 1. Establish Authority and Evidence

Before modifying implementation code:

1. Read the nearest project instructions and the authoritative architecture, specification, or decision documents relevant to the change.
2. Read the affected code, nearby tests and types, and one local example of the pattern the change would follow.
3. Identify the current responsibility, data and side-effect owners, allowed dependency direction, exposed contracts, and any migration constraints.
4. Separate confirmed facts from missing evidence. Do not infer a boundary from filenames or a proposed solution alone.

Keep this phase read-only. Gather the smallest evidence set that can support a routing decision. More reading is justified only when it can change the route.

Read [references/triage.md](references/triage.md) for the decision test, evidence standard, and short boundary-note format.

### 2. Select Exactly One Path

Emit one, and only one, routing path:

| Path | Use when | Required next action |
|---|---|---|
| `DIRECT` | The change stays inside existing responsibilities, ownership, dependencies, contracts, and migration boundaries. | State the evidence briefly, then implement within the user's authorization. |
| `BOUNDARY_NOTE` | A local boundary or internal contract is affected, but responsibility, ownership, and dependency direction remain stable. | Record a short boundary note, then implement. |
| `ARCHITECTURE_GATE` | Evidence confirms a material change to responsibility, ownership, dependency direction, contract semantics, or migration boundaries. | Stop implementation, draft or update one canonical architecture brief, and obtain user acceptance before implementation planning. |
| `DISCOVERY` | A routing fact is unknown and the missing evidence could change the route or design. | Define and run a bounded investigation or isolated prototype, then rerun triage. |

Use this output contract:

```text
ARCHITECTURE TRIAGE
Path: DIRECT | BOUNDARY_NOTE | ARCHITECTURE_GATE | DISCOVERY
Evidence: <project-specific facts and file or document locations>
Boundary impact: <what changes, or why boundaries remain stable>
Next action: <the single next step allowed by this path>
```

Do not hedge between paths. If a critical fact is unknown, choose `DISCOVERY`, not a guessed architecture decision.

### 3. Respect the Selected Path

For `DIRECT`, proceed with the narrow implementation and ordinary verification.

For `BOUNDARY_NOTE`, record the affected local contract and the responsibilities and direction that remain unchanged. Keep the note short; it is not a disguised architecture brief.

For `ARCHITECTURE_GATE`:

An existing accepted brief satisfies acceptance for its exact scope across turns. Keep the material-change route and proceed through its satisfied exit without requesting the same acceptance again. New material changes or contradictory evidence require renewed triage; general delegation alone is not brief acceptance. Until acceptance is satisfied:

- do not modify business implementation code;
- read [references/architecture-brief.md](references/architecture-brief.md);
- update an existing authoritative brief when one exists, otherwise create or present one canonical brief;
- ask the user to accept the brief before producing an implementation plan or changing business code.

For `DISCOVERY`:

- do not modify business implementation code;
- name the unknown, the smallest evidence-gathering action, and the exit criterion;
- prefer read-only inspection or measurement;
- keep any necessary prototype isolated and disposable rather than wiring it into production paths;
- report what was learned and rerun this workflow before planning implementation.

### 4. Control Abstraction and Migration Scope

Every new abstraction must answer at least one current need, materially reduce a demonstrated risk, or provide a measured operational benefit. Do not preselect microservices, event buses, plugin systems, generic repositories, or provider-neutral layers for hypothetical growth.

When a migration is real, preserve coexistence, compatibility, cutover, and rollback invariants. Do not label a replacement complete while ownership or the source of truth remains ambiguous.

Maintain one canonical architecture brief. Merge corrections into it; never create sibling "enhanced," "revised," or "final" variants.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "It touches many files, so it needs an architecture brief." | File count does not prove a boundary change. Trace responsibility, ownership, dependencies, contracts, and migration instead. |
| "The user asked for modular code, so we should add layers first." | Modularity is an outcome. New layers need a current requirement or demonstrated risk reduction. |
| "An external provider means we need a generic adapter now." | An external API alone is not a gate or a reason to generalize. Use `DISCOVERY` only when missing provider facts determine the boundary. |
| "We can write the implementation while the brief is reviewed." | That turns an unaccepted design into sunk cost. `ARCHITECTURE_GATE` pauses business implementation. |
| "We should split services now for a future million users." | Hypothetical scale is not evidence. Measure a current constraint before changing ownership and failure semantics. |

## Red Flags

- More than one routing path is emitted.
- Project-specific evidence is replaced by generic best practices.
- File size, file count, or vocabulary is treated as decisive evidence.
- Business code changes before the exit condition of `ARCHITECTURE_GATE` or `DISCOVERY` is satisfied.
- A speculative distributed system is treated as the default solution.
- Multiple architecture briefs describe the same decision.
- An existing project authority is silently overridden.

## Verification

Before leaving triage, confirm:

- [ ] The nearest project authority, relevant code and tests or types, and one local pattern were inspected.
- [ ] Current and proposed boundaries are supported by named evidence.
- [ ] Exactly one path was selected and its write boundary was respected.
- [ ] Non-triggers did not manufacture an architecture gate.
- [ ] Every proposed abstraction has a current justification.
- [ ] `ARCHITECTURE_GATE` uses one minimal canonical brief and requires acceptance before implementation planning; existing acceptance for the same scope satisfies this condition.
- [ ] `DISCOVERY` has a bounded question, evidence action, and exit criterion.
