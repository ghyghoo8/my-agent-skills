---
name: capability-adoption-assessment
description: Assesses whether a specific capability is worth adopting into a workflow. Use for an open integration decision that needs an explicit value-versus-cost recommendation. Excludes vague ideas, passive theses, architecture-only review, approved work, mandatory fixes, and status queries.
---

# Capability Adoption Assessment

## Purpose

Decide whether a target workflow should spend delivery and maintenance capacity
on a specific new or existing capability. Technical compatibility is evidence,
not a recommendation: the decision depends on incremental value relative to the
current baseline and the full cost of adoption.

This is a read-only decision workflow. It does not authorize a pilot,
implementation, migration, or architecture change.

## Frame the Decision

Identify the candidate capability, target workflow, current baseline, and the
observable outcome adoption is meant to improve. Distinguish the capability's
general merits from its incremental contribution to this target.

Use the user's stated success threshold or constraint when available. If one
missing expectation could materially reverse the result, ask one concise
question about that outcome or threshold, then wait. Otherwise state the
smallest reasonable assumption and continue; do not start a broad interview.

## Gather Only Decision-Changing Evidence

Read the smallest project evidence set that can establish:

- the target workflow's current problem, baseline, users, and usage frequency;
- the capability's maturity, outputs, contracts, and demonstrated behavior;
- the semantic, data, policy, or lifecycle gap between capability and target;
- integration, validation, migration, operating, and maintenance obligations;
- current alternatives and the opportunity cost of choosing this work.

Stop gathering evidence once additional detail cannot change the rating or
recommendation. Do not turn an obvious no-go into a full architecture study.
Missing evidence remains `UNKNOWN`; it is not permission to invent benefit,
effort, dates, money, or ROI.

## Assess Value

Rate incremental value as `HIGH`, `MEDIUM`, `LOW`, or `UNKNOWN`, and state the
confidence and evidence. Consider:

- expected improvement over the current baseline;
- number of affected users or decisions and how often the benefit occurs;
- whether an existing capability already provides the same outcome;
- time to observable value and a metric that could verify it;
- risk reduction or required obligation when it is genuinely decision-relevant.

Novelty, technical sophistication, and already-written code are not value by
themselves.

## Assess Cost

Rate total adoption cost as `HIGH`, `MEDIUM`, `LOW`, or `UNKNOWN`, and state the
confidence and evidence. Include only material dimensions, but consider:

- one-time work: semantic adapters, contracts, data, policy, tests, migration,
  rollout, and rollback;
- recurring work: operations, monitoring, support, governance, retraining,
  version coupling, and maintenance;
- risk and opportunity cost: failure impact, reversibility, and displaced work.

Existing implementation effort is sunk cost. Use numeric estimates only when
project evidence supports them; otherwise use honest relative ratings.

## Select One Recommendation

Choose exactly one recommendation:

- `GO`: evidence shows incremental value outweighs total cost sufficiently to
  continue into the owning design workflow.
- `PILOT`: value is plausible and one low-cost, reversible validation can resolve
  the main uncertainty without wiring the production flow.
- `DEFER`: a decision-changing unknown remains and the useful validation is not
  yet ready or cheap enough to run now.
- `NO-GO`: expected value does not justify cost, risk, or opportunity cost.

Also state the net result as `POSITIVE`, `UNCERTAIN`, or `NEGATIVE`. Do not use a
weighted score unless the project or user already defines the weights.

For `NO-GO`, stop without architecture or implementation planning. For `DEFER`,
name the smallest evidence action and revisit condition. For `GO` or `PILOT`,
hand off next to `modular-architecture-design` only when responsibility,
ownership, dependencies, public contracts, or migration may change; this Skill
does not select an architecture path itself. Subsequent work keeps its own user
authorization boundary.

## Output Contract

If a decision-changing clarification is required, respond with that one question
only and wait; do not issue provisional ratings. The contract below applies to
the final assessment after the answer is available.

Default to a compact decision card. Use one decision-relevant evidence clause
per field and combine material Cost dimensions on one line. Expand only when
the user asks, a material uncertainty needs explanation, or a high-impact
handoff depends on it. Never bury or omit Value, Cost, net result, or the single
recommendation:

```text
CAPABILITY ADOPTION ASSESSMENT
Capability -> Target: <candidate -> workflow>
Outcome and baseline: <observable improvement and current state>
Value: HIGH | MEDIUM | LOW | UNKNOWN — <incremental evidence; confidence>
Cost: HIGH | MEDIUM | LOW | UNKNOWN — one-time: <...>; recurring: <...>; risk/opportunity: <... when material>
Net result: POSITIVE | UNCERTAIN | NEGATIVE
Recommendation: GO | PILOT | DEFER | NO-GO
Why: <the decisive value-versus-cost comparison>
Unknowns: <none, or only decision-changing unknowns>
Next action: <stop, bounded validation, or owning workflow handoff>
```

## Verification

Before the final assessment response, confirm:

- [ ] A specific capability, target workflow, and observable target outcome were identified.
- [ ] Value and Cost are separate explicit results grounded in current evidence.
- [ ] Unknowns and confidence are visible; unsupported precision was not invented.
- [ ] Exactly one net result and one recommendation were selected.
- [ ] Any earlier question was the only clarification and contained no provisional decision.
- [ ] `NO-GO` stopped further planning; any handoff preserved the next workflow's ownership.
- [ ] No implementation, pilot, migration, or external action was inferred from assessment consent.
