"""LeetCode 308 - Range Sum Query 2D - Mutable.

Fill in the body using a 2D Binary Indexed Tree (Fenwick Tree) to support
point updates and rectangle-sum queries.
"""

from typing import List


class NumMatrix:
    """Supports point updates and rectangle-sum queries over a mutable matrix.

    Args:
        matrix: The initial 2D integer matrix.

    Example:
        >>> nm = NumMatrix([[1, 2], [3, 4]])
        >>> nm.sumRegion(0, 0, 1, 1)
        10
        >>> nm.update(0, 0, 10)
        >>> nm.sumRegion(0, 0, 1, 1)
        19
    """

    def __init__(self, matrix: List[List[int]]) -> None:
        # TODO: implement (initialize a 2D Fenwick Tree and cache cell values)
        pass

    def update(self, row: int, col: int, val: int) -> None:
        """Set matrix[row][col] = val in O(log m * log n).

        Args:
            row: 0-based row index.
            col: 0-based column index.
            val: New value for the cell.
        """
        # TODO: implement
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Return the sum of the sub-rectangle [row1..row2] x [col1..col2].

        Args:
            row1: Top row (inclusive).
            col1: Left column (inclusive).
            row2: Bottom row (inclusive, >= row1).
            col2: Right column (inclusive, >= col1).

        Returns:
            The inclusive rectangle sum.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    nm = NumMatrix([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ])
    print(nm.sumRegion(2, 1, 4, 3))  # expected: 8
    nm.update(3, 2, 2)
    print(nm.sumRegion(2, 1, 4, 3))  # expected: 10
