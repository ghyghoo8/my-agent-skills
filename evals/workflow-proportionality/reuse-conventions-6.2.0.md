# Reuse and concise conventions — 6.2.0

Date: 2026-09-27. Baseline: `bf7bf4c` (6.1.0). The user accepted task-scoped
consolidation of repeated semantics, separate frequency/state handlers, concise
development conventions and code comments that carry local documentation. They
then explicitly requested a detailed iteration document followed by Goal execution.
The current task's plan and sole progress queue are in the workspace's
`.codex/agent-state/iteration-6.2.0.md`; task history is not plugin runtime content.

## Scope and contracts

Four existing Skills were updated. Simplification owns the semantic reuse check;
implementation and review link to it. Documentation owns the short division
between handler comments and persistent development conventions. A second
existing or planned implementation prompts the check; repeated calls to an
already shared helper do not. Matching semantics default to reuse/consolidation
within scope. Different concepts, meanings or dependency constraints justify
separate handlers. Necessary local extraction may accompany authorized work;
unrelated cleanup and architecture changes retain existing boundaries.

Handler comments explain local contracts, important rules, edge cases and
rationale. The existing guide links to those handlers and retains ownership,
entrypoints and cross-module constraints. Existing accurate conventions do not
need per-task additions. Project-designated business specifications remain
authoritative; neither comments nor a guide promote unaccepted decisions.

The additive scoped capability uses MINOR 6.2.0. All discovery descriptions,
authorization limits, architecture routes and runtime packaging boundaries are
unchanged. No new Skill, runtime reference, script, dependency or rule catalog
was introduced.

## Added behavior contracts

Discovery grows 60→62 and workflow proportionality 33→38. All 93 prior case
objects are unchanged. Historical results and the metadata baseline remain intact.

- `second-local-implementation-checks-existing-entry`
- `concise-convention-promotion-uses-existing-documentation-owner`
- `two-consumers-justify-one-scoped-rule`
- `similar-syntax-does-not-establish-shared-responsibility`
- `cabinet-status-and-frequency-have-separate-shared-handlers`
- `repeated-helper-calls-are-already-consolidated`
- `existing-convention-needs-no-per-task-appendix`

These cases assess actions, scope and semantic outcomes rather than fixed wording.

## Independent next-action sample

One fresh subagent context received three scenario requests and minimum project
facts, plus permission to read Skill metadata and selected instructions. It was
not given evals, diffs, history, other agent outputs or expected answers. The three
scenarios shared that reader context. No model/effort override was requested;
there was no independent effective-model receipt. The reader simulated replies
and next actions only, without editing a business project or calling live Goal.

**A — two responsibilities and concise persistence.** The request explicitly
required L2/L3 frequency ceiling, already accepted status priority, separate
frequency/state handlers, searchable comments and concise persisted conventions.
Facts: two matching local frequency implementations; existing numeric
compatibility/power-formatting and device-state modules; different device protocol
decoders; unchanged calculation values, module ownership, public interfaces and
dependencies; AGENTS already points to a development guide whose numeric section
and authoritative business specification exist; local semantic comments are missing.

Observed: the reader selected the direct UI workflow with scoped simplification
and documentation. It kept numeric formatting and device status in separate
existing owners, migrated affected consumers, removed only verified obsolete
duplicates, preserved raw calculation values and protocol differences, and planned
tests of both helper and consumers. It proposed searchable local comments plus
brief guide links, retaining the existing AGENTS pointer. No new approval or
architecture gate was introduced. Excerpt: “开发文档只记录职责、复用入口和限制，链接 handler 与现有业务规格。”

**B — similar syntax with different rules.** The user suggested reusing the pump
formatter for a second order-quantity display. Facts: pump display uses ceiling
and `--` for missing input; accepted order rules use round-to-nearest and an error
for missing input; the domains have incompatible dependency direction; an existing
order formatter is available and the user did not authorize changing its rules.

Observed: the reader explained those concrete differences, reused the order
entry, preserved its rounding/error contract and continued the authorized order
work. It planned distinguishing boundary tests and introduced neither a shared
mode-switching utility nor a cross-domain import. Excerpt: “沿用已有订单格式化入口，让第二处订单显示遵守已接受的订单规则。”

**C — already shared and documented.** The user asked to finish a change adding
a third consumer. Facts: one helper implementation, three consistent calls,
complete comments, accurate guide/AGENTS links, passed current checks, and no new
rule or defect. Observed: completion based on the existing evidence, with no
wrapper, new abstraction, comment/guide addition or repeated testing.

Main-thread assessment found these three observations consistent with the
sampled positive and negative boundaries. They are not execution of every new
YAML case, full-model business delivery, or a statistically repeated experiment.

A separate fresh-context read-only reviewer found no blocking defect in the four
Skills, seven added cases or iteration handoff. The review prompted an explicit
display-only rounding invariant in the frequency case, preserving the underlying
reading for calculations and start/stop decisions. One non-blocking coverage
limit remains: the current exception fixture combines semantic differences with
dependency conflicts; it does not independently establish behavior for matching
semantics blocked solely by dependency boundaries.

## Context size and verification

All 27 Skill frontmatters are unchanged: discovery remains **6826 / 7000** name
and description characters. Relative to HEAD, entrypoint body changes are:

| Skill | Character delta |
|---|---:|
| code-simplification | +1327 |
| documentation-and-adrs | +839 |
| incremental-implementation | +314 |
| code-review-and-quality | +171 |

Total added body text is 2651 characters, loaded with the applicable Skills.
Cross-skill links target the relevant sections. No latency, token-cost saving or
installed-session loading guarantee was measured. Detailed task and verification
records stay outside the plugin.

From the repository root, the validator loop documented in
[CONTRIBUTING.md](../../CONTRIBUTING.md#validation) was run with existing
`python3`/PyYAML via `rtk proxy sh -c`: all 27 Skill quick validators and the
Plugin validator passed. The exact executable loop is recorded in the iteration
document and the prior [6.1 verification](candidate-proposals-6.1.0.md#static-checks-and-limits).

`rtk proxy python3 -` ran read-only inline checks: all 7 repository JSON and 13
YAML files including the hidden marketplace parsed; unique Skill names and
unchanged discovery metadata passed; source descriptors, exact allowlists,
40-character commit IDs and 31 primary artifact owners passed; relative links,
new section anchors, plugin containment and absence of runtime scripts passed.
Old case objects were compared against `git show HEAD:<path>`. Added tracked and
untracked text was scanned for unfinished placeholders, private absolute paths
and likely secrets. `rtk git diff --check` passed. The complete diff and this new
report are reviewed as part of final reconciliation.

The Goal for this task is real and explicitly authorized; Goal actions were not
used to run simulations. Source completion does not publish/install the plugin
or establish that another active chat has loaded it. The full behavior suite,
actual cabinet UI implementation and runtime performance benchmark were not run.
