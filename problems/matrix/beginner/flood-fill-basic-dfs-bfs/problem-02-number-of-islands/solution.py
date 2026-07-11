"""Number of Islands — LeetCode 200.

Fill in the body of `numIslands`. Do not hard-code answers; implement the
traversal so it works for any valid input.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count the connected components of land ('1') in the grid.

        Args:
            grid: An m x n grid whose cells are the strings '0' (water) or
                '1' (land). Land is connected 4-directionally.

        Returns:
            The number of islands (maximal 4-directionally connected groups
            of '1' cells).

        Example:
            grid = [["1","1","0"],
                    ["0","1","0"],
                    ["0","0","1"]]
            -> 2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    g = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(sol.numIslands(g))
    # Expected: 3
