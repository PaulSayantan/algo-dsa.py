"""Range Sum Query 2D - Immutable (LeetCode 304).

Fill in the body of the NumMatrix class. Do not change the signatures.
"""

from typing import List


class NumMatrix:
    """Answer submatrix-sum queries in O(1) after preprocessing.

    Example:
        >>> nm = NumMatrix([[3, 0, 1, 4, 2],
        ...                 [5, 6, 3, 2, 1],
        ...                 [1, 2, 0, 1, 5],
        ...                 [4, 1, 0, 1, 7],
        ...                 [1, 0, 3, 0, 5]])
        >>> nm.sumRegion(2, 1, 4, 3)   # expected 8
        >>> nm.sumRegion(1, 1, 2, 2)   # expected 11
        >>> nm.sumRegion(1, 2, 2, 4)   # expected 12
    """

    def __init__(self, matrix: List[List[int]]) -> None:
        """Preprocess the matrix (build the 2D prefix-sum table here).

        Args:
            matrix: A non-empty m x n grid of integers that will not change.
        """
        # TODO: implement
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Return the sum of the submatrix bounded by the given corners.

        Args:
            row1: Top row index (inclusive).
            col1: Left column index (inclusive).
            row2: Bottom row index (inclusive).
            col2: Right column index (inclusive).

        Returns:
            The sum of all matrix[i][j] with row1 <= i <= row2 and
            col1 <= j <= col2.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    nm = NumMatrix(
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5],
        ]
    )
    print(nm.sumRegion(2, 1, 4, 3))  # expected 8
    print(nm.sumRegion(1, 1, 2, 2))  # expected 11
    print(nm.sumRegion(1, 2, 2, 4))  # expected 12
