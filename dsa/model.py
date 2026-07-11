"""Core dataclasses shared across the toolkit."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List, Optional


@dataclass
class Case:
    """One executable check derived from a ``__main__`` block.

    A case corresponds to a single ``print(<call>)`` statement. ``setup`` holds
    the source of every non-print statement that appeared *before* this print in
    the block (object construction, mutations, intermediate assignments), so
    replaying ``setup`` then evaluating ``call_src`` reproduces the exact state
    the print observed. This is what makes stateful design-class op-sequences
    (e.g. ``KthLargest.add``) replay correctly with no special-casing.
    """

    index: int
    call_src: str
    setup: List[str] = field(default_factory=list)
    expected: Any = None
    # "value"          -> deterministic; compare eval(call) to `expected`
    # "nondeterministic" -> expected could not be parsed as a literal (prose hint)
    kind: str = "value"
    raw_expected: Optional[str] = None
    lineno: int = 0
    # True when the comment said "(any order)" — compare as an unordered collection.
    unordered: bool = False

    @property
    def deterministic(self) -> bool:
        return self.kind == "value"


@dataclass
class Problem:
    """A single problem folder and everything parsed from its three files."""

    id: str  # e.g. "arrays/beginner/linear-search/problem-01-linear-search"
    path: Path
    category: str  # arrays | strings | matrix | paradigms
    difficulty_tier: str  # beginner | intermediate | advanced | "" (paradigms)
    algorithm: str  # algorithm slug (parent folder)
    slug: str  # problem folder name

    problem_md: Path = None  # type: ignore[assignment]
    solution_py: Path = None  # type: ignore[assignment]
    solution_md: Path = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.problem_md is None:
            self.problem_md = self.path / "PROBLEM.md"
        if self.solution_py is None:
            self.solution_py = self.path / "solution.py"
        if self.solution_md is None:
            self.solution_md = self.path / "SOLUTION.md"


@dataclass
class CaseResult:
    """Outcome of grading one case."""

    case: Case
    status: str  # pass | fail | error | skip
    actual: Any = None
    detail: str = ""


@dataclass
class ProblemResult:
    """Aggregate outcome of grading all cases for one problem/module."""

    problem_id: str
    results: List[CaseResult] = field(default_factory=list)
    load_error: Optional[str] = None

    @property
    def passed(self) -> int:
        return sum(1 for r in self.results if r.status == "pass")

    @property
    def failed(self) -> int:
        return sum(1 for r in self.results if r.status in ("fail", "error"))

    @property
    def skipped(self) -> int:
        return sum(1 for r in self.results if r.status == "skip")

    @property
    def ok(self) -> bool:
        """True if nothing failed/errored and the module loaded."""
        return self.load_error is None and self.failed == 0
