"""Unique Paths II — LeetCode 63.

Count distinct right/down paths from the top-left to the bottom-right of a
grid where cells marked 1 are obstacles that cannot be entered.
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """Return the number of obstacle-free right/down paths.

        Args:
            obstacleGrid: An m x n grid where 0 is a free cell and 1 is an
                obstacle that cannot be part of any path.

        Returns:
            The number of distinct paths from the top-left to the
            bottom-right corner that move only right or down and never enter
            an obstacle cell. Returns 0 if the start or end cell is blocked.

        Example:
            >>> Solution().uniquePathsWithObstacles(
            ...     [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            ... )
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(sol.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # expected: 1
    print(sol.uniquePathsWithObstacles([[1]]))  # expected: 0
