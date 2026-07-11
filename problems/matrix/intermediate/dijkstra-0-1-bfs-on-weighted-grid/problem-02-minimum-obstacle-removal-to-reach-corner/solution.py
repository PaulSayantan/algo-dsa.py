"""Minimum Obstacle Removal to Reach Corner (LeetCode 2290).

Fill in the body using 0-1 BFS (a deque). Do not modify the signature.
"""
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """Return the minimum number of obstacle cells (value 1) that must be
        removed to travel from (0, 0) to (m-1, n-1) using 4-directional moves.

        Entering an empty cell (0) is free; entering an obstacle cell (1) costs
        one removal.

        Args:
            grid: An m x n matrix whose cells are 0 (empty) or 1 (obstacle).
                  grid[0][0] and grid[m-1][n-1] are guaranteed to be 0.

        Returns:
            The least number of obstacles that need to be removed.

        Example:
            >>> Solution().minimumObstacles([[0, 1, 1],
            ...                              [1, 1, 0],
            ...                              [1, 1, 0]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumObstacles([[0, 1, 1],
                                [1, 1, 0],
                                [1, 1, 0]]))          # expected: 2
    print(sol.minimumObstacles([[0, 1, 0, 0, 0],
                                [0, 1, 0, 1, 0],
                                [0, 0, 0, 1, 0]]))    # expected: 0
