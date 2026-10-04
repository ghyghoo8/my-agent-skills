# Business enum reuse — 6.2.3

On 2026-10-04 the accepted convention was added to code-simplification's
existing Reuse and Consolidation section: shared business enums, associated
types, labels and ordering have one domain/module-owned definition. Check
existing definitions before adding literals or maps; reuse them across the
affected consumers. Local-only values stay near their consumer, while matching
numeric codes do not merge different business meanings or dependency owners.

incremental-implementation already links to this section. The rule has one
runtime owner, without another Skill, global registry or duplicated rule text.
All 27 frontmatter descriptions, discovery cases and metadata budget are
unchanged. This clarifies existing semantic reuse without changing triggers,
routes, authorization or model policy, so it uses PATCH version 6.2.3.

Two workflow-proportionality cases cover shared enum/type/label/order reuse
and the local-value/distinct-meaning boundary. All 41 previous case objects
remain unchanged; the suite now has 43 cases. An independent agent reviewed
the placement and case boundaries.

## Targeted next-action probes

Two separate fresh-context agents received only the current reuse guidance,
necessary scope instructions and raw scenario evidence, without eval
expectations or prior conclusions. These standalone probes examine the same
rule boundaries as the new cases; they are not full executions of the YAML suite.

| Probe | Observed next action | Review |
|---|---|---|
| Existing report enum shared by preview/export | Reuse the owning definitions, associated type, labels and ordering; remove the in-scope obsolete map after checking consumers, preserve fallbacks and verify both outputs. | PASS |
| Component-only prompt and unrelated domains with identical numeric codes | Keep the prompt local; retain separate domain enums and reject a global registry or scope expansion. | PASS |

No business files, exports or external actions were executed. Agent model
settings were inherited; no independent effective-model receipt was available.
The probes do not prove full-suite or installed-plugin behavior.

## Validation

- `rtk proxy python3 /tmp/my-agent-skills-enums-6.2.3-validation.py` — PASS:
  27 bundled Skill quick validators, 20 repository JSON/YAML parses including
  hidden paths, 31 uniquely owned upstream artifacts with exact allowlists and
  40-character commit IDs, relative link targets, unchanged 6826/7000 discovery
  metadata, preserved existing cases/frontmatter/source pins/model policy,
  skills-only runtime and added-line hygiene.
- `rtk git diff --check` — PASS. The complete tracked diff and this new report
  were reviewed for scope and consistency.
- At the initial enum-rule review, the documented bundled Plugin validator was unavailable. Its
  `~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py` path is
  absent; focused system/bundled/primary-cache searches found no copy. It was
  not run, and the other static checks do not claim its result. No tooling was installed.

## Repository Plugin validator follow-up

The user subsequently authorized adding the Plugin validator. Maintenance code
now lives at [scripts/validate_plugin.py](../../scripts/validate_plugin.py),
outside the published plugin, with CLI tests at
[tests/test_validate_plugin.py](../../tests/test_validate_plugin.py).
[CONTRIBUTING.md](../../CONTRIBUTING.md#validation) now uses this repository
validator, removing the missing system Plugin validator prerequisite.

It checks readable, unambiguous manifest JSON, selected identity/listing fields,
SemVer, declared paths and asset files, direct Skill layout and the repository's
skills-only content boundary. It rejects symlinks, duplicate manifest authority,
runtime/dependency files and executable content. The implementation uses only
Python's standard library. It is not the official `plugin-creator` validator;
public-directory submission, Skill frontmatter and model behavior keep their
separate validation requirements. Runtime Skills and plugin version 6.2.3
are unchanged by this follow-up.

- `rtk proxy python3 -m unittest discover -s tests -p 'test_validate_plugin.py'`
  — PASS: 21 CLI tests, including valid packages, malformed/duplicate JSON,
  non-JSON numeric constants, SemVer variants, field types/limits, missing or
  escaping assets, symlinks and undeclared runtime files. Tests first failed
  before implementation. Independent review reproduced the numeric-constant
  loophole; its new test failed before the parser fix and passed afterward.
- `rtk proxy python3 scripts/validate_plugin.py plugins/my-agent-skills`
  — PASS for the current published bundle's manifest, resources, Skill layout
  and skills-only boundary.
- `rtk proxy python3 /tmp/my-agent-skills-enums-6.2.3-validation.py`
  — PASS after the follow-up: all 27 Skill quick validators, 20 JSON/YAML files,
  31 upstream artifacts, 124 relative links, preserved case/frontmatter/source
  invariants, discovery 6826/7000, runtime boundary and diff hygiene.
- `rtk git diff --check` — PASS. The complete changed and new files were reviewed.

The unavailable official system Plugin validator and public-directory submission
were not run; repository validator success does not claim either result.

No commit, push, plugin installation/cache update or global-rule edit was performed.
