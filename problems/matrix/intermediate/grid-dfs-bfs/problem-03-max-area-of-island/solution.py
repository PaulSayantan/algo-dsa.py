from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Return the area of the largest 4-directionally connected island.

        A cell with value 1 is land and 0 is water. The area of an island is
        the count of land cells it contains.

        Args:
            grid: An m x n binary matrix of 0s (water) and 1s (land).

        Returns:
            The maximum island area, or 0 if the grid contains no land.

        Example:
            >>> Solution().maxAreaOfIsland([[0,0,1,0],
            ...                             [0,1,1,0],
            ...                             [0,0,0,0]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
    ]
    print(sol.maxAreaOfIsland(grid1))
    # Expected: 4
    grid2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    print(sol.maxAreaOfIsland(grid2))
    # Expected: 0
