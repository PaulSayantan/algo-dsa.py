"""The ``dsa`` command-line interface.

Commands:
    dsa submit [PATH|--algo A|--category C|-k SUBSTR]  grade solution.py; commit on pass
    dsa revise CATEGORY                              pick a random problem to revise
    dsa revisit [PATH|filters]                    mark a problem for revision + reset it
    dsa verify [--json OUT] [--only-bugs] [--advisories]  audit the corpus
    dsa stats                                        corpus/case counts
    dsa list  [filters]                              list matching problems
    dsa next  [filters]                              print a problem to work on
    dsa random [filters]                             print a random problem
    dsa show  PATH                                   print a problem's statement

``submit`` is the grader-with-side-effects: when every case passes it stages and
commits that single ``solution.py`` (message stamped with the submission time).
When a solution fails twice in a row it is auto-added to the revision set and
reset to its pristine template. ``revise`` / ``revisit`` manage that set.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Optional

from . import revision, vcs
from .discovery import find_problems, iter_problems, resolve, workspace_root
from .grader import grade_source_sandboxed
from .model import Problem
from .parsing.solution_py import extract_cases_from_file, is_stub

# Failed submits allowed before a problem is auto-marked for revision and reset.
_MAX_FAILED_ATTEMPTS = 2

# Accepted category spellings (singular forms map to the on-disk plural folder).
_CATEGORIES = {"arrays", "strings", "matrix", "paradigms", "hashing", "stacks", "queues", "deques"}
_CATEGORY_ALIASES = {
    "array": "arrays",
    "string": "strings",
    "matrices": "matrix",
    "paradigm": "paradigms",
    "hashmap": "hashing",
    "hashmaps": "hashing",
    "hashset": "hashing",
    "hash": "hashing",
    "stack": "stacks",
    "queue": "queues",
    "deque": "deques"
}

# --- shared filter args -----------------------------------------------------


def _add_filter_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--category", help="arrays | strings | matrix | paradigms | hashing | stacks | queues | deques")
    p.add_argument("--algo", help="algorithm slug (folder name)") 
    p.add_argument("--difficulty", dest="tier", help="beginner | intermediate | advanced")
    p.add_argument("-k", dest="query", help="substring match on problem id")


def _filtered(args) -> List[Problem]:
    # Honor the same singular/plural category aliases the `revise` command accepts
    # (e.g. --category array -> arrays); an unrecognized value passes through
    # unchanged so it simply matches nothing, as before.
    category = args.category
    if category:
        category = _canonical_category(category) or category
    return find_problems(
        category=category,
        algorithm=args.algo,
        difficulty_tier=args.tier,
        query=args.query,
    )


# --- commands ---------------------------------------------------------------


def _resolve_single(args) -> Optional[Problem]:
    """Resolve a submit/revisit target to exactly one problem, or print why not.

    A submit is a deliberate per-solution commit, so an ambiguous target (a filter
    or path matching several problems) is treated as an error rather than silently
    picking one or committing many.
    """
    problems = resolve(args.path) if args.path else _filtered(args)
    if not problems:
        print("no matching problems", file=sys.stderr)
        return None
    if len(problems) > 1:
        print(
            f"target matches {len(problems)} problems; narrow to exactly one "
            "(pass a specific path/id):",
            file=sys.stderr,
        )
        for prob in problems[:10]:
            print(f"  {prob.id}", file=sys.stderr)
        if len(problems) > 10:
            print(f"  ... and {len(problems) - 10} more", file=sys.stderr)
        return None
    return problems[0]


def _print_failures(result) -> None:
    for cr in result.results:
        if cr.status in ("fail", "error"):
            print(f"        case{cr.case.index}: {cr.detail}")


def cmd_submit(args) -> int:
    prob = _resolve_single(args)
    if prob is None:
        return 2

    root = workspace_root()
    if not vcs.is_git_repo(root):
        print("submit requires a git repository (none found)", file=sys.stderr)
        return 2

    src = prob.solution_py.read_text(encoding="utf-8")

    # A pristine/stub solution has nothing to submit: its cases "pass" only by
    # being skipped, so guard against committing an unimplemented template.
    if is_stub(src):
        print(f"STUB  {prob.id}  — nothing to submit (solution.py is still a template)")
        return 2

    # Grade in a subprocess with a wall-clock timeout so an infinite loop or hang in
    # the learner's solution surfaces as a clean "timeout" load_error rather than
    # wedging the CLI forever (a common bug: a loop whose bound never advances).
    result = grade_source_sandboxed(src, prob.id, timeout=args.timeout)
    if result.load_error:
        print(f"ERROR  {prob.id}: {result.load_error}")
        return 1

    if result.ok:
        # `result.ok` is "nothing failed" — but a solution whose cases are ALL
        # non-deterministic (skipped) has passed 0 verifiable cases, so committing
        # it would claim "passing" for work nothing actually checked. Require an
        # explicit opt-in for that; a genuine pass (>=1 deterministic case passed)
        # commits normally.
        verified = result.passed > 0
        if not verified and not getattr(args, "allow_unverified", False):
            print(
                f"UNVERIFIED  {prob.id}  — all {result.skipped} case(s) are "
                "non-deterministic; nothing could be checked."
            )
            print("  not committed. Re-run with --allow-unverified to submit anyway.")
            return 2

        # A passing submit graduates the problem: drop it from the revision set
        # entirely (whether it was there for revision or just holding a pending
        # failed-attempt counter) so `dsa revise` won't resurface a solved one.
        graduated = revision.unmark(prob.id, root)
        tag = "PASS" if verified else "PASS (unverified)"
        print(f"{tag}  {prob.id}  [{result.passed}/{len(result.results)} cases]")
        if graduated:
            print("  cleared from the revision set.")
        stamp = datetime.now().replace(microsecond=0)
        verdict = (
            f"{result.passed} case(s) passing."
            if verified
            else f"unverified — {result.skipped} non-deterministic case(s), nothing to assert."
        )
        message = (
            f"Solve {prob.id}\n\n"
            f"Submitted {stamp.isoformat(sep=' ')} — {verdict}"
        )
        try:
            sha = vcs.commit_path(root, prob.solution_py, message)
        except vcs.GitError as e:
            print(f"  commit failed: {e}", file=sys.stderr)
            return 1
        if sha:
            print(f"  committed {sha[:9]}  {prob.solution_py.relative_to(root)}")
        else:
            print("  already committed (no changes to solution.py)")
        return 0

    # Failing submit.
    print(f"FAIL  {prob.id}  [{result.passed}/{len(result.results)} cases]")
    _print_failures(result)
    attempts = revision.record_failed_attempt(prob.id, root=root)
    if attempts >= _MAX_FAILED_ATTEMPTS:
        revision.mark(prob.id, reason="failed-submit", root=root)
        try:
            revision.reset_solution(prob.solution_py, root)
        except revision.ResetError as e:
            print(f"  (could not reset solution: {e})", file=sys.stderr)
        else:
            print(
                f"\n  failed {attempts}x — marked for revision and reset "
                f"{prob.solution_py.relative_to(root)} to its template."
            )
    else:
        remaining = _MAX_FAILED_ATTEMPTS - attempts
        print(f"\n  attempt {attempts}/{_MAX_FAILED_ATTEMPTS}; "
              f"{remaining} more failure(s) will reset it for revision.")
    return 1


def _canonical_category(arg: str) -> Optional[str]:
    """Map a user-supplied category argument to its on-disk folder, or ``None``."""
    key = arg.strip().lower()
    if key in _CATEGORIES:
        return key
    return _CATEGORY_ALIASES.get(key)


def cmd_revise(args) -> int:
    import random as _random

    category = _canonical_category(args.category)
    if category is None:
        print(
            f"unknown category {args.category!r}; expected one of: "
            f"{', '.join(sorted(_CATEGORIES))}",
            file=sys.stderr,
        )
        return 2

    root = workspace_root()
    marked = revision.list_marked(root)
    # Only surface genuinely-marked problems (skip the internal 'pending' entries
    # that merely hold a failed-attempt counter) that belong to this category.
    candidates = [
        pid
        for pid, entry in marked.items()
        if entry.get("reason") != "pending" and pid.split("/", 1)[0] == category
    ]
    if not candidates:
        print(f"no problems marked for revision in category {category!r}")
        return 0

    pid = _random.choice(sorted(candidates))
    entry = marked[pid]
    prob = _first_problem_by_id(pid, root)
    print(pid)
    if prob is not None:
        print(f"  {prob.path}")
    print(f"  added for revision: {entry.get('added_at', '?')}  ({entry.get('reason', '?')})")
    return 0


def _first_problem_by_id(problem_id: str, root: Path) -> Optional[Problem]:
    for prob in iter_problems(root):
        if prob.id == problem_id:
            return prob
    return None


def cmd_revise_add(args) -> int:
    prob = _resolve_single(args)
    if prob is None:
        return 2

    root = workspace_root()
    if not vcs.is_git_repo(root):
        print("revisit requires a git repository (none found)", file=sys.stderr)
        return 2

    already = revision.is_marked(prob.id, root) and revision.load(root)["problems"][
        prob.id
    ].get("reason") != "pending"
    revision.mark(prob.id, reason="manual", root=root)
    verb = "already marked; refreshed" if already else "marked"
    print(f"{verb} for revision: {prob.id}")

    # Reset solution.py back to its pristine template so revision starts clean.
    try:
        revision.reset_solution(prob.solution_py, root)
    except revision.ResetError as e:
        print(f"  (could not reset solution: {e})", file=sys.stderr)
        return 1
    print(f"  reset {prob.solution_py.relative_to(root)} to its template.")
    return 0


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

    # Honor --advisories: surface the PROBLEM.md-vs-expected cross-check (an advisory
    # signal that otherwise only lands in the --json report). Without this the flag
    # was a silent no-op that produced identical output.
    if args.advisories and not args.only_bugs:
        advisories = [
            r for r in records if str(r.get("expected_vs_problem", "")).startswith("fail")
        ]
        if advisories:
            print(f"\n{len(advisories)} advisory mismatch(es) (PROBLEM.md Output vs expected):")
            for r in advisories:
                print(f"  {r['problem_id']}\n     {r['expected_vs_problem']}")

    if args.json:
        out = Path(args.json)
        # Report a write failure cleanly instead of dumping a raw traceback after the
        # (already-printed) verification results, which would also discard the exit code.
        try:
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(json.dumps({"counts": dict(counts), "problems": records}, indent=2))
        except OSError as e:
            print(f"could not write report to {out}: {e}", file=sys.stderr)
            return 1
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
    # Problems are discovered by their solution.py, so PROBLEM.md is not guaranteed to
    # exist (or be UTF-8). Guard the read and report cleanly instead of crashing with a
    # raw traceback and a non-contract exit code.
    try:
        print(prob.problem_md.read_text(encoding="utf-8"))
    except OSError as e:
        print(f"cannot read {prob.problem_md}: {e}", file=sys.stderr)
        return 2
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dsa", description="DSA practice workspace toolkit")
    sub = p.add_subparsers(dest="command", required=True)

    sb = sub.add_parser(
        "submit",
        help="grade solution.py; commit it on pass (auto-revise+reset after 2 fails)",
    )
    sb.add_argument("path", nargs="?", help="problem path or id substring")
    sb.add_argument(
        "--allow-unverified",
        action="store_true",
        help="commit even when every case is non-deterministic (nothing to assert)",
    )
    sb.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="per-submission grading timeout in seconds (guards against infinite loops)",
    )
    _add_filter_args(sb)
    sb.set_defaults(func=cmd_submit)

    rv = sub.add_parser(
        "revise",
        help="pick a random problem marked for revision in a category",
    )
    rv.add_argument("category", help="arrays | strings | matrix | paradigms | hashing")
    rv.set_defaults(func=cmd_revise)

    ra = sub.add_parser(
        "revisit",
        help="mark a problem for revision and reset its solution.py to the template",
    )
    ra.add_argument("path", nargs="?", help="problem path or id substring")
    _add_filter_args(ra)
    ra.set_defaults(func=cmd_revise_add)

    v = sub.add_parser("verify", help="self-verify the corpus using SOLUTION.md references")
    _add_filter_args(v)
    v.add_argument("--json", help="write full JSON report to this path")
    v.add_argument("--only-bugs", action="store_true", help="print only content bugs")
    v.add_argument("--advisories", action="store_true", help="include advisory checks")
    # Subprocess isolation is ON by default so one hanging reference can't wedge the
    # whole scan; --no-safe opts into the faster in-process path. --safe is kept as a
    # no-op alias for backward compatibility.
    v.add_argument(
        "--no-safe",
        dest="safe",
        action="store_false",
        help="run in-process (faster) instead of isolating each problem in a subprocess",
    )
    v.add_argument("--safe", dest="safe", action="store_true", help=argparse.SUPPRESS)
    v.set_defaults(safe=True)
    v.add_argument("--timeout", type=float, default=10.0, help="per-problem timeout when isolated")
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
    try:
        return args.func(args)
    except KeyboardInterrupt:
        # A Ctrl-C during a long verify/submit should abort cleanly, not dump a stack
        # trace. 130 is the conventional SIGINT exit code.
        print("\ninterrupted", file=sys.stderr)
        return 130
    except Exception as e:  # noqa: BLE001 - last-resort guard: no raw traceback to users
        print(f"dsa: {type(e).__name__}: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
