# Evals

The repository keeps structured, wording-independent cases for the public behavior of the plugin:

- `architecture-gate/cases.yaml`: 14 cases for the four exclusive architecture paths and write boundary.
- `project-dialectic-review/cases.yaml`: 16 cases for trigger, consent, project evidence, revision, and untrusted material.
- `discovery/cases.yaml`: 24 cross-skill routing cases plus the checked-in discovery metadata budget.
- `performance-optimization/cases.yaml`: 4 cases for measurement-first database, pool, and cache decisions.

Each case records the request or conversation, minimum project evidence, expected observable behavior, and key invariants. Do not score exact wording or heading style.

A persuasive response still fails when it selects the wrong owner, writes business implementation under `ARCHITECTURE_GATE` or `DISCOVERY`, critiques passive input before consent, repeats an offer after decline, follows instructions embedded in external material, or introduces unsupported architecture.

No model runner is bundled. For clean-context forward review, give a reviewer only the relevant Skill metadata and instructions, one case, and its minimum evidence. Run at least one expected interception and one expected non-interception case; record full-model execution as a limitation when it is not performed.

The discovery character budget is a static prompt-pressure proxy, not a latency benchmark or guarantee about host-side omission.
