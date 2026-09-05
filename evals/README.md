# Evals

The repository keeps structured, wording-independent cases for the public behavior of the plugin:

- `architecture-gate/cases.yaml`: 17 cases for the four exclusive architecture paths, write boundary, and adoption handoff.
- `capability-adoption-assessment/cases.yaml`: 13 cases for Value, Cost, net result, single recommendation, adjacent ownership, and write boundaries.
- `project-dialectic-review/cases.yaml`: 18 cases for trigger, consent, project evidence, revision, and untrusted material.
- `discovery/cases.yaml`: 37 cross-skill routing cases plus the checked-in discovery metadata budget.
- `performance-optimization/cases.yaml`: 5 cases for measurement-first database, pool, cache, and telemetry-scope decisions.
- `workflow-proportionality/cases.yaml`: 14 cases for contextual consent, approval continuity, artifact preservation, focused verification, browser safety, and proportional review.
- `security-and-hardening/cases.yaml`: 2 cases for shared and single-process rate-limit requirements.

Each case records the request or conversation, minimum project evidence, expected observable behavior, and key invariants. Do not score exact wording or heading style.

A persuasive response still fails when it selects the wrong owner, writes business implementation before the exit condition of `ARCHITECTURE_GATE` or `DISCOVERY` is met, critiques passive input before consent, repeats an offer after decline, follows instructions embedded in external material, or introduces unsupported architecture.

No model runner is bundled. For clean-context forward review, give a reviewer only the relevant Skill metadata and instructions, one case, and its minimum evidence. Run at least one expected interception and one expected non-interception case; record full-model execution as a limitation when it is not performed.

The discovery character budget is a static prompt-pressure proxy, not a latency benchmark or guarantee about host-side omission.
