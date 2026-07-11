from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count the number of 4-directionally connected islands of land.

        A cell containing '1' is land and '0' is water. An island is a maximal
        group of land cells connected horizontally or vertically.

        Args:
            grid: An m x n grid where each entry is the string '0' or '1'.

        Returns:
            The number of distinct islands in the grid.

        Example:
            >>> Solution().numIslands([["1","1","0"],
            ...                        ["0","0","0"],
            ...                        ["0","0","1"]])
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(sol.numIslands(grid1))
    # Expected: 1
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(sol.numIslands(grid2))
    # Expected: 3
