# Definition of Done

A reusable template for a project-defined completion bar. Apply the criteria relevant to the authorized task and its impact, plus all checks required by the project. Unlike acceptance criteria, which vary per task and answer "did we build the right thing?", the Definition of Done supplies consistent criteria for comparable work and answers "is this finished to our standard?". Use the applicable criteria as the completion check in `planning-and-task-breakdown`, `incremental-implementation`, and `shipping-and-launch`.

## Definition of Done vs. Acceptance Criteria

| | Acceptance Criteria | Definition of Done |
|---|---|---|
| Scope | Specific to one task or spec | Applicable criteria for each increment |
| Changes | Different for each item | Project-defined and reused by scope |
| Answers | "Did we build *this thing*?" | "Is it *ready*?" |
| Owner | Defined when planning the task | Defined once for the project |
| Example | "User can reset password via email link" | "Tests pass, no regressions, docs updated" |

The two are complementary. A task is done only when **its** acceptance criteria are met **and** the standing Definition of Done is satisfied. Skipping either leaves work that looks finished but is not.

## The Standing Checklist

Select applicable items by actual change and lifecycle stage. A documentation edit does not require browser runtime testing, observability, or release approval. Do not waive project-mandated checks, authorization requirements, or architecture exit conditions. Explain meaningful verification gaps; no extra checklist is needed for obvious non-applicable items.

### Correctness
- [ ] All acceptance criteria for the task are met
- [ ] Changed behavior has appropriate evidence; verify at runtime when rendering, integration, or execution semantics require it
- [ ] Meaningful new behavior has outcome-based regression coverage; reversible low-impact edits do not need manufactured tests
- [ ] Relevant tests and required project checks pass; expand to the full suite when required or warranted by impact
- [ ] Edge cases and error paths are handled, not just the happy path

### Quality
- [ ] Code reveals intent through naming and structure; no comments needed to explain *what* it does
- [ ] No duplicated business logic
- [ ] No dead code, debug output, or commented-out blocks left behind
- [ ] Changes are scoped to the task; no unrelated refactors snuck in
- [ ] Applicable linting and formatting checks pass

The depth behind these items lives in `code-review-and-quality` (the five-axis review) and `code-simplification` (reducing complexity without changing behavior).

### Integration
- [ ] Change works with the rest of the system, not just in isolation
- [ ] Database migrations, config changes, and feature flags are accounted for
- [ ] Backward compatibility considered for any public interface or API change

### Documentation
- [ ] Public interfaces, APIs, and user-facing behavior are documented
- [ ] Architectural decisions worth preserving are recorded (see `documentation-and-adrs`)
- [ ] Documentation describes the current state in timeless language, not the change history

### Ship-readiness
- [ ] Security implications reviewed for any untrusted input, auth, or data handling (see `security-and-hardening`)
- [ ] Observability in place for new critical paths (logs, metrics, traces) (see `observability-and-instrumentation`)
- [ ] Rollback path exists for anything risky (see `shipping-and-launch`)
- [ ] Required review and authorization are satisfied for the actual merge or deployment; existing approval remains valid within its scope

## How to Apply

- **Per task**: confirm the Correctness and Quality sections before checking the task off.
- **Per feature**: confirm Integration and Documentation before considering the feature complete.
- **Per release**: apply relevant release criteria and mandatory project gates; `shipping-and-launch` supplies deployment-specific checks when releasing is in scope.

Define applicability in project policy and reuse it consistently. Update that policy when requirements change, not to excuse failures or bypass required gates. Once relevant checks pass, stop unless new changes, failures, or unresolved concerns justify additional verification.

## Red Flags

- "It's done, I just haven't run it yet": unverified work is not done.
- "Tests pass" used as a synonym for done while applicable documentation, regression, or runtime checks are skipped.
- A different bar applied depending on deadline pressure.
- Acceptance criteria treated as the whole bar, with no standing quality floor.
- "Done" declared before human review on changes that need it.
