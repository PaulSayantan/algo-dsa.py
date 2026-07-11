# `dsa` — practice-workspace toolkit

Turns the static problem corpus into a **runnable, self-verifying** practice
environment. It reads the existing 3-file contract
(`PROBLEM.md` / `solution.py` / `SOLUTION.md`) — no content regeneration.

## Install

```bash
pip install -e .            # runtime (PyYAML)
pip install -e ".[dev]"     # + pytest, hypothesis, ruff, black
```

Everything except the optional static-site/PBT extras runs on the Python
standard library (works on Python 3.10+).

## Use it

```bash
# Solve a problem, then grade your solution.py against its # expected: oracle:
dsa test problems/arrays/beginner/binary-search/problem-01-binary-search
dsa test --algo two-pointers-opposite-ends        # a whole algorithm
dsa test --category arrays --difficulty beginner  # a whole tier

# Or use pytest directly — one test per example case (stubs report as skips):
pytest problems/arrays/beginner/binary-search
pytest -k two-pointers

# Pick something to work on:
dsa next --category strings          # next unsolved problem
dsa random --difficulty intermediate
dsa show  <path>                     # print a PROBLEM.md

# Corpus stats and self-verification:
dsa stats
dsa verify --json build/verification_report.json
```

## How grading works

Each `solution.py` ends with an `if __name__ == "__main__":` block whose
`print(...)  # expected: <literal>` lines are a complete, aligned test oracle.
`dsa test` (and the pytest collector in `conftest.py`) parse those with
`ast` + `tokenize` into one `Case` per `print`, run your code, and compare with
float tolerance. One mechanism covers all three problem shapes:

- **`class Solution`** methods,
- **free functions**, and
- **stateful design classes** (`KthLargest`, `NumArray`, …) — the interleaved
  setup/`print` lines in `__main__` replay as an operation sequence, so state
  is rebuilt correctly for each case.

## `dsa verify` — content self-audit

For each problem, the reference implementation embedded in `SOLUTION.md`
(the ` ```python ` fence under the *Optimal* heading) is executed against the
same `# expected:` oracle. Statuses:

| status            | meaning |
|-------------------|---------|
| `ok`              | reference ran and matched every deterministic case |
| `unverifiable`    | reference snippet isn't executable as-is (prose/fragment/different API) |
| `nondeterministic`| all cases are random/any-valid-answer — nothing to assert |
| `no_reference`    | `SOLUTION.md` has no python fence |
| `content_bug`     | reference ran cleanly but disagreed with the oracle |

Current baseline: **605 ok, 220 unverifiable, 48 nondeterministic, 11
no_reference, 0 content_bug** across 884 problems — i.e. wherever both the
oracle and the reference are executable, they agree.

## Layout

```
dsa/
  parsing/
    solution_py.py   # __main__ -> Cases (ast + tokenize; handles all comment styles)
    problem_md.py    # PROBLEM.md metadata + ## Examples (function & op-sequence)
    solution_md.py   # extract the optimal reference code block
    literals.py      # literal parsing + float-tolerant / (deep) unordered equality
  model.py           # Case, Problem, CaseResult, ProblemResult
  discovery.py       # walk problems/, filter by category/algo/difficulty
  executor.py        # load a namespace, adapt interfaces, eval a case (stdout silenced)
  grader.py          # run cases -> results (with optional subprocess timeout)
  reference.py       # per-problem + whole-corpus self-verification
  cli.py             # the `dsa` command
conftest.py          # pytest: one test per case, collected from problems/
tests/test_toolkit.py# unit tests for the toolkit itself
```
