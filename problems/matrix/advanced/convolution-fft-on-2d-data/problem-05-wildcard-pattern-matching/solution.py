"""2D pattern matching with '?' wildcards, via masked correlation and FFT.

Fill in `find_matches` using Convolution / FFT on 2D data.
"""
from __future__ import annotations

from typing import List, Tuple


def find_matches(T: List[List[str]], P: List[List[str]]) -> List[Tuple[int, int]]:
    """Return all anchors where pattern P matches text T, honoring '?' wildcards.

    A match at (i, j) means for every pattern cell (r, c): P[r][c] == '?' or
    P[r][c] == T[i + r][j + c]. Anchors range over 0 <= i <= n - p and
    0 <= j <= m - q, and are returned in row-major order.

    Args:
        T: n x m grid of single-character strings (the text).
        P: p x q grid of single-character strings; '?' is a wildcard that matches
           any text character. p <= n and q <= m.

    Returns:
        A list of (i, j) anchor tuples where P occurs in T, in row-major order.

    Example:
        >>> find_matches(
        ...     [['a', 'b', 'a', 'b'],
        ...      ['b', 'a', 'b', 'a'],
        ...      ['a', 'b', 'a', 'b']],
        ...     [['a', '?'], ['?', 'a']],
        ... )
        [(0, 0), (0, 2), (1, 1)]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    T = [['a', 'b', 'a', 'b'],
         ['b', 'a', 'b', 'a'],
         ['a', 'b', 'a', 'b']]
    P = [['a', '?'], ['?', 'a']]
    print(find_matches(T, P))
    # Expected: [(0, 0), (0, 2), (1, 1)]

    T2 = [['1', '0', '1'], ['0', '1', '0']]
    P2 = [['?', '0'], ['0', '?']]
    print(find_matches(T2, P2))
    # Expected: [(0, 0)]
