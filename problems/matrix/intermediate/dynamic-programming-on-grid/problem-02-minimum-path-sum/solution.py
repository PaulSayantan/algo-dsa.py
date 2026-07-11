"""Minimum Path Sum — LeetCode 64.

Find the minimum sum of numbers along a right/down path from the top-left
to the bottom-right corner of a grid.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Return the minimum path sum from top-left to bottom-right.

        Args:
            grid: An m x n grid of non-negative integers.

        Returns:
            The smallest possible sum of values along a path that moves only
            right or down from grid[0][0] to grid[m-1][n-1].

        Example:
            >>> Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))  # expected: 7
    print(sol.minPathSum([[1, 2, 3], [4, 5, 6]]))  # expected: 12
    print(sol.minPathSum([[5]]))  # expected: 5
