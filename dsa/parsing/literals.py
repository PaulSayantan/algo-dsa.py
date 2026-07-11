"""Parsing and comparison of expected-output literals.

Expected values in the workspace are Python literals written in ``# expected:``
comments (ints, floats, strings, bools, None, and nested lists/tuples/dicts).
A handful are prose ("a valid wiggle", "some permutation") and must be treated
as non-deterministic rather than parsed.
"""

from __future__ import annotations

import ast
import math
from typing import Any, Tuple

_SENTINEL = object()


def try_parse_literal(text: str) -> Tuple[bool, Any]:
    """Attempt to parse ``text`` as a Python literal.

    Returns ``(True, value)`` on success, ``(False, None)`` if the text is not a
    literal (e.g. a prose hint). ``ast.literal_eval`` safely handles the literal
    grammar without executing arbitrary code.
    """
    stripped = text.strip()
    if not stripped:
        return False, None
    # Some comments trail an aside after the literal, e.g. "[7, 7, 7]  (all > highVal)".
    # Try the whole string first; if that fails, retry progressively shorter prefixes
    # that end at a balanced bracket/quote boundary.
    for candidate in _candidate_prefixes(stripped):
        try:
            return True, ast.literal_eval(candidate)
        except (ValueError, SyntaxError):
            continue
    return False, None


def _candidate_prefixes(text: str):
    """Yield the full string, then trailing-comment-trimmed variants."""
    yield text
    # Trim a trailing parenthetical/aside separated by two+ spaces or a '#'.
    for sep in ("  (", "  #", "  //", "  -"):
        idx = text.find(sep)
        if idx > 0:
            yield text[:idx].strip()


def equal(actual: Any, expected: Any, *, rel_tol: float = 1e-6, abs_tol: float = 1e-9) -> bool:
    """Structural equality with float tolerance applied recursively.

    Ints and bools compare exactly (note ``True == 1`` in Python; we keep that
    behavior since expected literals are canonical). Floats anywhere in a nested
    structure compare with :func:`math.isclose`.
    """
    # Floats (including one-side-float comparisons like 5 vs 5.0).
    if isinstance(actual, float) or isinstance(expected, float):
        try:
            return math.isclose(float(actual), float(expected), rel_tol=rel_tol, abs_tol=abs_tol)
        except (TypeError, ValueError):
            return False

    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if len(actual) != len(expected):
            return False
        return all(equal(a, e, rel_tol=rel_tol, abs_tol=abs_tol) for a, e in zip(actual, expected))

    if isinstance(expected, dict) and isinstance(actual, dict):
        if actual.keys() != expected.keys():
            return False
        return all(
            equal(actual[k], expected[k], rel_tol=rel_tol, abs_tol=abs_tol) for k in expected
        )

    return actual == expected


def equal_unordered(actual: Any, expected: Any, **kw: Any) -> bool:
    """Order-insensitive comparison for top-level sequences (opt-in per problem)."""
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if len(actual) != len(expected):
            return False
        remaining = list(actual)
        for e in expected:
            for i, a in enumerate(remaining):
                if equal(a, e, **kw):
                    del remaining[i]
                    break
            else:
                return False
        return True
    return equal(actual, expected, **kw)


def equal_unordered_deep(actual: Any, expected: Any, **kw: Any) -> bool:
    """Order-insensitive comparison applied recursively to nested sequences.

    Handles answers like Group Anagrams where both the outer grouping order and
    each inner group's order are arbitrary. Matches elements greedily by deep
    unordered equality.
    """
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if len(actual) != len(expected):
            return False
        remaining = list(actual)
        for e in expected:
            for i, a in enumerate(remaining):
                if equal_unordered_deep(a, e, **kw):
                    del remaining[i]
                    break
            else:
                return False
        return True
    return equal(actual, expected, **kw)
