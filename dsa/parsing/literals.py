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
        # ast.literal_eval raises ValueError/SyntaxError for malformed input, but also
        # TypeError for structurally-valid-but-illegal literals (e.g. an unhashable
        # dict key like "{[1]: 2}") and MemoryError/RecursionError on pathological
        # nesting. Treat all of them uniformly as "not a literal" so a single bad
        # comment degrades to a non-deterministic case rather than aborting the whole
        # problem's case extraction upstream.
        except (ValueError, SyntaxError, TypeError, MemoryError, RecursionError):
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
    # Floats (including one-side-float comparisons like 5 vs 5.0). Only take the
    # tolerance branch when BOTH operands are genuinely numeric — otherwise a float()
    # coercion of a numeric-looking string (e.g. equal("5", 5.0)) would report a true
    # type mismatch as equal, silently PASSing an incorrect solution. bool is an int
    # subclass, so True/1.0 still compares here, matching this function's documented
    # "True == 1" behavior.
    if isinstance(actual, float) or isinstance(expected, float):
        if not (isinstance(actual, (int, float)) and isinstance(expected, (int, float))):
            return False
        return math.isclose(float(actual), float(expected), rel_tol=rel_tol, abs_tol=abs_tol)

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


def _perfect_matching(actual: Any, expected: Any, elem_equal) -> bool:
    """True iff every ``expected`` element can be paired 1:1 with an ``actual`` one.

    Greedy first-match is *unsound* here: element equality goes through
    :func:`equal`'s ``math.isclose`` tolerance, which is not transitive, so a greedy
    pairing can consume an actual element that another expected element uniquely
    needed and wrongly report a mismatch (false FAIL) even though a valid perfect
    matching exists. We instead compute a maximum bipartite matching via augmenting
    paths (Kuhn's algorithm) and require it to cover every element.
    """
    n = len(expected)
    adj = [[j for j, a in enumerate(actual) if elem_equal(a, e)] for e in expected]
    match_a = [-1] * len(actual)  # actual index -> matched expected index, or -1

    def _augment(i: int, seen: list) -> bool:
        for j in adj[i]:
            if not seen[j]:
                seen[j] = True
                if match_a[j] == -1 or _augment(match_a[j], seen):
                    match_a[j] = i
                    return True
        return False

    matched = sum(_augment(i, [False] * len(actual)) for i in range(n))
    return matched == n


def equal_unordered(actual: Any, expected: Any, **kw: Any) -> bool:
    """Order-insensitive comparison for top-level sequences (opt-in per problem)."""
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if len(actual) != len(expected):
            return False
        return _perfect_matching(actual, expected, lambda a, e: equal(a, e, **kw))
    return equal(actual, expected, **kw)


def equal_unordered_deep(actual: Any, expected: Any, **kw: Any) -> bool:
    """Order-insensitive comparison applied recursively to nested sequences.

    Handles answers like Group Anagrams where both the outer grouping order and
    each inner group's order are arbitrary. Matches elements by deep unordered
    equality using a sound maximum bipartite matching (see :func:`_perfect_matching`).
    """
    if isinstance(expected, (list, tuple)) and isinstance(actual, (list, tuple)):
        if len(actual) != len(expected):
            return False
        return _perfect_matching(actual, expected, lambda a, e: equal_unordered_deep(a, e, **kw))
    return equal(actual, expected, **kw)
