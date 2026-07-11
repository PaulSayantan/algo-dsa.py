"""As Far from Land as Possible — LeetCode 1162.

Empty solution template. Fill in `maxDistance`.
"""

from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """Return the largest distance from any water cell to its nearest land cell.

        Distance is Manhattan / 4-directional step distance. If the grid has no land
        or no water, return -1.

        Args:
            grid: An n x n grid where 0 is water and 1 is land.

        Returns:
            The maximum over all water cells of the distance to the nearest land cell,
            or -1 if the grid contains no water or no land.

        Example:
            >>> Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
            2
        """
        # TODO: implement using Multi-Source BFS.
        pass


if __name__ == "__main__":
    print(Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))  # Expected: 2
    print(Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))  # Expected: 4
    print(Solution().maxDistance([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # Expected: -1
