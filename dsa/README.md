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
standard library (works on Python 3.9+).

## Use it

```bash
# Solve a problem, then submit: grade solution.py against its # expected: oracle,
# and — only when every case passes — stage & commit that one solution.py.
dsa submit problems/arrays/beginner/binary-search/problem-01-binary-search
dsa submit -k binary-search                         # by id substring (must match one)

# Or use pytest directly for a no-commit dry run — one test per example case
# (stubs report as skips):
pytest problems/arrays/beginner/binary-search
pytest -k two-pointers

# Pick something to work on:
dsa next --category strings          # next unsolved problem
dsa random --difficulty intermediate
dsa show  <path>                     # print a PROBLEM.md

# Spaced revision:
dsa revisit -k binary-search      # mark a problem for revision + reset its solution.py
dsa revise arrays                    # print a random problem to re-solve from that category

# Corpus stats and self-verification:
dsa stats
dsa verify --json build/verification_report.json
```

## `dsa submit` — grade, then commit on green

`dsa submit <target>` resolves to **exactly one** problem (an ambiguous filter is
an error), grades its `solution.py`, and:

- **all cases pass** → stages and commits *only* that `solution.py`, with a
  message stamped with the submission date/time.
- **still a template** → refuses (a stub's cases only "pass" by being skipped).
- **implemented but every case is non-deterministic** → refuses (0 cases could
  be verified); pass `--allow-unverified` to commit it anyway, with an honest
  "unverified" commit message.
- **fails** → records the attempt. After **2** failed submits the problem is
  automatically added to the revision set and its `solution.py` is reset to the
  pristine template — nothing is committed. Marking resets the two-strike
  counter, so a freshly-reset problem gets a full new grace window.

A path/id target may point at the problem directory *or* its `solution.py`. A
target that matches several problems is an error (submit is a single-file commit).

## `dsa revise` / `dsa revisit` — spaced repetition

Revision state lives in `.dsa/revision.json` (git-ignored): a map of problem id →
`{added_at, reason, attempts}`.

- `dsa revisit <target>` marks one problem for revision and resets its
  `solution.py` back to the template so you can re-solve it from scratch.
- `dsa revise <category>` (`arrays`|`strings`|`matrix`|`paradigms`) prints a
  random problem currently marked for revision in that category; you then start
  the revision manually (e.g. `dsa show <path>`).

Resetting a `solution.py` restores the blob from the commit that first added it —
which in this corpus is the unimplemented template — so provided helper classes
and the `# expected:` oracle are preserved while your solution is discarded.

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
