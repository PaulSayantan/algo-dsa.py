"""
LeetCode 308 - Range Sum Query 2D - Mutable

Implement NumMatrix supporting point updates and submatrix-sum queries,
each in O(log m * log n) using a 2D Binary Indexed Tree (Fenwick Tree).

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]) -> None:
        """
        Initialize the structure with a 2D integer matrix.

        Args:
            matrix: The initial m x n integer grid. It is guaranteed to be
                non-empty with at least one row and one column.

        Returns:
            None.
        """
        # TODO: implement
        # Suggested state to maintain:
        #   self.rows, self.cols
        #   self.tree  -> (rows+1) x (cols+1) BIT, all zeros
        #   self.nums  -> a copy of the current cell values, so update() can
        #                 compute the delta (val - old_value)
        # Then seed the BIT by calling your internal point-add for every cell.
        pass

    def update(self, row: int, col: int, val: int) -> None:
        """
        Set matrix[row][col] to val.

        Args:
            row: 0-indexed row of the cell to update.
            col: 0-indexed column of the cell to update.
            val: New value for the cell.

        Returns:
            None.

        Example:
            nm.update(3, 2, 2)  # matrix[3][2] becomes 2
        """
        # TODO: implement
        # Compute delta = val - self.nums[row][col], store the new value,
        # then add `delta` to the BIT at (row, col).
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Return the sum of the elements inside the rectangle with upper-left
        corner (row1, col1) and lower-right corner (row2, col2), inclusive.

        Args:
            row1: Top row of the query rectangle (inclusive).
            col1: Left column of the query rectangle (inclusive).
            row2: Bottom row of the query rectangle (inclusive).
            col2: Right column of the query rectangle (inclusive).

        Returns:
            The integer sum of all cells in the rectangle.

        Example:
            nm.sumRegion(2, 1, 4, 3)  # -> 8
        """
        # TODO: implement
        # Use inclusion-exclusion on prefix sums:
        #   prefix(r2, c2) - prefix(r1-1, c2) - prefix(r2, c1-1) + prefix(r1-1, c1-1)
        pass


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    nm = NumMatrix(matrix)
    print(nm.sumRegion(2, 1, 4, 3))  # expected: 8
    nm.update(3, 2, 2)
    print(nm.sumRegion(2, 1, 4, 3))  # expected: 10
