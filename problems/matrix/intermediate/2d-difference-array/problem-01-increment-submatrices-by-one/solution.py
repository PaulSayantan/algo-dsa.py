"""Increment Submatrices by One (LeetCode 2536).

Add 1 to every cell of each queried submatrix, then return the final grid.
Solve with a 2D difference array + prefix-sum reconstruction.
"""

from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """Return the n x n grid after applying every rectangle +1 update.

        Args:
            n: Side length of the square grid, initially all zeros.
            queries: List of [row1, col1, row2, col2] inclusive rectangle
                corners; each query adds 1 to every cell inside the rectangle.

        Returns:
            The n x n matrix (list of lists) after all queries are applied.

        Example:
            >>> Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]])
            [[1, 1, 0], [1, 2, 1], [0, 1, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]))
    # Expected: [[1, 1, 0], [1, 2, 1], [0, 1, 1]]

    print(sol.rangeAddQueries(2, [[0, 0, 1, 1]]))
    # Expected: [[1, 1], [1, 1]]
