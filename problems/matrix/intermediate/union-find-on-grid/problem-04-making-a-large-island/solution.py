"""LeetCode 827 - Making a Large Island.

Solve with Union-Find on Grid: union all existing land into components with
known sizes, then for each 0 try flipping it and sum the sizes of the DISTINCT
neighboring components (+1 for the flipped cell). Return the best result.
"""
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """Return the largest island size achievable by flipping at most one 0.

        Args:
            grid: An n x n binary matrix of 0s (water) and 1s (land).

        Returns:
            The maximum island size after changing at most one 0 to 1. If the
            grid is already all 1s, this is n * n.

        Example:
            >>> Solution().largestIsland([[1, 0], [0, 1]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().largestIsland([[1, 0], [0, 1]]))  # expected: 3
    print(Solution().largestIsland([[1, 1], [1, 0]]))  # expected: 4
    print(Solution().largestIsland([[1, 1], [1, 1]]))  # expected: 4
