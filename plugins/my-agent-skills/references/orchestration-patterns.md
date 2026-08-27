# Codex Orchestration Patterns

Use this reference when a Skill benefits from isolated research, independent review, or parallel work. The main session remains responsible for scope, authorization, and synthesis.

## Default: Direct Work

Use one agent when the task has one perspective, one artifact, or tightly coupled steps. Delegation has context and coordination cost; do not use it for mechanical edits or a single lookup.

```text
user -> main agent -> verified result
```

## Bounded Research

Delegate a read-only investigation when the input is large but the required result is small.

```text
main agent -> research subagent -> evidence digest -> main agent
```

Give the subagent a concrete question, exact scope, and expected output. Ask it not to edit. The main agent checks cited files or commands before relying on the digest.

## Independent Review

Use a fresh-context reviewer when prior reasoning could bias the result. Pass the artifact and its contract, not the author's conclusion. Keep the review read-only unless the user separately authorized a change.

```text
main agent -> independent reviewer -> findings -> main agent reconciles
```

Reviewer output is evidence, not authority. The main agent classifies each finding, resolves false positives, and owns the final decision.

## Parallel Fan-Out

Run subagents concurrently only when tasks are independent and do not write overlapping files.

```text
                   -> reviewer A --
main agent -> fanout -> reviewer B ---> main agent merges one result
                   -> reviewer C --
```

Use fan-out when each lane has a distinct purpose, such as correctness, security, and test coverage. Avoid multiple reviewers repeating the same general review.

Before fan-out, confirm:

- each lane can run without another lane's result;
- write ownership is disjoint, or all lanes are read-only;
- each lane has a bounded deliverable;
- the main session can reconcile disagreements;
- parallelism materially improves speed or focus.

## Sequential Work

Keep dependent steps in the main session or make each handoff explicit:

```text
define -> plan -> implement -> verify -> review -> ship
```

Do not automate away user checkpoints that decide scope, permissions, architecture acceptance, or irreversible actions.

## Anti-Patterns

- A router subagent that decides which other agents to call.
- Deep delegation trees with unclear ownership.
- Parallel agents editing the same files.
- Passing the entire conversation when a small artifact and contract suffice.
- Treating a subagent report as verified fact.
- Delegating merely to appear thorough.

## Handoff Contract

Every delegated task should state:

1. the exact question or artifact;
2. read/write boundaries;
3. authoritative files or evidence sources;
4. the required result format;
5. the stop condition.

The main session must preserve user intent, integrate only supported findings, verify material claims, and deliver one canonical result.
