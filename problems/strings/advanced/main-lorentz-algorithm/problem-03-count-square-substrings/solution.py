"""Count Square Substrings.

Count all occurrences (i, length) such that s[i:i+length] is a square XX,
counting different (start, length) positions separately (with multiplicity).

Fill in the body yourself. The recommended approach is the Main-Lorentz
algorithm: enumerate squares as O(n log n) contiguous start-index ranges and sum
the sizes of those ranges.
"""

from __future__ import annotations


def count_square_substrings(s: str) -> int:
    """Count all square occurrences ``(start, length)`` in ``s``.

    Args:
        s: The input string (lowercase English letters).

    Returns:
        The number of positions ``(i, length)`` for which ``s[i:i+length]`` is a
        tandem repeat ``XX``. Positions with the same content but different
        ``(start, length)`` are counted separately.

    Example:
        >>> count_square_substrings("aabb")
        2
        >>> count_square_substrings("aaaa")
        4
    """
    # TODO: implement using the Main-Lorentz algorithm.
    pass


if __name__ == "__main__":
    print(count_square_substrings("aabb"))        # expected: 2
    print(count_square_substrings("abcabcabc"))    # expected: 4
    print(count_square_substrings("aaaa"))         # expected: 4
    print(count_square_substrings("abcde"))        # expected: 0
