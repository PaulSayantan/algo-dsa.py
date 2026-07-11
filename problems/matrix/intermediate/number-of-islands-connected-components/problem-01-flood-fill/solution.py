"""Flood Fill — LeetCode 733.

Empty solution template. Fill in the body yourself.
"""

from typing import List


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        """Flood fill the region connected to (sr, sc) with ``color``.

        Args:
            image: An ``m x n`` grid of integer pixel values.
            sr: Row index of the starting pixel.
            sc: Column index of the starting pixel.
            color: The new color to paint the connected region with.

        Returns:
            The same grid (modified in place is acceptable) after painting
            every 4-directionally connected pixel that shared the starting
            pixel's original color.

        Example:
            >>> Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
            [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
    # Expected: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    print(sol.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
    # Expected: [[0, 0, 0], [0, 0, 0]]  (new color == old color, no change)

    print(sol.floodFill([[0, 0, 0], [0, 1, 0]], 1, 1, 2))
    # Expected: [[0, 0, 0], [0, 2, 0]]
