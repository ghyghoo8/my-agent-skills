# Sol model update — 6.2.2

On 2026-09-30 the user requested only `gpt-6-sol` → `gpt-6.1-sol`.
The milestone controller and Sol workers now use that model ID. All reasoning
efforts, role ownership, Luna/Astra settings, consultation limits, authorization,
host-support checks and explicit user locks retain their previous semantics.
No trigger, route, pause or output contract changes; this uses a PATCH version.

The planning Skill, milestone reference, current README/eval guidance and
downstream adaptation agree. Live planning/discovery/proportionality fixtures
use the new default and identify plugin 6.2.2. Case IDs and counts remain
65/62/41. The explicit-user-lock case deliberately retains `gpt-6-sol` to check
that a selected older model is not overwritten by the new default. Frozen
historical reports, receipts, results and source commit pins remain unchanged.

## Targeted behavior review

Two separate agents received only the current planning Skill and milestone
reference plus one request and its minimum raw project evidence, without eval
expectations or prior conclusions. Each performed a read-only next-action
simulation; hypothetical host facts were not operated against a live project.

| Case | Observed response | Review |
|---|---|---|
| `controller-ultra-selects-fit-child-models` | Kept `gpt-6.1-sol ultra` control, selected supported task-fit Sol efforts, bounded Luna work and fresh-context Sol review; Astra remained one conditional read-only consultation. Recommendations did not activate execution. | PASS |
| `unsupported-sol-settings-block-execution-not-authorized-planning` | Continued authorized plan/queue preparation, blocked target-host integration without a suitable Sol setting, and rejected Luna/Astra substitution and effort-label equivalence. | PASS |

These two probes do not establish full-suite, installed-plugin, comparative
quality, latency or cost results. No model override was requested for the
review agents and no independent effective-model receipt was available;
this is not a verified GPT-6.1 Sol runtime benchmark.

## Static validation

Commands ran from the repository root:

- `rtk proxy python3 /tmp/my-agent-skills-6.2.2-validation.py` — PASS. The
  temporary checker invoked the bundled Skill quick validator for all 27
  Skills; parsed 20 tracked JSON/YAML files including hidden marketplace and
  historical result files; checked 31 uniquely owned upstream artifacts,
  exact allowlists and 40-character commit IDs; resolved relative Markdown
  link targets; confirmed unchanged discovery metadata at 6826/7000; compared
  runtime/document diffs and parsed eval objects against the previous commit
  to verify only the requested model and version substitutions; checked new
  lines for unfinished placeholders, private paths and likely secrets, and
  confirmed historical evidence and the skills-only runtime were unchanged.
- `rtk git diff --check` — PASS.
- `rtk proxy git diff` plus review of this newly added report — no unrelated
  changes found. A separate agent also reviewed the model-policy diff.

The bundled Plugin validator could not run: its documented
`~/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py` is absent,
and focused searches in the system Skills and bundled/primary plugin caches
found no copy. The custom manifest/inventory checks above are separate static
checks, not a claimed substitute pass for that validator. No tools were installed.

No live milestone execution, model switch, plugin installation/cache update,
commit, push or publication was performed.
