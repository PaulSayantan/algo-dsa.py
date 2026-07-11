"""Number of Islands — LeetCode 200.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count the number of 4-directionally connected islands of '1's.

        Args:
            grid: An ``m x n`` grid whose entries are the characters '1'
                (land) or '0' (water).

        Returns:
            The number of distinct islands (connected components of land).

        Example:
            >>> Solution().numIslands([
            ...     ["1", "1", "0"],
            ...     ["0", "1", "0"],
            ...     ["0", "0", "1"],
            ... ])
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

    print(sol.numIslands([["0", "0", "0"], ["0", "0", "0"]]))
    # Expected: 0
