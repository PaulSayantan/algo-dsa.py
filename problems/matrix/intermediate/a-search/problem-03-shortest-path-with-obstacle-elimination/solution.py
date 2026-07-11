"""Shortest Path in a Grid with Obstacles Elimination — LeetCode 1293.

Empty solution template. Fill in `shortestPath`.
"""

from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """Return the minimum number of steps from (0, 0) to (m-1, n-1), allowed to
        eliminate at most k obstacles along the way, or -1 if unreachable.

        Moves are 4-directional. Stepping onto a cell with value 1 consumes one of the
        remaining eliminations; stepping onto a 0 consumes none.

        Args:
            grid: An m x n matrix of 0 (empty) and 1 (obstacle) cells.
            k: The maximum number of obstacles that may be eliminated.

        Returns:
            The fewest steps to reach the bottom-right corner, or -1 if impossible.

        Example:
            >>> Solution().shortestPath(
            ...     [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1)
            6
        """
        # TODO: implement using A* Search over states (row, col, eliminations_left).
        pass


if __name__ == "__main__":
    print(Solution().shortestPath(
        [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1))
    # Expected: 6
    print(Solution().shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1))
    # Expected: -1
