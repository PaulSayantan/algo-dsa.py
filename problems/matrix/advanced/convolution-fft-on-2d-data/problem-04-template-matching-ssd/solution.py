"""2D template matching: find the window minimizing sum of squared differences.

Fill in `best_match` using Convolution / FFT on 2D data.
"""
from __future__ import annotations

from typing import List, Tuple


def best_match(I: List[List[int]], Tpl: List[List[int]]) -> Tuple[int, int]:
    """Return the top-left anchor minimizing SSD between a window of I and Tpl.

    SSD(i, j) = sum over r, c of (I[i + r][j + c] - Tpl[r][c]) ** 2, taken over
    all valid anchors 0 <= i <= n - p, 0 <= j <= m - q. Ties are broken by
    smallest i, then smallest j (row-major order).

    Args:
        I: n x m integer intensity matrix.
        Tpl: p x q integer template, with p <= n and q <= m.

    Returns:
        A tuple (i, j): the anchor of the best-matching (lowest-SSD) window.

    Example:
        >>> best_match(
        ...     [[1, 2, 3, 0], [4, 5, 6, 1], [7, 8, 9, 2]],
        ...     [[5, 6], [8, 9]],
        ... )
        (1, 1)
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    I = [[1, 2, 3, 0], [4, 5, 6, 1], [7, 8, 9, 2]]
    Tpl = [[5, 6], [8, 9]]
    print(best_match(I, Tpl))
    # Expected: (1, 1)

    print(best_match([[0, 0, 0], [0, 9, 0], [0, 0, 0]], [[9]]))
    # Expected: (1, 1)
