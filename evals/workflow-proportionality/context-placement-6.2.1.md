# 6.2.1 Context placement review

The change reconciles the imported `context-engineering` example with the newer
`documentation-and-adrs` convention owner. `AGENTS.md` remains the concise
always-on entrypoint; an existing project guide owns detailed development
conventions, and API or domain documents own public field behavior.

## Prompt footprint

| Runtime Skill | HEAD bytes | Revised bytes | Change |
|---|---:|---:|---:|
| `context-engineering/SKILL.md` | 13,684 | 13,559 | −125 |
| `documentation-and-adrs/SKILL.md` | 11,797 | 11,773 | −24 |

All 27 Skill names and descriptions remain unchanged: 6,826 raw characters
against the 7,000-character discovery budget. No Skill, runtime dependency,
hook, or tool was added. These are static context-size checks, not a latency
measurement or a guarantee about host-side Skill selection.

## Behavior review

Three new outcome cases in `cases.yaml` cover an existing guide, an explicit
request for a guide, and the original single-rule request without a guide.
Four independent, read-only next-action
probes used the revised Skill files with minimal scenario evidence:

- Existing guide: chose a concise guide entry and API/source links, then a
  short `AGENTS.md` pointer while retaining operating boundaries.
- No guide, explicit request: chose one project-placed guide, an `AGENTS.md`
  pointer, and API links without copying the public contract.
- No guide, single-rule request: kept `API.md` and tests as owners, chose at
  most a short `AGENTS.md` pointer, and did not create another guide.
- Existing rule with no new convention: chose no documentation change.

The probes test next-action decisions. They do not execute a full installed
plugin routing evaluation or prove future model behavior.

## Static validation

- Bundled quick validator passed for all 27 Skills; Plugin validator passed.
- Python parsed 20 repository JSON/YAML files, including the hidden marketplace
  manifest. The upstream registry check found one source and 31 allowlisted
  artifacts with unique ownership and valid 40-character commits.
- `git diff --check` passed. The new Skill example uses a project-relative
  guide link as an illustration and instructs agents to use actual project
  paths.
