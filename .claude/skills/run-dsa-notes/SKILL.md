---
name: run-dsa-notes
description: Build, run, and drive the dsa practice-workspace toolkit. Use when asked to run dsa-notes, run the toolkit, grade a solution, run the tests, verify the corpus, smoke-test the grader, or check that the workspace works end-to-end.
---

The `dsa` toolkit turns the static problem corpus into a runnable, self-grading
practice environment. There is **no GUI and no server** — it is a CLI plus a
Python grading library. An agent drives it two ways: the read-only CLI
(`.venv/bin/python -m dsa.cli …`) and the smoke driver at
[.claude/skills/run-dsa-notes/driver.py](driver.py), which grades an in-memory
solution through the real sandbox (pass / fail / timeout) and runs the CLI
queries — no git side effects.

All paths below are relative to the repo root (`dsa-notes/`).

## Prerequisites

The repo ships a working virtualenv at `.venv/` (Python 3.14). **System `python3`
is 3.9 and has no pytest** — always use the venv interpreter. No `apt-get`/`brew`
step is needed on this machine; the venv already has the package installed
editable plus `pytest` and `ruff`.

Verify the environment in one line:

```bash
.venv/bin/python -c "import dsa, pytest; print('dsa+pytest OK', pytest.__version__)"
# → dsa+pytest OK 9.1.1
```

If `.venv/` is missing (fresh clone elsewhere), recreate it:

```bash
python3 -m venv .venv && .venv/bin/python -m pip install -e ".[dev]"
```

> Note: `.[dev]` lists `black` and `hypothesis`, but they are **not** installed in
> the shipped venv and nothing in the toolkit imports them. `ruff` and `pytest`
> are present and are all you need.

## Run (agent path) — the smoke driver

The primary handle. It grades a correct solution (must pass 3/3), a wrong one
(must fail), and a non-terminating one (timeout must fire), then runs the CLI
queries. Run it from the repo root with `PYTHONPATH` set to the root:

```bash
PYTHONPATH="$PWD" .venv/bin/python .claude/skills/run-dsa-notes/driver.py
```

Expected output (exit 0):

```
== grading harness ==
  [PASS] correct solution grades green — passed=3/3 load_error=None
  [PASS] wrong solution is caught — failed=2
  [PASS] infinite loop hits the timeout — load_error='timeout after 3.0s' elapsed=3.0s
== CLI (read-only) ==
  [PASS] dsa stats runs — Problems: 1380
  [PASS] dsa next resolves a problem
  [PASS] dsa list filters by id — 28 matches

DRIVER OK: every stage behaved as expected.
```

### Driving the CLI directly

The console script is **not** installed; invoke the module. These are read-only:

| command | what it does |
|---|---|
| `.venv/bin/python -m dsa.cli stats` | corpus + case counts (1380 problems / 4519 cases) |
| `.venv/bin/python -m dsa.cli list -k <substr>` | list problems whose id matches |
| `.venv/bin/python -m dsa.cli next --category strings` | next unsolved problem |
| `.venv/bin/python -m dsa.cli show <path>` | print a PROBLEM.md |
| `.venv/bin/python -m dsa.cli verify --algo <slug>` | self-audit references vs. oracle |

`dsa submit` **has a git side effect** (commits `solution.py` on pass, resets it
after 2 fails) — don't run it as a smoke test. Grade without side effects via
pytest or the driver instead.

## Grade real problems with pytest

`conftest.py` collects one test per `# expected:` case from every `solution.py`.
Stubs report as **skips**; implemented solutions pass/fail.

```bash
.venv/bin/python -m pytest problems/arrays/beginner/binary-search/problem-01-binary-search   # → 3 skipped (one stub, 3 cases)
.venv/bin/python -m pytest problems/arrays/beginner/binary-search   # whole technique → 19 skipped (6 stubs)
.venv/bin/python -m pytest -k "two-pointers"                        # by id substring
```

## Test (the toolkit's own unit tests)

```bash
.venv/bin/python -m pytest tests/ -q
# → 69 passed in ~13s
```

## Gotchas

- **The grader re-imports your script (spawn).** `grade_source_sandboxed` runs
  each solution in a `multiprocessing` *spawn* worker, which re-imports the
  calling module. Any script that calls it must keep all executable code under
  `if __name__ == "__main__":`, or the worker recurses →
  `RuntimeError: ... Safe importing of main module`. This is why the driver is a
  committed file, not a heredoc.
- **`python - <<'EOF'` cannot drive the grader.** A stdin heredoc has no
  importable path, so the spawn worker dies with
  `FileNotFoundError: '<stdin>'` / `ModuleNotFoundError: No module named 'dsa'`.
  Use a real file plus `PYTHONPATH="$PWD"`.
- **System Python ≠ venv Python.** `python3` here is 3.9 with no pytest; every
  command uses `.venv/bin/python`.
- **No sandbox beyond the timeout.** Graded code runs with full filesystem/
  network access; the only containment is the wall-clock timeout. Never grade
  code you have not read. See the `dsa-security-review` skill.

## Troubleshooting

- **`No module named dsa`** when running a script under `.venv/bin/python`: run
  from the repo root and prefix `PYTHONPATH="$PWD"` (the driver needs it; the
  `-m dsa.cli` form does not, since cwd is on the path).
- **`no result from worker`** from the grader: the worker crashed at import —
  almost always the spawn re-import trap above. Guard the module body.
- **pytest reports everything skipped**: expected for stub `solution.py` files.
  Implement the entrypoint (remove the `# TODO`/`pass`) to get real pass/fail.
