# Architecture Gate Evals

`architecture-gate/cases.yaml` contains 14 structured cases across positive, negative, boundary, and adversarial categories.

Each case records the request, minimum project evidence, expected route, and observable invariants. Reviewers score:

- exactly one selected route;
- the business-code write boundary;
- use of project evidence;
- rejection of speculative abstractions;
- one canonical architecture brief when gated.

Do not score exact wording or heading style. A persuasive answer fails if it selects the wrong route, writes business implementation under `ARCHITECTURE_GATE` or `DISCOVERY`, or introduces unsupported architecture.

No model runner is bundled in v0.1. For a clean-context forward review, give a reviewer only the Skill, one case's request, and its minimum evidence; compare the result with `expected_path` and `key_invariants`.
