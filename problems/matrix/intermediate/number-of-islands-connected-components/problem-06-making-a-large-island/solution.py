"""Making A Large Island — LeetCode 827.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """Largest island size achievable by flipping at most one 0 to 1.

        Args:
            grid: An ``n x n`` binary matrix of ``0`` (water) and ``1`` (land).

        Returns:
            The size of the largest 4-directionally connected island after
            changing at most one ``0`` cell to ``1``. If the grid is already
            all land, returns ``n * n``.

        Example:
            >>> Solution().largestIsland([[1, 0], [0, 1]])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    print(sol.largestIsland([[1, 0], [0, 1]]))
    # Expected: 3

    print(sol.largestIsland([[1, 1], [1, 0]]))
    # Expected: 4

    print(sol.largestIsland([[1, 1], [1, 1]]))
    # Expected: 4
