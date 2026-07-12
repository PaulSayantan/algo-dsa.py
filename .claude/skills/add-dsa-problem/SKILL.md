---
name: add-dsa-problem
description: Add new DSA practice problems to this workspace via the build/gen generator. Use when asked to add a problem, add problems, author a new technique, create problem folders, generate the 3-file contract (PROBLEM.md/solution.py/SOLUTION.md), or bulk-add DSA content.
---

Problems are **never hand-written folder-by-folder.** You author a Python *spec
module* under `build/gen/specs/<module>.py` declaring `TECHNIQUES = [...]`; the
generator renders each spec into the repo's 3-file contract and **captures the
`# expected:` oracle by running your reference implementation** — so reference
and oracle agree by construction. The full authoring contract lives in
[build/gen/AUTHORING_GUIDE.md](../../../build/gen/AUTHORING_GUIDE.md); this skill
is the verified run-loop around it.

All paths are relative to the repo root (`dsa-notes/`). Use `.venv/bin/python`
(system `python3` is 3.9 and lacks the deps).

## The loop (dry-run until clean, then emit)

1. **Copy the canonical template.** `build/gen/specs/stacks_beginner.py` shows
   both problem shapes (a `Solution`-method problem and a stateful design class).
   Start from it. Data model and hard rules: see the AUTHORING_GUIDE.

2. **Dry-run** — validates every reference against your independent
   `expected_check`, confirms stubs are detected as stubs, writes nothing:

   ```bash
   .venv/bin/python build/gen/run.py --dry-run <module>
   ```

   Iterate until it prints exactly:

   ```
   All references captured cleanly; all stubs detected as stubs.
   ```

   with `0 ERROR(S)`. A non-zero exit means a reference threw, disagreed with
   your `expected_check`, produced a non-round-trippable value, or a stub had a
   too-filled-in body.

3. **Emit for real** (writes `problems/<cat>/<tier>/<slug>/…`):

   ```bash
   .venv/bin/python build/gen/run.py <module>
   ```

4. **Verify the emitted problems** — the reference-vs-oracle self-audit:

   ```bash
   .venv/bin/python -m dsa.cli verify --algo <technique-slug>
   # → Verified N problems:  ok  N
   ```

5. **Confirm the learner path grades** — a fresh stub must collect as *skips*
   (never fails):

   ```bash
   .venv/bin/python -m pytest problems/<cat>/<tier>/<slug> -q
   # → all skipped (stub not implemented)
   ```

6. **Regenerate the README tables** (counts problem-* folders from disk):

   ```bash
   .venv/bin/python build/gen/readme_section.py
   # → wrote build/gen/readme_section.md   (paste the relevant section into README.md)
   ```

This exact loop was run end-to-end while authoring this skill: a throwaway
`arrays/beginner` technique dry-ran clean, emitted its 3 files, captured
`# expected: 6` / `# expected: 0`, and verified `ok 1`.

## Minimal working spec (verified — dry-runs clean and emits)

Save as `build/gen/specs/<yourname>.py`. **Do not** start the module name with
`_` — `run.py` skips `_`-prefixed modules (`m.name.startswith("_")`).

```python
"""Throwaway example spec."""
from generator import Example, ProblemSpec, TechniqueSpec

TECHNIQUES = [
    TechniqueSpec(
        category="arrays", tier="beginner", slug="sum-a-list",
        title="Sum a List",
        blurb="Fold a list to a scalar — the simplest reduction pattern.",
        problems=[
            ProblemSpec(
                slug="problem-01-sum-list", title="Sum a List", difficulty="Easy",
                source="Classic — Sum",
                description="Return the sum of a list of integers.",
                hint="Accumulate with addition.",
                stub=(
                    "from typing import List\n\n\n"
                    "class Solution:\n"
                    "    def total(self, nums: List[int]) -> int:\n"
                    "        # TODO: implement\n"
                    "        pass\n"
                ),
                reference=(
                    "from typing import List\n\n\n"
                    "class Solution:\n"
                    "    def total(self, nums: List[int]) -> int:\n"
                    "        return sum(nums)\n"
                ),
                main_lines=[
                    "sol = Solution()",
                    "print(sol.total([1, 2, 3]))",
                    "print(sol.total([]))",
                ],
                expected_check=[6, 0],   # YOUR independent answer, one per print()
                examples=[Example(input="[1, 2, 3]", output="6")],
            ),
        ],
    )
]
```

## Gotchas (learned by running the generator)

- **Module name can't start with `_`.** `run.py` silently skips it, so
  `--dry-run` reports `0 techniques` and nothing emits. Name it `myspec.py`, not
  `_myspec.py`. (The technique *slug* can be anything, e.g. `zzz-smoke-demo`.)
- **`expected_check` must be YOUR independent value, not copied from the
  reference.** It is the non-circular cross-check: the generator asserts the
  reference's captured output equals it, so a wrong reference is caught. Length
  must equal the number of `print(...)` lines.
- **The reference runs under an auto-injected preamble.** `typing.*`, `heapq`,
  `math`, `bisect`, `collections`, `itertools`, `functools`, `re`, `random`,
  `sys`, and the common `collections`/`functools` names are already imported —
  don't re-import them in the `reference` (you may in the `stub` for the learner).
- **stub body must be genuinely empty** (`pass`/`...`/docstring/`# TODO`/
  `raise NotImplementedError`) or `is_stub` won't detect it and pytest will
  *fail* the case instead of skipping it. Filled-in helper classes (a `ListNode`)
  are fine — only the *entry method the cases call* must be empty.
- **Outputs must be deterministic, round-trippable literals.** If an algorithm
  admits several valid answers, return a scalar (length/cost/count/bool), not the
  path itself. `inf`/`nan`/custom objects fail the round-trip guard.
- **Emitting is not committed automatically.** After `run.py <module>`, the new
  files are untracked. Commit them yourself (or grade+`dsa submit` a solved one).

## Troubleshooting

- **`--dry-run` says `Total: 0 techniques from 0 module(s)`**: module name starts
  with `_`, or the file has no top-level `TECHNIQUES` list. Rename / fix.
- **`reference capture failed: ...`**: the reference threw or disagreed with
  `expected_check`. The message names the case index and both values — fix the
  reference or your expected value.
- **`stub NOT detected as a stub (body too filled-in)`**: the entry method has
  real logic. Reduce it to `pass`.
