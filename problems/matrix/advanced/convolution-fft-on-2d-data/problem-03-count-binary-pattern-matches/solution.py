"""Count exact occurrences of a binary pattern grid inside a binary text grid.

Fill in `count_pattern_matches` using Convolution / FFT on 2D data.
"""
from __future__ import annotations

from typing import List


def count_pattern_matches(T: List[List[int]], P: List[List[int]]) -> int:
    """Count top-left positions where pattern P matches text T exactly.

    A match at (i, j) means T[i + r][j + c] == P[r][c] for every cell of P.
    Only positions with 0 <= i <= n - p and 0 <= j <= m - q are considered.

    Args:
        T: n x m binary grid (entries 0 or 1).
        P: p x q binary grid (entries 0 or 1), with p <= n and q <= m.

    Returns:
        The number of positions at which P occurs in T.

    Example:
        >>> count_pattern_matches(
        ...     [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]],
        ...     [[1, 0], [0, 1]],
        ... )
        3
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    T = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    P = [[1, 0], [0, 1]]
    print(count_pattern_matches(T, P))
    # Expected: 3

    print(count_pattern_matches([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1], [1, 1]]))
    # Expected: 4
