# Architecture Triage Reference

Use this reference to distinguish material boundary changes from ordinary implementation work.

## Authority Order

Use the closest applicable authority in this order:

1. nearer project or module instructions;
2. accepted architecture documents, specifications, and decision records;
3. current code, tests, types, schemas, and migration state;
4. one local implementation pattern;
5. the heuristics in this reference.

When authorities conflict, surface the conflict instead of choosing silently. A generic heuristic never overrides a project-specific rule.

## Evidence Standard

Evidence must describe both the current boundary and the proposed delta. Useful evidence includes:

- the module that currently owns a responsibility;
- the source of truth and the only authorized writer for data;
- the component that owns an external mutation, retry state, or idempotency key;
- allowed imports or calls between modules;
- public schemas, status codes, error codes, states, events, or maintained consumers;
- live records, callers, or processes that must coexist during a migration.

Names and layout are clues, not proof. A directory named `services`, a large file, or a user request to "make it modular" does not establish ownership.

## Decision Test

Ask the questions in order:

1. Is a fact needed to determine boundary impact unknown?
   - If yes and it could change the route, choose `DISCOVERY`.
2. Does confirmed evidence show a material change in any dimension below?
   - If yes, choose `ARCHITECTURE_GATE`.
3. Is there a real but local boundary or internal-contract impact while responsibility, ownership, and dependency direction remain stable?
   - If yes, choose `BOUNDARY_NOTE`.
4. Otherwise choose `DIRECT`.

### Materiality by Dimension

| Dimension | Material signal | Usually not material |
|---|---|---|
| Responsibility | A capability moves, splits across competing owners, or gains a new authoritative owner. | Private helpers move within the same owner. |
| Data ownership | The source of truth, write authority, lifecycle, or consistency model changes. | The same owner adds a private field without changing consumers. |
| Side effects | A different module can charge, refund, notify, publish, delete, retry, or deduplicate an external action. | Existing orchestration calls the same owner through the same contract. |
| Dependency direction | A new cross-boundary edge, inversion, or cycle changes the permitted graph. | More files use an already-approved dependency in the same direction. |
| Contract | Public or cross-team inputs, outputs, errors, states, ordering, or compatibility semantics change. | A private function signature changes inside one module. |
| Migration | Old and new owners or representations must coexist, cut over, backfill, or roll back. | A reversible local refactor needs no live transition. |

## Path Calibration

### `DIRECT`

Choose `DIRECT` for work contained by existing boundaries. Typical examples include a local bug and regression test, copy or style edits, a mechanical file split that preserves exports, and a multi-file change inside one module.

### `BOUNDARY_NOTE`

Choose `BOUNDARY_NOTE` only when the boundary impact is real but contained. For example, adding a field to an existing internal command may affect two modules while preserving the command owner, receiver, data owner, and dependency direction.

Use this short format:

```text
Boundary note: <local contract or boundary change>.
Preserved: <responsibility, ownership, dependency direction, compatibility>.
Verification: <test or observable proof>.
```

### `ARCHITECTURE_GATE`

Choose `ARCHITECTURE_GATE` when evidence already proves a material boundary change and the missing artifact is an accepted design. Stop business implementation until that acceptance exists.

### `DISCOVERY`

Choose `DISCOVERY` when the facts needed to classify or design the change are missing. State:

- the decision-blocking unknown;
- the smallest inspection, measurement, experiment, or provider fact needed;
- the limit of the investigation;
- the evidence that ends discovery;
- that triage will run again afterward.

Performance uncertainty is not automatically discovery. It becomes discovery when a proposed boundary change depends on an unmeasured constraint. An unknown external provider is not automatically discovery either; it becomes discovery when authentication, callback, error, data, or compliance semantics determine the boundary.

## Non-Triggers

Never escalate solely because of:

- the number of files or modules mentioned;
- file length;
- a desire for clean or modular code;
- possible reuse;
- the existence of an external API;
- a hypothetical future load;
- a forceful request to use microservices, Kafka, or another named solution.

Treat the proposed technology as a hypothesis. Route based on current responsibility, ownership, dependencies, contracts, migration, and evidence.
