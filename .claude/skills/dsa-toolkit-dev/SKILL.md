---
name: dsa-toolkit-dev
description: Modify the dsa toolkit code (dsa/ package, conftest.py, build/gen) safely. Use when asked to change, fix, refactor, or add a feature to the toolkit/CLI/grader/parser, update dsa code, or work on anything under dsa/ — covers the test + lint gate and the regression baseline.
---

The toolkit is the Python under `dsa/` (parser → executor → grader → CLI),
`conftest.py` (the pytest collector), and `build/gen/` (the problem generator).
The **learner corpus under `problems/` is data, not toolkit code** — it is
excluded from lint and is only touched via the `add-dsa-problem` skill. This
skill is the verified change→test→lint loop for the toolkit itself.

All paths are relative to the repo root. Use `.venv/bin/python` (system `python3`
is 3.9; the venv is 3.14 with the package installed editable).

## The gate every change must pass

```bash
# 1. Toolkit unit tests — the real regression gate.
.venv/bin/python -m pytest tests/ -q
# → 69 passed in ~13s

# 2. A corpus smoke sample — proves grading still works against real content.
.venv/bin/python -m pytest problems/arrays/beginner/binary-search -q
# → 19 skipped  (6 stub solutions collect as skips, not failures)

# 3. The end-to-end driver — grade pass/fail/timeout + CLI queries in one shot.
PYTHONPATH="$PWD" .venv/bin/python .claude/skills/run-dsa-notes/driver.py
# → DRIVER OK: every stage behaved as expected.
```

If you changed parsing/grading, also spot-check the self-audit on a slice:

```bash
.venv/bin/python -m dsa.cli verify --algo binary-search
# → Verified 6 problems:  ok  6
```

## Lint — and the HONEST baseline

The repo config (`pyproject.toml`) selects `E,F,I,W,UP` at `target-version =
"py39"`. **`ruff check dsa tests` is NOT clean today** — it reports ~128
pre-existing findings, almost all `UP` (typing-modernization: `from __future__
import annotations` combined with `typing.List`/`Optional`, e.g.
[dsa/cli.py:27](../../../dsa/cli.py#L27)). Two are genuine pyflakes issues:

- `F841` unused local `joined` in [dsa/parsing/problem_md.py:180](../../../dsa/parsing/problem_md.py#L180)
- `F401` unused import `extract_cases` in `tests/test_toolkit.py:21`
- (`W291` trailing whitespace at [dsa/cli.py:59](../../../dsa/cli.py#L59))

**Do not "fix" the whole `UP` backlog as part of an unrelated change** — it's a
large, pre-existing, cosmetic diff that buries your real change. The honest gate
is **"introduce no new finding,"** not "zero findings" — even the real-bug rule
set is not clean today:

```bash
.venv/bin/ruff check dsa tests --select F,E9    # pyflakes + syntax errors
# → Found 2 errors  (the F841 + F401 above — the known baseline; add none beyond these)
```

After your edit, compare counts against that baseline (don't require zero):

```bash
.venv/bin/ruff check dsa tests --statistics
```

`black` is referenced in `pyproject.toml` but is **not installed** in the venv
and nothing needs it; don't try to run it.

## Architecture you must not break (contracts)

- **The 3-file contract is sacred.** Grading is *derived* from each
  `solution.py`'s `__main__` `print(...) # expected:` oracle — never write a
  per-problem test file. Parser: `dsa/parsing/solution_py.py`.
- **Three interface shapes, one grader.** `class Solution` methods, free
  functions, and stateful design classes (op-sequence replay). `dsa/executor.py`
  adapts all three; changes there must keep all three green (the unit tests cover
  each).
- **Grading runs in a spawn subprocess with a wall-clock timeout**
  (`grade_source_sandboxed`, `dsa/grader.py`). Anything you pass through the
  worker boundary must be picklable — `CaseResult.actual` is deliberately nulled
  before `q.put` because learner return values may be unpicklable. Keep that.
- **`dsa submit` is a single-file commit with real git side effects** (commits on
  pass; after 2 fails marks for revision and resets `solution.py` to its
  first-added blob via `dsa/vcs.py`). When touching `cli.py`/`vcs.py`/
  `revision.py`, test on a throwaway branch/commit and restore — never leave the
  tree or history dirty. (See `tests/test_submit_revise.py`, which uses temp git
  repos.)

## Verified restore recipe for testing `submit`

`submit` commits. To exercise it without polluting history:

```bash
ORIG=$(git rev-parse HEAD)
# ... implement a solution, run: dsa submit <path> ...
git reset --hard "$ORIG"            # drop the test commit
git checkout -- <path/to/solution.py>   # restore the stub
```

This exact recipe was used to verify the PASS→commit path and returned the repo
to `$ORIG` with the solution back to its template.

## Gotchas

- **Don't drive the grader from a heredoc.** `python - <<'EOF'` breaks the spawn
  worker (`FileNotFoundError: '<stdin>'`). Write a real file; guard its body
  under `if __name__ == "__main__":`; run with `PYTHONPATH="$PWD"`.
- **`build/` is gitignored — nothing under it is tracked** (verified:
  `git ls-files build/` is empty). `build/gen/` (the generator) and
  `build/verification_report.json` are local-only; edits there never show in
  `git status` and are **not** committed with your toolkit change. If a generator
  change must be preserved, `git add -f` it deliberately, or move it out of
  `build/`.
- **`tests/` is the source of truth**, not the corpus. A corpus problem can be
  legitimately `unverifiable`/`nondeterministic`; don't treat a non-`ok` verify
  status as a toolkit regression unless a *previously* `ok` problem flipped.

## Troubleshooting

- **A parsing change makes many problems `content_bug` in `dsa verify`**: you
  changed how the oracle or reference is extracted. Snapshot a baseline *before*
  editing (`dsa verify --json build/before.json`), then diff after — the current
  clean baseline is `605 ok / 220 unverifiable / 48 nondeterministic /
  11 no_reference / 0 content_bug` (per dsa/README.md); a jump in `content_bug`
  is your regression. (`build/verification_report.json` exists but is gitignored,
  so it is not a trustworthy committed baseline.)
- **`tests/` hangs**: a change removed the grading timeout. Grading must stay
  sandboxed (`grade_source_sandboxed`), or one bad solution wedges the suite.
