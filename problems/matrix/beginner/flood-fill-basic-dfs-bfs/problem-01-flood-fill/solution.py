"""Flood Fill — LeetCode 733.

Fill in the body of `floodFill`. Do not hard-code answers; implement the
traversal so it works for any valid input.
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
        """Recolor the connected region containing the seed pixel.

        Args:
            image: An m x n grid of pixel values.
            sr: Row index of the starting pixel.
            sc: Column index of the starting pixel.
            color: The new color to paint the connected region.

        Returns:
            The same grid, mutated in place, with the connected region
            (all pixels 4-directionally reachable from the seed that share
            the seed's original color) repainted to `color`.

        Example:
            image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
            -> [[2,2,2],[2,2,0],[2,0,1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(sol.floodFill(grid, 1, 1, 2))
    # Expected: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
