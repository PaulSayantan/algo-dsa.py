"""Unit tests for the dsa toolkit's parsers, executor, and grader.

These pin the behavior the whole pipeline depends on: correct case extraction
across the three signature families, the two expected-comment placements, float
and non-deterministic handling, literal equality, reference extraction, and
end-to-end grading of a known-correct and a known-wrong solution.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dsa.discovery import find_problems, iter_problems, workspace_root
from dsa.grader import grade_source
from dsa.parsing import solution_md
from dsa.parsing.literals import equal, equal_unordered, try_parse_literal
from dsa.parsing.solution_py import extract_cases, extract_cases_from_file, is_stub

ROOT = workspace_root()


def _p(pid: str) -> Path:
    return ROOT / "problems" / pid


# --- literals ---------------------------------------------------------------


@pytest.mark.parametrize(
    "text,expected",
    [
        ("4", 4),
        ("-1", -1),
        ("12.75", 12.75),
        ("[[1, 4], [2, 5]]", [[1, 4], [2, 5]]),
        ("'abc'", "abc"),
        ("True", True),
        ("[7, 7, 7]  (all > highVal)", [7, 7, 7]),  # trailing aside trimmed
    ],
)
def test_try_parse_literal_ok(text, expected):
    ok, value = try_parse_literal(text)
    assert ok and value == expected


@pytest.mark.parametrize("text", ["a valid wiggle", "some permutation of [1,2,3]", ""])
def test_try_parse_literal_prose(text):
    ok, _ = try_parse_literal(text)
    assert not ok


def test_equal_float_tolerance():
    assert equal(4.0000001, 4.0)
    assert equal([1, 2.0000001], [1, 2])
    assert not equal(4.1, 4.0)


def test_equal_unordered():
    assert equal_unordered([3, 1, 2], [1, 2, 3])
    assert not equal_unordered([1, 2, 2], [1, 2, 3])


# --- case extraction: signature families ------------------------------------


def test_class_solution_cases():
    cases = extract_cases_from_file(_p("arrays/beginner/binary-search/problem-01-binary-search") / "solution.py")
    assert [c.expected for c in cases] == [4, -1, 0]
    # Every case's setup starts by constructing the Solution object. Later cases
    # additionally replay earlier calls (harmless for stateless problems, and
    # required for stateful op-sequences).
    assert all(c.setup[0] == "sol = Solution()" for c in cases)
    assert all("sol.search(" in c.call_src for c in cases)


def test_design_class_op_replay():
    # Stateful KthLargest: each case carries cumulative setup so state replays.
    cases = extract_cases_from_file(
        _p("paradigms/heap-priority-queue/problem-01-kth-largest-in-stream") / "solution.py"
    )
    assert [c.expected for c in cases] == [4, 5, 5, 8, 8]
    assert [c.call_src for c in cases] == [
        "kl.add(3)",
        "kl.add(5)",
        "kl.add(10)",
        "kl.add(9)",
        "kl.add(4)",
    ]


def test_free_function_cases():
    cases = extract_cases_from_file(
        _p("arrays/advanced/convex-hull-trick-li-chao-tree/problem-05-building-bridges") / "solution.py"
    )
    assert [c.expected for c in cases] == [32, 3]
    assert cases[0].setup == []  # first case has no prior setup/calls


# --- case extraction: expected-comment placement ----------------------------


def test_block_comment_below_print_not_shifted():
    # transpose puts "# Expected:" BELOW each print; expecteds must not shift by one.
    cases = extract_cases_from_file(_p("matrix/beginner/transpose/problem-01-transpose-matrix") / "solution.py")
    assert cases[0].expected == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert cases[1].expected == [[1, 4], [2, 5], [3, 6]]
    assert cases[2].expected == [[7]]


def test_block_comment_above_print():
    cases = extract_cases_from_file(
        _p("arrays/advanced/convex-hull-trick-li-chao-tree/problem-05-building-bridges") / "solution.py"
    )
    assert cases[0].expected == 32


def test_float_expected_parsed():
    cases = extract_cases_from_file(
        _p("arrays/beginner/sliding-window-fixed-size/problem-02-maximum-average-subarray-i") / "solution.py"
    )
    assert cases[0].expected == pytest.approx(12.75)


def test_nondeterministic_marked():
    cases = extract_cases_from_file(
        _p("paradigms/randomization/problem-04-generate-random-point-in-a-circle") / "solution.py"
    )
    assert all(not c.deterministic for c in cases)


def test_any_order_qualifier_marks_unordered():
    cases = extract_cases_from_file(
        _p("arrays/intermediate/quickselect/problem-03-k-closest-points-to-origin") / "solution.py"
    )
    # The second case comment says "expected (any order): ...".
    assert any(c.unordered for c in cases)


# --- stub detection ---------------------------------------------------------


def test_is_stub_true_for_template():
    src = (_p("arrays/beginner/binary-search/problem-01-binary-search") / "solution.py").read_text()
    assert is_stub(src)


def test_is_stub_false_for_implementation():
    src = "def f(x):\n    return x + 1\n"
    assert not is_stub(src)


def test_is_stub_ignores_boilerplate_and_helpers():
    # A template with a filled-in ListNode data class and build/to_list harness
    # helpers but an empty entrypoint is still a stub (the invoked method is empty).
    src = (
        _p("arrays/beginner/insertion-sort/problem-02-insertion-sort-list") / "solution.py"
    ).read_text()
    assert is_stub(src)


def test_full_corpus_solutions_are_all_stubs():
    # Every shipped solution.py must register as an unimplemented stub, so the
    # pytest collector reports skips (not failures) out of the box.
    non_stub = [
        p.id for p in iter_problems() if not is_stub(p.solution_py.read_text(encoding="utf-8"))
    ]
    assert non_stub == []


# --- reference extraction ---------------------------------------------------


def test_reference_extraction_prefers_optimal():
    ref = solution_md.extract_reference_file(
        _p("arrays/beginner/binary-search/problem-01-binary-search") / "SOLUTION.md"
    )
    assert ref.code is not None
    assert ref.heading.lower().startswith("optimal")
    assert "lo" in ref.code and "hi" in ref.code


# --- end-to-end grading -----------------------------------------------------


def test_grade_correct_solution_passes():
    stub = (_p("arrays/beginner/binary-search/problem-01-binary-search") / "solution.py").read_text()
    correct = stub.replace(
        "        # TODO: implement\n        pass",
        (
            "        lo, hi = 0, len(nums) - 1\n"
            "        while lo <= hi:\n"
            "            mid = (lo + hi) // 2\n"
            "            if nums[mid] == target:\n"
            "                return mid\n"
            "            if nums[mid] < target:\n"
            "                lo = mid + 1\n"
            "            else:\n"
            "                hi = mid - 1\n"
            "        return -1"
        ),
    )
    result = grade_source(correct, "bs")
    assert result.ok and result.passed == 3


def test_stateful_opseq_replays_correctly():
    # KthLargest is stateful: case N depends on the mutations of cases < N. A
    # correct implementation must pass all 5 cases, which only works if prior
    # add() calls are replayed as setup. We use the real __main__ oracle from the
    # workspace with a hand-written correct body.
    oracle = (
        _p("arrays/advanced/top-k-via-heap/problem-01-kth-largest-in-a-stream") / "solution.py"
    ).read_text()
    main_block = oracle[oracle.index("if __name__"):]
    impl = (
        "import heapq\n"
        "from typing import List\n\n\n"
        "class KthLargest:\n"
        "    def __init__(self, k, nums):\n"
        "        self.k = k\n"
        "        self.heap = nums[:]\n"
        "        heapq.heapify(self.heap)\n"
        "        while len(self.heap) > k:\n"
        "            heapq.heappop(self.heap)\n\n"
        "    def add(self, val):\n"
        "        heapq.heappush(self.heap, val)\n"
        "        if len(self.heap) > self.k:\n"
        "            heapq.heappop(self.heap)\n"
        "        return self.heap[0]\n\n\n"
        + main_block
    )
    result = grade_source(impl, "kth")
    assert result.ok and result.passed == 5


def test_grade_wrong_solution_fails():
    stub = (_p("arrays/beginner/binary-search/problem-01-binary-search") / "solution.py").read_text()
    wrong = stub.replace("        # TODO: implement\n        pass", "        return 0")
    result = grade_source(wrong, "bs-wrong")
    assert not result.ok and result.failed == 2


def test_stub_solution_all_skipped():
    stub = (_p("arrays/beginner/binary-search/problem-01-binary-search") / "solution.py").read_text()
    result = grade_source(stub, "bs-stub")
    assert result.passed == 0 and result.failed == 0
    assert all(r.status == "skip" for r in result.results)


# --- discovery --------------------------------------------------------------


def test_discovery_counts():
    problems = list(iter_problems())
    assert len(problems) == 884
    cats = {p.category for p in problems}
    assert cats == {"arrays", "strings", "matrix", "paradigms"}


def test_find_by_algorithm():
    probs = find_problems(algorithm="binary-search", category="arrays")
    assert probs and all(p.algorithm == "binary-search" for p in probs)
