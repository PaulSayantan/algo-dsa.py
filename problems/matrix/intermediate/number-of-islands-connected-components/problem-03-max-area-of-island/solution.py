"""Max Area of Island — LeetCode 695.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Return the size (cell count) of the largest 4-connected island.

        Args:
            grid: An ``m x n`` binary matrix of ``0`` (water) and ``1`` (land).

        Returns:
            The maximum number of land cells in any single 4-directionally
            connected island, or ``0`` if the grid has no land.

        Example:
            >>> Solution().maxAreaOfIsland([[1, 1, 0, 0, 1], [1, 0, 0, 1, 1]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    print(sol.maxAreaOfIsland(grid1))
    # Expected: 6

    print(sol.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
    # Expected: 0

    print(sol.maxAreaOfIsland([[1, 1, 0, 0, 1], [1, 0, 0, 1, 1]]))
    # Expected: 3
