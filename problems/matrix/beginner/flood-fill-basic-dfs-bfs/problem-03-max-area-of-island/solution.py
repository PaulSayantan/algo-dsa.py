"""Max Area of Island — LeetCode 695.

Fill in the body of `maxAreaOfIsland`. Do not hard-code answers; implement the
traversal so it works for any valid input.
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Return the size (cell count) of the largest 4-connected island.

        Args:
            grid: An m x n binary matrix where 1 is land and 0 is water.
                Land is connected 4-directionally.

        Returns:
            The maximum number of cells in any single connected island, or 0
            if the grid contains no land.

        Example:
            grid = [[1,1,0],
                    [0,1,0],
                    [0,0,1]]
            -> 3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    g = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1],
    ]
    print(sol.maxAreaOfIsland(g))
    # Expected: 3
