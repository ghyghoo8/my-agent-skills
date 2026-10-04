# Progressive performance examples and official evidence reuse — 6.2.3

On 2026-10-04 the user authorized performance review items 1 and 3: make
implementation examples conditional and reuse already verified official evidence.
This follow-up stays in the pending 6.2.3 patch. It preserves all 27 Skill
frontmatter blocks, discovery cases, routes, model policy and the skills-only
runtime. Discovery-budget changes from review item 2 are outside this update.

## Performance example loading

Nine Step 3 code blocks, the backend timing example and the CI commands moved
verbatim from performance-optimization into the existing performance-checklist.
The frontend measurement snippet used the same web-vitals calls already present
in that reference, so the entrypoint now links to them without another copy.
Workflow diagrams, the symptom tree and example budgets remain in the entrypoint.

Each topic keeps its decision rule and links to its example by heading. The
Skill explicitly reads only sections relevant to the measured symptom or chosen
approach. Query execution safety, index write cost, pool headroom, cache identity
and staleness, controlled measurement, noise handling, rollback and authorization
remain in the entrypoint. Reference examples retain their own context and
illustrative-value boundaries. Existing request-coalescing and other reference
content remain available. The reference's field-data instruction now matches
the entrypoint's available-and-authorized boundary.

## Official evidence reuse

source-driven-development now reuses official evidence only within the same
task, confirmed version and covered feature/API. It retains source URLs, version
applicability and verified findings. Missing evidence, version drift, uncovered
APIs or conflicts require targeted retrieval before dependent implementation.
Unknown-version material, unverified summaries and memory cannot substitute for
official evidence; installed types only supplement signature checks. Source
priority, retrieval safety and existing authorization remain unchanged.

## Static input measurements

The metric is Unicode characters in complete UTF-8 Markdown files, measured with
the same Python `len(path.read_text(encoding="utf-8"))` before and after edits.

| Artifact | Before | After | Change |
|---|---:|---:|---:|
| performance-optimization/SKILL.md | 23,192 | 20,235 | -2,957 (-12.8%) |
| performance-checklist.md | 13,899 | 21,873 | +7,974 |
| source-driven-development/SKILL.md | 9,875 | 10,493 | +618 |
| Discovery names and descriptions | 6,826 | 6,826 | Unchanged; budget 7,000 |

This reduces the performance entrypoint's static input. The reference grows
because examples and targeted context live there; gains depend on reading only
relevant sections. These measurements do not establish model token counts,
host loading behavior, network-call savings or end-to-end latency improvements.

## Behavior coverage

Two performance cases cover scoped N+1 and hero-image example reading, preserving
the five existing cases. Two workflow-proportionality cases cover official
evidence reuse and invalidation, preserving all 43 prior cases including enum
reuse. There are now seven performance cases and 45 proportionality cases.
Static case coverage is separate from executing cases against a model.

## Independent next-action probes

Three fresh-context agents received only the relevant updated Skill, raw scenario
evidence and a bounded read-only request, without case expectations or prior
conclusions. These probes examine the same boundaries as the cases; they are
not full executions of the YAML suites.

| Probe | Observed action | Review |
|---|---|---|
| Measured owner-query bottleneck with existing ORM/benchmark | Read only N+1 and backend measurement reference sections; retain output/fallback tests, fixed measurement conditions, noise and rollback rules. | PASS |
| Second form using previously verified same-task/version/API evidence | Reuse the official source and findings; retain citations and relevant form tests without another fetch. | PASS |
| Version change plus an uncovered server-only API | Require the affected official API and migration pages before dependent implementation; old summaries/memory and local types do not replace evidence. | PASS |

No business implementation, external fetch, application benchmark, deployment
or installation occurred in the probes. Their installed versions and evidence
were supplied fixtures, not newly observed runtime facts. The version-change
probe used a virtual framework. Agent settings were inherited, with no separate
effective-model receipt. Full-suite and installed-plugin behavior remain
unverified.

## Validation

- `rtk proxy python3 /tmp/my-agent-skills-progressive-validation.py` — PASS:
  27 Skill quick validators, 20 JSON/YAML files, 31 uniquely owned upstream
  artifacts with unchanged pins, 137 relative links, 35 performance fragment
  links, unchanged frontmatter/discovery 6826/7000, preserved old cases,
  exact example relocation and original Step 3 safety paragraphs, and hygiene.
- `rtk proxy python3 scripts/validate_plugin.py plugins/my-agent-skills` — PASS.
- `rtk proxy python3 -m unittest discover -s tests -p 'test_validate_plugin.py'`
  — PASS: all 21 CLI tests.
- `rtk git diff --check` — PASS. Changed files and the new report were reviewed.

The independent before/after reviewer confirmed all relocated code blocks and
existing reference code blocks remain exactly once, links resolve, and safety
contracts remain in the entrypoint. A stale “example below” pointer was corrected
to “linked example.” The unavailable official system Plugin validator, public
submission, real application performance and model latency were not tested.
No commit, push, plugin-cache update or global configuration edit was performed.
