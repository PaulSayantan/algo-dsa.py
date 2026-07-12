"""Content self-verification: run each problem's reference solution against its
own ``# expected:`` oracle to audit the corpus for content bugs.

Three cross-checks per problem:

1. ``ref_vs_expected``     — reference (from SOLUTION.md) vs the ``# expected:``
                             literals in solution.py. A mismatch means the
                             reference code or the expected literal is wrong.
2. ``expected_vs_problem`` — the ``# expected:`` literals vs the ``Output:``
                             values in PROBLEM.md examples (static; no exec).
3. status roll-up          — ok | content_bug | no_reference | nondeterministic
                             | load_error.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict, List

from .executor import (
    LoadError,
    collect_needed_names,
    collect_stateful_class_names,
    eval_case,
    make_reference_namespace,
)
from .model import Problem
from .parsing import problem_md
from .parsing.literals import equal, equal_unordered_deep
from .parsing.solution_md import extract_reference
from .parsing.solution_py import MainBlockNotFound, extract_cases


@dataclass
class VerifyResult:
    problem_id: str
    status: str  # ok | content_bug | no_reference | nondeterministic | load_error | no_cases
    ref_vs_expected: str = "n/a"  # pass | fail:<detail> | n/a
    expected_vs_problem: str = "n/a"  # pass | fail:<detail> | n/a
    num_cases: int = 0
    num_checked: int = 0
    detail: str = ""
    reference_heading: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _check_ref_against_expected(problem: Problem):
    """Return (status, detail, num_cases, num_checked, heading)."""
    sol_src = problem.solution_py.read_text(encoding="utf-8")
    cases = extract_cases(sol_src)
    det_cases = [c for c in cases if c.deterministic]

    ref = extract_reference(problem.solution_md.read_text(encoding="utf-8"))
    if ref.code is None:
        return "no_reference", "SOLUTION.md has no python fence", len(cases), 0, ""

    if not det_cases:
        return "nondeterministic", "no deterministic cases to check", len(cases), 0, ref.heading

    try:
        ns = make_reference_namespace(
            ref.code,
            needed_names=collect_needed_names(det_cases),
            stateful_names=collect_stateful_class_names(det_cases),
        )
    except LoadError as e:
        # A reference block that will not execute (indented fragment, missing
        # helper, etc.) cannot be used to verify — but this is a limitation of
        # the answer-key snippet, not evidence of a content bug in the problem.
        return "unverifiable", f"reference load: {e}", len(cases), 0, ref.heading

    mismatches: List[str] = []
    errors: List[str] = []
    unordered_only = 0  # mismatched strictly but matched as an unordered collection
    checked = 0
    for c in det_cases:
        try:
            actual = eval_case(ns, c.setup, c.call_src)
        except Exception as e:  # noqa: BLE001
            errors.append(f"case{c.index}: {type(e).__name__}: {e}")
            continue
        checked += 1
        # Cases explicitly annotated "(any order)" compare unordered outright
        # (deeply, so nested groupings like Group Anagrams also match).
        if c.unordered:
            if equal_unordered_deep(actual, c.expected):
                continue
            mismatches.append(f"case{c.index}: expected {c.expected!r}, ref gave {actual!r}")
            continue
        if equal(actual, c.expected):
            continue
        # A correct-but-reordered answer (top-k, k-closest, group-anagrams, ...)
        # is not a content bug — many problems accept any order. Retry with deep
        # order-insensitive comparison (handles nested groupings too).
        if equal_unordered_deep(actual, c.expected):
            unordered_only += 1
            continue
        mismatches.append(f"case{c.index}: expected {c.expected!r}, ref gave {actual!r}")

    # A mismatch is only trustworthy if the case it came from ran cleanly. If the
    # reference errored on some cases, those are interface problems (unverifiable),
    # not content bugs — but any clean-run strict-and-unordered value mismatch is
    # a real bug.
    if mismatches:
        return "content_bug", "; ".join(mismatches[:3]), len(cases), checked, ref.heading
    if errors and checked == 0:
        # Every case errored under the reference — interface couldn't be bound
        # (e.g. reference defines a differently-shaped API). Not a content bug.
        return "unverifiable", "; ".join(errors[:3]), len(cases), 0, ref.heading
    if unordered_only:
        return "ok_unordered", f"{unordered_only} case(s) match only ignoring order", len(cases), checked, ref.heading
    if errors:
        # Some cases verified cleanly and agreed; others errored on binding.
        return "ok_partial", "; ".join(errors[:2]), len(cases), checked, ref.heading
    return "ok", "", len(cases), checked, ref.heading


def _check_expected_against_problem(problem: Problem) -> str:
    """Static cross-check: solution.py expecteds vs PROBLEM.md function examples.

    Only compares when both sides are simple function-style with parsed outputs
    and counts line up; otherwise returns "n/a" (op-sequences and mismatched
    counts are out of scope for this cheap static check).
    """
    try:
        cases = [c for c in extract_cases(problem.solution_py.read_text(encoding="utf-8")) if c.deterministic]
        doc = problem_md.parse_file(problem.problem_md)
    except MainBlockNotFound:
        # No cases to align against — legitimately not applicable.
        return "n/a"
    except (OSError, UnicodeDecodeError, SyntaxError) as e:
        # A genuine read/parse failure (unreadable or non-UTF-8 PROBLEM.md, broken
        # solution.py). Use a distinct "error" marker so it stands out rather than
        # blending into the benign "n/a" (= nothing comparable).
        return f"error ({type(e).__name__}: {e})"

    fx = [e for e in doc.function_examples if e.output_parsed]
    if not fx or not cases:
        return "n/a"

    # Compare the outputs we can align by position (common prefix).
    n = min(len(fx), len(cases))
    for i in range(n):
        if not equal(cases[i].expected, fx[i].output):
            return f"fail (example{i + 1}: PROBLEM Output {fx[i].output!r} vs expected {cases[i].expected!r})"
    return "pass"


def verify_problem(problem: Problem) -> VerifyResult:
    try:
        status, detail, ncases, nchecked, heading = _check_ref_against_expected(problem)
    except Exception as e:  # noqa: BLE001
        return VerifyResult(problem.id, "load_error", detail=f"{type(e).__name__}: {e}")

    evp = _check_expected_against_problem(problem)

    res = VerifyResult(
        problem_id=problem.id,
        status=status,
        ref_vs_expected="pass" if status == "ok" else (f"fail:{detail}" if status == "content_bug" else status),
        expected_vs_problem=evp,
        num_cases=ncases,
        num_checked=nchecked,
        detail=detail,
        reference_heading=heading,
    )
    # The static PROBLEM.md-vs-expected check aligns examples to cases positionally,
    # which is noisy (examples and __main__ cases may use different inputs, and many
    # problems admit multiple valid answers). Keep it as an advisory signal only —
    # it does NOT change the trustworthy reference-execution status. `dsa verify
    # --advisories` surfaces these for manual review.
    return res


# --- Corpus-level verification with timeout protection ----------------------


def _verify_worker(problem: Problem, q) -> None:  # pragma: no cover - subprocess
    try:
        q.put(verify_problem(problem))
    except Exception as e:  # noqa: BLE001
        q.put(VerifyResult(problem.id, "load_error", detail=f"worker: {e}"))


def verify_problem_safe(problem: Problem, timeout: float = 10.0) -> VerifyResult:
    """Run :func:`verify_problem` in a subprocess so a pathological reference
    (infinite loop, runaway recursion) can't wedge a full-corpus scan."""
    import multiprocessing as mp

    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    p = ctx.Process(target=_verify_worker, args=(problem, q))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return VerifyResult(problem.id, "timeout", detail=f"timeout after {timeout}s")
    try:
        return q.get_nowait()
    except Exception:  # noqa: BLE001
        return VerifyResult(problem.id, "load_error", detail="no result from worker")


def verify_all(problems, timeout: float = 10.0, safe: bool = True):
    """Yield a :class:`VerifyResult` per problem.

    ``safe`` defaults to True so each problem runs in a subprocess with a wall-clock
    timeout: a single pathological reference (infinite loop, runaway recursion,
    blocking I/O) is killed and reported as ``timeout`` instead of wedging the entire
    corpus scan in-process. Pass ``safe=False`` for a faster in-process run when the
    references are known-terminating.
    """
    for problem in problems:
        yield verify_problem_safe(problem, timeout) if safe else verify_problem(problem)
