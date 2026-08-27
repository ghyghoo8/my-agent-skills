# Minimal Architecture Brief

Use this template only after selecting `ARCHITECTURE_GATE`.

Follow the project's existing documentation authority and location. Update an existing brief for the same decision. If none exists, create or present one canonical brief and keep later corrections in that document.

Do not write business implementation code until the user accepts the brief.

```markdown
# <Decision title>

Status: Proposed

## Goal and non-goals

Goal: <the current outcome and why it matters>

Non-goals:
- <explicitly excluded scope>

## Modules and ownership

| Module | Responsibility | Data owned | Side effects owned |
|---|---|---|---|
| <module> | <one clear responsibility> | <source of truth and writer> | <external mutations, retries, idempotency> |

## Dependency direction

<List the allowed arrows and explain any changed edge. State that cycles are absent, or name the cycle being resolved.>

## Boundary contract

- Interface: <commands, queries, events, or calls>
- Inputs and outputs: <required data and compatibility>
- Errors: <taxonomy and ownership>
- States: <valid states and transitions>
- Side effects: <executor, retry, deduplication, ordering>
- Invariants: <facts that must remain true>

## Migration and rollback

- Current state: <owner, representation, and active consumers>
- Transition: <coexistence, compatibility, or backfill>
- Cutover: <observable condition that changes authority>
- Rollback: <safe return path and preserved data>

## First verifiable vertical slice

- Scope: <smallest end-to-end slice>
- Proof: <test, runtime observation, or migration evidence>
- Stop condition: <what must be true before expanding>

## Alternative considered (optional; at most one)

<A materially different viable option and the reason it was not selected. Omit this section when there is no meaningful alternative.>

## Acceptance

Accepted by: <user or project authority>
Accepted on: <date or decision reference>
```

Keep the brief proportional. Do not add a roadmap, speculative extension points, or a catalog of alternatives. The purpose is to make the current boundary decision testable and reversible.
