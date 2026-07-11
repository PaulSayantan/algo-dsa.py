"""
LeetCode 2536 - Increment Submatrices by One

Start from an n x n zero matrix. For each query [row1, col1, row2, col2] add 1
to the whole submatrix, then return the final matrix.

Demonstrates the RANGE-UPDATE / POINT-QUERY mode of a 2D BIT: a rectangle add
is applied as four point updates on a 2D difference decomposition, and each
final cell value is read as a 2D prefix sum over that difference structure.

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """
        Apply every rectangle increment and return the resulting matrix.

        Args:
            n: Side length of the square matrix (n x n, initially all zeros).
            queries: List of [row1, col1, row2, col2] rectangles (all inclusive,
                0-indexed) to increment by 1.

        Returns:
            The n x n matrix after all increments have been applied.

        Example:
            Solution().rangeAddQueries(3, [[1,1,2,2],[0,0,1,1]])
            # -> [[1,1,0],[1,2,1],[0,1,1]]
        """
        # TODO: implement
        # Approach A (2D BIT, range-update/point-query):
        #   For each query, "add +1 to rectangle" == four point updates on a BIT
        #   whose prefix-sum AT a cell equals that cell's value:
        #       add(r1,   c1,   +1)
        #       add(r2+1, c1,   -1)
        #       add(r1,   c2+1, -1)
        #       add(r2+1, c2+1, +1)
        #   Then mat[i][j] = prefix_query(i, j).
        #
        # Approach B (2D difference array, O(n^2 + q)): same four-corner update
        #   into a diff grid, then a 2D prefix-sum pass to recover mat.
        pass


if __name__ == "__main__":
    print(Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]))
    # expected: [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
    print(Solution().rangeAddQueries(2, [[0, 0, 1, 1]]))
    # expected: [[1, 1], [1, 1]]
