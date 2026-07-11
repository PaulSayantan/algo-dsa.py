"""Shortest Path in a Grid with Obstacles Elimination (LeetCode 1293).

Fill in the body using the Lee Algorithm over an augmented (row, col, k) state.
Do not modify the signature.
"""
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """Return the fewest steps from top-left to bottom-right removing <= k walls.

        You may pass through (eliminate) at most k obstacle cells (value 1).
        Moves are 4-directional and each costs one step.

        Args:
            grid: An m x n matrix of 0 (empty) and 1 (obstacle) cells.
            k: The maximum number of obstacles that may be eliminated.

        Returns:
            The minimum number of steps to reach (m-1, n-1) from (0, 0), or -1
            if the target cannot be reached even after removing up to k walls.

        Example:
            >>> Solution().shortestPath([[0, 0, 0],
            ...                          [1, 1, 0],
            ...                          [0, 0, 0],
            ...                          [0, 1, 1],
            ...                          [0, 0, 0]], 1)
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPath([[0, 0, 0],
                            [1, 1, 0],
                            [0, 0, 0],
                            [0, 1, 1],
                            [0, 0, 0]], 1))   # expected: 6
    print(sol.shortestPath([[0, 1, 1],
                            [1, 1, 1],
                            [1, 0, 0]], 1))   # expected: -1
