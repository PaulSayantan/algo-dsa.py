"""Grade a solution namespace against a list of cases."""

from __future__ import annotations

import multiprocessing as mp
from typing import Any, Dict, List

from .executor import LoadError, eval_case, make_namespace
from .model import Case, CaseResult, ProblemResult
from .parsing.literals import equal, equal_unordered
from .parsing.solution_py import extract_cases, is_stub


def grade_namespace(
    namespace: Dict[str, Any],
    cases: List[Case],
    problem_id: str = "",
    *,
    unordered: bool = False,
    skip_nondeterministic: bool = True,
) -> ProblemResult:
    """Run each case against ``namespace`` and collect results."""
    result = ProblemResult(problem_id=problem_id)
    for case in cases:
        # Per-case "(any order)" annotation, or a caller-wide unordered override.
        cmp = equal_unordered if (unordered or case.unordered) else equal
        if not case.deterministic:
            if skip_nondeterministic:
                result.results.append(
                    CaseResult(case, "skip", detail="non-deterministic output")
                )
                continue
        try:
            actual = eval_case(namespace, case.setup, case.call_src)
        except Exception as e:  # noqa: BLE001
            result.results.append(
                CaseResult(case, "error", detail=f"{type(e).__name__}: {e}")
            )
            continue
        if not case.deterministic:
            # Ran without error; we cannot check the value.
            result.results.append(CaseResult(case, "skip", actual=actual, detail="non-deterministic"))
            continue
        # The comparison must be guarded too: a returned object with a raising __eq__
        # (a common accidental learner bug, e.g. a __eq__ assuming `other` is the same
        # type) would otherwise propagate out of grade_namespace, aborting every
        # remaining case and crashing the CLI instead of failing just this one case.
        try:
            matched = cmp(actual, case.expected)
        except Exception as e:  # noqa: BLE001
            result.results.append(
                CaseResult(case, "error", actual=actual, detail=f"compare {type(e).__name__}: {e}")
            )
            continue
        if matched:
            result.results.append(CaseResult(case, "pass", actual=actual))
        else:
            result.results.append(
                CaseResult(
                    case,
                    "fail",
                    actual=actual,
                    detail=f"expected {case.expected!r}, got {actual!r}",
                )
            )
    return result


def grade_source(
    solution_source: str,
    problem_id: str = "",
    *,
    preamble: str = "",
    unordered: bool = False,
) -> ProblemResult:
    """Extract cases from ``solution_source`` and grade that source against them.

    If every definition is an unimplemented stub, all cases are skipped with a
    clear reason (rather than reported as failures).
    """
    try:
        cases = extract_cases(solution_source)
    except Exception as e:  # noqa: BLE001
        return ProblemResult(problem_id=problem_id, load_error=f"case-extract: {e}")

    if is_stub(solution_source):
        r = ProblemResult(problem_id=problem_id)
        for c in cases:
            r.results.append(CaseResult(c, "skip", detail="stub (not implemented yet)"))
        return r

    try:
        ns = make_namespace(solution_source, preamble=preamble)
    except LoadError as e:
        return ProblemResult(problem_id=problem_id, load_error=str(e))

    return grade_namespace(ns, cases, problem_id, unordered=unordered)


# --- Sandboxed execution (timeout protection for learner code) --------------


def _worker(source: str, problem_id: str, preamble: str, unordered: bool, q: "mp.Queue") -> None:
    try:
        res = grade_source(source, problem_id, preamble=preamble, unordered=unordered)
        # ``CaseResult.actual`` holds the learner's raw return value, which may be an
        # exec-defined object that cannot be pickled across the spawn boundary. No
        # consumer reads ``actual`` (failure ``detail`` already embeds its repr), so
        # drop it before ``q.put`` — otherwise an unpicklable value would fail in the
        # feeder thread and the parent would misreport a graded result as lost.
        for cr in res.results:
            cr.actual = None
        q.put(res)
    except Exception as e:  # noqa: BLE001
        q.put(ProblemResult(problem_id=problem_id, load_error=f"worker: {e}"))


def grade_source_sandboxed(
    solution_source: str,
    problem_id: str = "",
    *,
    preamble: str = "",
    unordered: bool = False,
    timeout: float = 10.0,
) -> ProblemResult:
    """Grade in a subprocess so infinite loops / hangs cannot wedge the runner."""
    ctx = mp.get_context("spawn")
    q: "mp.Queue" = ctx.Queue()
    p = ctx.Process(target=_worker, args=(solution_source, problem_id, preamble, unordered, q))
    p.start()
    p.join(timeout)
    if p.is_alive():
        p.terminate()
        p.join()
        return ProblemResult(problem_id=problem_id, load_error=f"timeout after {timeout}s")
    try:
        return q.get_nowait()
    except Exception:  # noqa: BLE001
        return ProblemResult(problem_id=problem_id, load_error="no result from worker")
