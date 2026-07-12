#!/usr/bin/env python3
"""Smoke driver for the dsa toolkit — drives the *running* toolkit end-to-end.

This is the harness the run-dsa-notes skill points at. It exercises the toolkit
the same way `dsa submit` / `conftest.py` do, but with no git side effects: it
grades an in-memory correct solution (must pass), a wrong one (must fail), and a
non-terminating one (timeout must fire), then runs the read-only CLI queries.

IMPORTANT — spawn safety: `grade_source_sandboxed` runs each solution in a
`multiprocessing` *spawn* worker, which re-imports this module. All executable
statements therefore live under `if __name__ == "__main__":` (module import must
be side-effect free) or the worker recurses and dies with a
"Safe importing of main module" RuntimeError. This trap is why the driver exists
as a file rather than a `python - <<EOF` heredoc (a heredoc has no importable
module path and fails with FileNotFoundError: '<stdin>').

Run it from the repo root:

    PYTHONPATH="$PWD" .venv/bin/python .claude/skills/run-dsa-notes/driver.py

Exit code 0 = every stage behaved as expected; non-zero = a stage regressed.
"""
from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# A correct binary-search solution + the exact `# expected:` oracle its stub ships.
GOOD = '''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))  # expected: 4
    print(sol.search([-1, 0, 3, 5, 9, 12], 2))  # expected: -1
    print(sol.search([5], 5))                    # expected: 0
'''

# Same oracle, off-by-one body: every case must now fail.
BAD = GOOD.replace("return mid\n", "return mid + 1\n")

# Never terminates: the subprocess wall-clock timeout must kill it.
LOOP = '''
class Solution:
    def run(self):
        while True:
            pass
if __name__ == "__main__":
    print(Solution().run())  # expected: 1
'''


def _cli(*args: str) -> subprocess.CompletedProcess:
    """Invoke the dsa CLI as a module (the console script isn't installed)."""
    return subprocess.run(
        [sys.executable, "-m", "dsa.cli", *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )


def main() -> int:
    from dsa.grader import grade_source_sandboxed

    failures: list[str] = []

    def check(label: str, ok: bool, detail: str = "") -> None:
        print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))
        if not ok:
            failures.append(label)

    print("== grading harness ==")
    g = grade_source_sandboxed(GOOD, "smoke/good", timeout=10.0)
    check("correct solution grades green", g.ok and g.passed == 3,
          f"passed={g.passed}/{len(g.results)} load_error={g.load_error}")

    b = grade_source_sandboxed(BAD, "smoke/bad", timeout=10.0)
    nfail = sum(1 for r in b.results if r.status in ("fail", "error"))
    check("wrong solution is caught", (not b.ok) and nfail > 0, f"failed={nfail}")

    t0 = time.time()
    lp = grade_source_sandboxed(LOOP, "smoke/loop", timeout=3.0)
    elapsed = time.time() - t0
    check("infinite loop hits the timeout",
          lp.load_error is not None and "timeout" in lp.load_error and elapsed < 8,
          f"load_error={lp.load_error!r} elapsed={elapsed:.1f}s")

    print("== CLI (read-only) ==")
    s = _cli("stats")
    check("dsa stats runs", s.returncode == 0 and "Problems:" in s.stdout,
          s.stdout.strip().splitlines()[0] if s.stdout.strip() else s.stderr.strip())

    n = _cli("next", "--category", "strings")
    check("dsa next resolves a problem", n.returncode == 0 and "strings/" in n.stdout)

    ls = _cli("list", "-k", "binary-search")
    check("dsa list filters by id", ls.returncode == 0 and "binary-search" in ls.stdout,
          f"{len(ls.stdout.strip().splitlines())} matches")

    print()
    if failures:
        print(f"DRIVER FAILED: {len(failures)} stage(s): {', '.join(failures)}")
        return 1
    print("DRIVER OK: every stage behaved as expected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
