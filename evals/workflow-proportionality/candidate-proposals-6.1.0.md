# Candidate proposal assessment — 6.1.0

Date: 2026-09-27. Scope: direct development, design and planning requests that
contain unresolved proposed means, including a later request to write a development
document. The current task owner checks evidence before treating the proposal as
settled. Passive project dialectic review retains its consent boundary.

## Implementation and version

- `spec-driven-development` owns the short candidate check. Documentation and
  planning link to that section; a bounded local task can reason inline without
  the full specification lifecycle.
- `project-dialectic-review` and `using-agent-skills` clarify that skipping the
  independent review does not suppress judgment within a direct task. The review
  itself remains analysis-only; separately authorized follow-on work returns to
  its owner, even when that authority preceded the review.
- Goals, explicit constraints and accepted decisions remain distinct from
  candidate means. New material product choices retain their existing acceptance
  rules; delegated reversible details do not require another approval.
- MINOR adds compatible task-local assessment and handoffs. The standalone review
  output, passive-input consent, architecture paths and execution authority are
  preserved. No new Skill, runtime component or discovery description was added.

## Behavior cases

The eight additions are:

| Suite | New case IDs |
|---|---|
| discovery | `cabinet-suggestions-to-documentation-retain-owned-assessment`; `explicit-proposal-review-and-documents-use-existing-authorization`; `direct-suggested-local-fix-does-not-require-specification`; `cabinet-documentation-first-preserves-explicit-goal-follow-on` |
| project-dialectic-review | `mixed-direct-document-task-keeps-owner-judgment` |
| workflow-proportionality | `development-draft-does-not-accept-unsettled-product-rule`; `accepted-proposal-documentation-does-not-reopen-review`; `evidence-supported-proposal-needs-no-manufactured-opposition` |

The documentation-only cabinet continuation is explicitly synthetic. A separate
case preserves the actual follow-up wording authorizing a document and then Goal
execution. The prior 104 case objects in these three suites remain unchanged;
counts are now 60, 19 and 33. Existing passive-input and decline cases are retained.

## Next-action observations

Three fresh subagent contexts received raw scenario requests, minimum project
facts and permission to read Skill metadata and selected instructions. They were
not given the patch, eval files, expected answers or other agents' output. The
first batch contained two scenarios and the second five; scenarios within a
batch shared that reader context. A final separate sample checked explicit review
plus authorized documentation after the authorization-continuity wording was
clarified. These are simulations of the next reply and intended actions, not
actual business edits or live Goal calls. No model/effort override was requested;
no independent effective-model receipt was available.

The following preserves the supplied requests/facts and excerpts of observed
responses. Main-thread assessment found the sampled boundaries satisfied;
there was no separate blind grader or statistical repeat run.

### Batch 1: mixed requests

**A.** User requests four changes: prominent underlined cabinet/report links;
actual A/B pump readings instead of an average, with right-panel ceiling;
gray/green/red/orange `system_status`; and a centered temperature label without
its horizontal leader. Follow-up: “先按优化点整理详细、可交付的开发文档，然后开启goal，执行文档。”
Facts: the existing green dot means communication online; the four runtime enums
are known; missing fields do not establish standby; pump start/stop uses raw
values; existing links open new pages and have focus styling; narrow canvases can
clip labels. Reversible implementation details are delegated; no new status
aggregation has been accepted; no development document exists yet.

Observed: the reader selected specification, planning and documentation; directly
proposed preserving communication status, separate runtime labels, missing-value
placeholders, display-only rounding, focus/new-page behavior and clipping checks.
It stated “先把四项优化整理成可执行的开发文档，再核对执行条件，按你已有授权开启 Goal 并执行。”
It did not ask for a debate, fabricate an aggregation decision or start Goal
before the document/readiness work. This samples the Goal-follow-on discovery
case; it does not execute readiness or Goal tools.

**B.** User: “我建议用零功率表示离线。先写开发文档，暂不实施。” Facts: an online
device can be at zero power in standby; a reliable communication field exists;
the product has not accepted the proposed power-based rule; the document path is
known.

Observed: “零功率表示离线” was identified as misclassifying online standby. The
reader recommended the communication field, kept the replacement as a pending
document decision, continued independent drafting and planned one scoped choice
only for accepting the new product rule. It did not offer a separate debate or
infer implementation from documentation authority.

### Batch 2: preservation and non-interception

**A.** User: “这个显示规则上轮已确认：运行状态独立展示、在线状态照旧。只同步到开发文档。”
Facts: the same rule and document update were already accepted; no new conflict.
Observed: direct documentation synchronization, with no review or repeated
acceptance. This samples accepted-decision preservation.

**B.** User: “我建议把两个导航入口改为加下划线的文字链接，现在实现。” Facts: genuine
new-page navigation, supported style/accessibility, no state or interface delta,
and delegated local style/focus handling. Observed: `frontend-ui-engineering`
with an inline evidence check, then the bounded implementation and navigation/
keyboard verification. No invented objection, specification document or approval.

**C.** User: “我觉得把通信状态和运行状态合并成一个灯更简单。” Facts: the project
currently shows two independently varying dimensions; no direct task or review
consent. Observed: one neutral invitation, “这会影响项目的状态展示规则。要对这项建议做一次结合项目证据的辩证审查，并给出修订建议吗？”
The reader withheld substantive critique and awaited consent.

**D.** Same claim, but the user previously declined review of this exact item and
now only adds “我仍觉得这样更简洁。” Observed: acknowledgment without a renewed
offer, critique or inferred implementation authority. C/D check existing passive
consent and decline boundaries, not new cases.

**E.** User: “先挑出用零功率判离线这个建议的问题并修订，再把建议整理成开发文档，暂不实现。”
Facts: standby may have zero power; reliable communication data exists; the
replacement rule is not yet accepted; the document can contain pending choices.
Observed: explicit review followed by authorized documentation, with the revised
rule marked pending. No repeated review consent; only one scoped product-rule
choice after preparing the reviewable draft. This initial observation preceded
the final wording clarification; the final sample below directly exercises that
clarification with a settled product goal.

### Final sample: explicit review plus document authority

User: “先结合项目挑出我的导出方案中真正有问题的地方，修订后写入现有开发文档。我建议导出当前筛选的数据，但可以从加载到浏览器的所有行直接生成CSV。这次只评审和写文档，不实施。”
Facts: only filtered rows is an accepted goal; browser cache includes hidden rows;
an existing selector returns visible rows without changing product meaning,
interfaces or ownership; `docs/plan/export.md` is the authorized existing target.

Observed: the reader preserved browser-side CSV generation, identified the cached
hidden-row conflict and recommended the existing selector. It stated “评审结束后，直接转入已获授权的文档工作” and “无需再次确认评审或文档写入”.
It supplied acceptance examples and kept them as future implementation checks,
not claimed test results. Document completion ended the task without implementation
or a start offer. This directly samples
`explicit-proposal-review-and-documents-use-existing-authorization`.

## Static checks and limits

Commands were run from the repository root using existing `python3` with PyYAML.
The Skill/Plugin loop was:

```sh
rtk proxy sh -c 'set -eu; validation_python=python3; if [ -x .venv/bin/python ]; then validation_python=.venv/bin/python; fi; validation_system_skills="${CODEX_HOME:-$HOME/.codex}/skills/.system"; for validation_skill in plugins/my-agent-skills/skills/*/SKILL.md; do "$validation_python" "$validation_system_skills/skill-creator/scripts/quick_validate.py" "${validation_skill%/SKILL.md}"; done; "$validation_python" "$validation_system_skills/plugin-creator/scripts/validate_plugin.py" plugins/my-agent-skills'
```

- The loop follows [CONTRIBUTING.md](../../CONTRIBUTING.md#validation); all 27
  Skills and the plugin passed. The subsequently clarified dialectic entrypoint
  was checked again with the same quick validator.
- `rtk proxy python3 -`: inline checks parsed repository JSON/YAML (including the
  hidden marketplace), checked unique Skill IDs, unchanged frontmatter against
  `git show HEAD:<path>`, metadata budget, source descriptors, exact allowlists,
  40-character commit IDs, unique primary ownership, relative links, candidate
  anchor targets and plugin containment. It also scanned additions for unfinished
  placeholders, private paths and likely secret patterns; none found.
- A second `rtk proxy python3 -` compared every old case object with HEAD and
  checked unique IDs in the three affected suites: 56→60, 18→19, 30→33; all prior
  cases were unchanged.
- `rtk proxy git diff -- …` was used to read the runtime/document/eval changes;
  `rtk git diff --check` checked whitespace.

Discovery stays at 27 Skills and 6826 / 7000 name-and-description characters.
Source commits and artifact owners did not change; the descriptor records one
additional downstream adaptation. Historical eval results are untouched.

A separate fresh-context read-only reviewer examined the five Skill changes and
the eight added cases, finding no blocking or important issues in ownership,
consent, acceptance, follow-on authority or case scoring. That review did not
claim to run model regressions or audit report statistics.

The eight added YAML contracts were reviewed; the samples above cover selected
requests and boundary variants, not execution of all eight cases or the full
suite. No actual UI, document-generation integration, readiness/Goal lifecycle,
installed-plugin reload, repeated-run reliability or latency was measured.
Repository validation does not install or publish 6.1.0, and does not establish
that an already running chat uses the modified source.
