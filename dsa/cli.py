"""The ``dsa`` command-line interface.

Commands:
    dsa test [PATH|--algo A|--category C|-k SUBSTR]  grade solution.py vs its oracle
    dsa verify [--json OUT] [--only-bugs] [--advisories]  audit the corpus
    dsa stats                                        corpus/case counts
    dsa list  [filters]                              list matching problems
    dsa next  [filters]                              print a problem to work on
    dsa random [filters]                             print a random problem
    dsa show  PATH                                   print a problem's statement
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import List, Optional

from .discovery import find_problems, iter_problems, resolve, workspace_root
from .grader import grade_source
from .model import Problem
from .parsing.solution_py import extract_cases_from_file, is_stub

# --- shared filter args -----------------------------------------------------


def _add_filter_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--category", help="arrays | strings | matrix | paradigms")
    p.add_argument("--algo", help="algorithm slug (folder name)")
    p.add_argument("--difficulty", dest="tier", help="beginner | intermediate | advanced")
    p.add_argument("-k", dest="query", help="substring match on problem id")


def _filtered(args) -> List[Problem]:
    return find_problems(
        category=args.category,
        algorithm=args.algo,
        difficulty_tier=args.tier,
        query=args.query,
    )


# --- commands ---------------------------------------------------------------


def cmd_test(args) -> int:
    if args.path:
        problems = resolve(args.path)
    else:
        problems = _filtered(args)
    if not problems:
        print("no matching problems", file=sys.stderr)
        return 2

    total_pass = total_fail = total_skip = 0
    shown = 0
    for prob in problems:
        src = prob.solution_py.read_text(encoding="utf-8")
        result = grade_source(src, prob.id)
        total_pass += result.passed
        total_fail += result.failed
        total_skip += result.skipped

        if result.load_error:
            print(f"ERROR  {prob.id}: {result.load_error}")
            continue
        stub = is_stub(src)
        tag = "STUB " if stub else ("PASS " if result.ok else "FAIL ")
        # Only print per-problem lines when testing a small set or there are failures.
        if len(problems) <= 25 or not result.ok:
            print(f"{tag} {prob.id}  [{result.passed}/{len(result.results)} cases]")
            for cr in result.results:
                if cr.status in ("fail", "error"):
                    print(f"        case{cr.case.index}: {cr.detail}")
        shown += 1

    print(
        f"\nsummary: {total_pass} passed, {total_fail} failed, "
        f"{total_skip} skipped across {len(problems)} problem(s)"
    )
    return 0 if total_fail == 0 else 1


def cmd_verify(args) -> int:
    from .reference import verify_all

    root = workspace_root()
    problems = _filtered(args) if (args.category or args.algo or args.tier or args.query) else list(
        iter_problems(root)
    )

    from collections import Counter

    counts: Counter = Counter()
    records = []
    bugs = []
    for res in verify_all(problems, timeout=args.timeout, safe=args.safe):
        counts[res.status] += 1
        records.append(res.to_dict())
        if res.status == "content_bug":
            bugs.append(res)

    print(f"Verified {sum(counts.values())} problems:")
    for status, n in counts.most_common():
        print(f"  {status:16} {n}")

    if bugs and not args.only_bugs:
        print(f"\n{len(bugs)} content bug(s) (reference ran cleanly but disagreed with the oracle):")
    if bugs:
        for b in bugs:
            print(f"  {b.problem_id}\n     {b.detail}")

    if args.json:
        out = Path(args.json)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"counts": dict(counts), "problems": records}, indent=2))
        print(f"\nwrote report -> {out}")

    return 1 if counts.get("content_bug") else 0


def cmd_stats(args) -> int:
    from collections import Counter

    root = workspace_root()
    by_cat: Counter = Counter()
    by_tier: Counter = Counter()
    total_cases = 0
    n_det = n_nondet = 0
    n_problems = 0
    for prob in iter_problems(root):
        n_problems += 1
        by_cat[prob.category] += 1
        by_tier[prob.difficulty_tier or "(none)"] += 1
        try:
            cases = extract_cases_from_file(prob.solution_py)
        except Exception:  # noqa: BLE001
            continue
        total_cases += len(cases)
        n_det += sum(1 for c in cases if c.deterministic)
        n_nondet += sum(1 for c in cases if not c.deterministic)

    print(f"Problems: {n_problems}")
    print("  by category:", dict(by_cat))
    print("  by tier:    ", dict(by_tier))
    print(f"Cases: {total_cases} total  ({n_det} deterministic, {n_nondet} non-deterministic)")
    return 0


def cmd_list(args) -> int:
    for prob in _filtered(args):
        print(prob.id)
    return 0


def cmd_next(args) -> int:
    problems = _filtered(args)
    # Prefer a problem whose solution.py is still a stub (not yet attempted).
    for prob in problems:
        if is_stub(prob.solution_py.read_text(encoding="utf-8")):
            print(prob.id)
            print(f"  {prob.path}")
            return 0
    if problems:
        print(problems[0].id)
        print(f"  {problems[0].path}")
        return 0
    print("no matching problems", file=sys.stderr)
    return 2


def cmd_random(args) -> int:
    import random as _random

    problems = _filtered(args)
    if not problems:
        print("no matching problems", file=sys.stderr)
        return 2
    prob = _random.choice(problems)
    print(prob.id)
    print(f"  {prob.path}")
    return 0


def cmd_show(args) -> int:
    problems = resolve(args.path)
    if not problems:
        print("no matching problem", file=sys.stderr)
        return 2
    prob = problems[0]
    print(prob.problem_md.read_text(encoding="utf-8"))
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dsa", description="DSA practice workspace toolkit")
    sub = p.add_subparsers(dest="command", required=True)

    t = sub.add_parser("test", help="grade solution.py against its # expected: oracle")
    t.add_argument("path", nargs="?", help="problem path or id substring")
    _add_filter_args(t)
    t.set_defaults(func=cmd_test)

    v = sub.add_parser("verify", help="self-verify the corpus using SOLUTION.md references")
    _add_filter_args(v)
    v.add_argument("--json", help="write full JSON report to this path")
    v.add_argument("--only-bugs", action="store_true", help="print only content bugs")
    v.add_argument("--advisories", action="store_true", help="include advisory checks")
    v.add_argument("--safe", action="store_true", help="isolate each problem in a subprocess")
    v.add_argument("--timeout", type=float, default=10.0, help="per-problem timeout (with --safe)")
    v.set_defaults(func=cmd_verify)

    s = sub.add_parser("stats", help="show corpus and case statistics")
    s.set_defaults(func=cmd_stats)

    ls = sub.add_parser("list", help="list matching problems")
    _add_filter_args(ls)
    ls.set_defaults(func=cmd_list)

    nx = sub.add_parser("next", help="print the next unsolved problem")
    _add_filter_args(nx)
    nx.set_defaults(func=cmd_next)

    rd = sub.add_parser("random", help="print a random matching problem")
    _add_filter_args(rd)
    rd.set_defaults(func=cmd_random)

    sh = sub.add_parser("show", help="print a problem's PROBLEM.md")
    sh.add_argument("path", help="problem path or id substring")
    sh.set_defaults(func=cmd_show)

    return p


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
