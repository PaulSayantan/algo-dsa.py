"""LeetCode 200 - Number of Islands.

Solve with Union-Find on Grid: flatten each cell (r, c) to id r * cols + c,
union adjacent land cells, then count distinct land roots.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count the number of 4-directionally connected islands of '1' cells.

        Args:
            grid: An m x n grid where each entry is '1' (land) or '0' (water).

        Returns:
            The number of distinct islands (connected components of land).

        Example:
            >>> Solution().numIslands([
            ...     ["1", "1", "0", "0", "0"],
            ...     ["1", "1", "0", "0", "0"],
            ...     ["0", "0", "1", "0", "0"],
            ...     ["0", "0", "0", "1", "1"],
            ... ])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sample = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(Solution().numIslands(sample))  # expected: 1
