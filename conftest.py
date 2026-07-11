"""Pytest root conftest: dynamically collect one test per solution.py case.

Running ``pytest`` at the repo root grades every learner ``solution.py`` against
its ``# expected:`` oracle — no per-problem test file is written, preserving the
3-file contract. Stub (unimplemented) solutions are reported as skips.

Scope it with the standard pytest node-id filter, e.g.::

    pytest problems/arrays/beginner/binary-search
    pytest -k "two-pointers"

The toolkit's own unit tests live under ``tests/`` and are collected normally.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dsa.grader import grade_source
from dsa.parsing.solution_py import MainBlockNotFound, extract_cases, is_stub

_ROOT = Path(__file__).parent
_PROBLEMS = _ROOT / "problems"


def pytest_collect_file(parent, file_path):  # type: ignore[override]
    p = Path(file_path)
    if p.name == "solution.py" and _PROBLEMS in p.parents:
        return SolutionFile.from_parent(parent, path=p)
    return None


class SolutionFile(pytest.File):
    def collect(self):
        source = self.path.read_text(encoding="utf-8")
        try:
            cases = extract_cases(source)
        except (MainBlockNotFound, SyntaxError):
            return
        rel = self.path.parent.relative_to(_PROBLEMS)
        for case in cases:
            yield SolutionItem.from_parent(
                self, name=f"{rel}::case-{case.index}", source=source, case_index=case.index
            )


class SolutionItem(pytest.Item):
    def __init__(self, *, source: str, case_index: int, **kw):
        super().__init__(**kw)
        self._source = source
        self._case_index = case_index

    def runtest(self) -> None:
        if is_stub(self._source):
            pytest.skip("solution.py is an unimplemented stub")
        result = grade_source(self._source, self.name)
        if result.load_error:
            pytest.fail(f"could not load solution: {result.load_error}", pytrace=False)
        crs = [r for r in result.results if r.case.index == self._case_index]
        if not crs:
            pytest.skip("case not found")
        cr = crs[0]
        if cr.status == "skip":
            pytest.skip(cr.detail or "skipped")
        if cr.status in ("fail", "error"):
            pytest.fail(cr.detail, pytrace=False)

    def reportinfo(self):
        return self.path, 0, self.name
