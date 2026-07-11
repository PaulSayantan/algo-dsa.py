"""Detect a Tandem Repeat.

Return whether the string contains any substring of the form XX (a square).

Fill in the body yourself. The recommended approach is the Main-Lorentz
divide-and-conquer: split the string in half, recurse, and detect squares that
cross the midpoint using the Z-function. Existence only requires knowing whether
any crossing range is non-empty.
"""

from __future__ import annotations


def contains_tandem_repeat(s: str) -> bool:
    """Decide whether ``s`` contains at least one tandem repeat (square ``XX``).

    Args:
        s: The input string (lowercase English letters).

    Returns:
        True if some contiguous substring of ``s`` has the form ``XX`` for a
        non-empty block ``X``; otherwise False.

    Example:
        >>> contains_tandem_repeat("abab")
        True
        >>> contains_tandem_repeat("abcde")
        False
    """
    # TODO: implement using the Main-Lorentz algorithm.
    pass


if __name__ == "__main__":
    print(contains_tandem_repeat("abab"))        # expected: True
    print(contains_tandem_repeat("abcde"))       # expected: False
    print(contains_tandem_repeat("abcabcabc"))   # expected: True
    print(contains_tandem_repeat("a"))           # expected: False
