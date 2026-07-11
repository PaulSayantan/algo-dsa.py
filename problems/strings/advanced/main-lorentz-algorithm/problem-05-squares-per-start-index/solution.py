"""Squares Starting at Each Index.

Return ans of length n where ans[i] = number of squares XX that start at index i
(different lengths counted separately).

Fill in the body yourself. The recommended approach is the Main-Lorentz
algorithm: enumerate squares as O(n log n) contiguous start-index ranges, add +1
over each range with a difference array, and take a prefix sum.
"""

from __future__ import annotations

from typing import List


def squares_per_start_index(s: str) -> List[int]:
    """Count, for each index, how many squares start there.

    Args:
        s: The input string (lowercase English letters).

    Returns:
        A list ``ans`` of length ``len(s)`` where ``ans[i]`` is the number of
        block lengths ``L >= 1`` with ``s[i:i+L] == s[i+L:i+2L]`` (i.e. the number
        of squares beginning at index ``i``, distinct lengths counted separately).

    Example:
        >>> squares_per_start_index("aaaa")
        [2, 1, 1, 0]
        >>> squares_per_start_index("abcde")
        [0, 0, 0, 0, 0]
    """
    # TODO: implement using the Main-Lorentz algorithm + difference array.
    pass


if __name__ == "__main__":
    print(squares_per_start_index("aaaa"))          # expected: [2, 1, 1, 0]
    print(squares_per_start_index("abcabcabc"))      # expected: [1, 1, 1, 1, 0, 0, 0, 0, 0]
    print(squares_per_start_index("mississippi"))    # expected: [0, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0]
    print(squares_per_start_index("abcde"))          # expected: [0, 0, 0, 0, 0]
