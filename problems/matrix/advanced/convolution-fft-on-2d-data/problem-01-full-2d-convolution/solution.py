"""Full 2D linear convolution of two integer matrices.

Fill in `convolve2d_full` using Convolution / FFT on 2D data.
"""
from __future__ import annotations

from typing import List


def convolve2d_full(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    """Return the full 2D linear convolution of matrices A and B.

    The result has shape (rA + rB - 1) x (cA + cB - 1), where
        C[i][j] = sum over k, l of A[k][l] * B[i - k][j - l]
    restricted to indices lying inside both matrices.

    Args:
        A: Integer matrix of shape rA x cA (all rows equal length).
        B: Integer matrix of shape rB x cB (all rows equal length).

    Returns:
        The full convolution matrix C of shape (rA + rB - 1) x (cA + cB - 1),
        with integer entries.

    Example:
        >>> convolve2d_full([[1, 2], [3, 4]], [[1, 0], [0, 1]])
        [[1, 2, 0], [3, 5, 2], [0, 3, 4]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[1, 0], [0, 1]]
    print(convolve2d_full(A, B))
    # Expected: [[1, 2, 0], [3, 5, 2], [0, 3, 4]]

    print(convolve2d_full([[1, 2, 3]], [[1, 1]]))
    # Expected: [[1, 3, 5, 3]]
