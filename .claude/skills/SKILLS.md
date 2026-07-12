# Workspace skills

Project skills for the dsa-notes workspace, discovered automatically by Claude
Code from `.claude/skills/`. Each is invocable as a slash command (e.g.
`/run-dsa-notes`) and auto-loads when a request matches its description. Every
command in every SKILL.md was executed against this workspace before it was
written.

All skill commands assume the repo root as the working directory and the shipped
virtualenv interpreter `.venv/bin/python` (system `python3` is 3.9 and lacks the
deps; the venv is 3.14 with the package installed editable).

| Skill | Use it when you want to… | Committed harness |
|---|---|---|
| [run-dsa-notes](run-dsa-notes/SKILL.md) | Build, run, and smoke-test the toolkit end-to-end (grade pass/fail/timeout + CLI queries). | [driver.py](run-dsa-notes/driver.py) |
| [add-dsa-problem](add-dsa-problem/SKILL.md) | Add new problems/techniques via the `build/gen` spec → dry-run → emit → verify loop. | (uses `build/gen/run.py`) |
| [dsa-toolkit-dev](dsa-toolkit-dev/SKILL.md) | Change toolkit code (`dsa/`, `conftest.py`, `build/gen`) behind the test+lint gate. | (uses `tests/` + `driver.py`) |
| [dsa-security-review](dsa-security-review/SKILL.md) | Audit the arbitrary-code-execution surface, scan the corpus, check deps for CVEs. | [scan_corpus.py](dsa-security-review/scan_corpus.py) |

## Fast paths (copy-paste)

```bash
# Prove the whole toolkit works (no side effects):
PYTHONPATH="$PWD" .venv/bin/python .claude/skills/run-dsa-notes/driver.py

# Add problems: author build/gen/specs/<module>.py, then:
.venv/bin/python build/gen/run.py --dry-run <module>   # validate, write nothing
.venv/bin/python build/gen/run.py <module>             # emit the 3-file contract
.venv/bin/python -m dsa.cli verify --algo <slug>       # self-audit what you emitted

# Change toolkit code — the gate:
.venv/bin/python -m pytest tests/ -q                   # 69 passed
.venv/bin/ruff check dsa tests --select F,E9           # baseline: 2 known findings, add none

# Security review:
.venv/bin/python .claude/skills/dsa-security-review/scan_corpus.py   # 0 HIGH = clean
.venv/bin/python -m pip install -q pip-audit && .venv/bin/python -m pip_audit
```

## Cross-cutting facts every skill relies on

- **CLI invocation:** `.venv/bin/python -m dsa.cli <cmd>` — the `dsa` console
  script is not installed in the venv.
- **Grading is code execution.** The grader `exec`/`eval`s solutions in a
  `multiprocessing` *spawn* subprocess whose only containment is a wall-clock
  timeout — no FS/network sandbox. Any script that calls `grade_source_sandboxed`
  must keep its body under `if __name__ == "__main__":` (the worker re-imports the
  module) and run with `PYTHONPATH="$PWD"`; a `python - <<EOF` heredoc cannot
  drive it.
- **The 3-file contract** (`PROBLEM.md`/`solution.py`/`SOLUTION.md`) is derived
  data: grading comes from each `solution.py`'s `# expected:` oracle — never write
  per-problem test files. `problems/` is excluded from lint.
- **`build/` is gitignored** — the generator (`build/gen/`) and reports are
  local-only; commit generator changes with `git add -f` if you must keep them.

See also the repo-level [CLAUDE.md](../../CLAUDE.md) for architecture and the
canonical command list.
