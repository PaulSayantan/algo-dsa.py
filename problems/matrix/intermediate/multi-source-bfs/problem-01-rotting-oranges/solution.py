"""Rotting Oranges — LeetCode 994.

Empty solution template. Fill in `orangesRotting`.
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Return the minimum number of minutes until no fresh orange remains.

        Every rotten orange (value 2) begins rotting simultaneously at minute 0.
        Each minute, a fresh orange (value 1) that is 4-directionally adjacent to a
        rotten orange also rots. If at least one fresh orange can never be reached,
        return -1.

        Args:
            grid: An m x n grid where each cell is 0 (empty), 1 (fresh), or 2 (rotten).

        Returns:
            The minimum number of minutes until no fresh orange remains, or -1 if
            some fresh orange can never rot.

        Example:
            >>> Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
            4
        """
        # TODO: implement using Multi-Source BFS.
        pass


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(Solution().orangesRotting(grid))  # Expected: 4
    print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # Expected: -1
    print(Solution().orangesRotting([[0, 2]]))  # Expected: 0
