from typing import List


class Solution:
    def floodFill(
        self,
        image: List[List[int]],
        sr: int,
        sc: int,
        color: int,
    ) -> List[List[int]]:
        """Flood fill a connected region of same-colored pixels.

        Starting from image[sr][sc], recolor every pixel that is connected
        4-directionally (up/down/left/right) to it through pixels sharing the
        starting pixel's original color, replacing that color with `color`.

        Args:
            image: An m x n grid of integer pixel values.
            sr: Row index of the starting pixel.
            sc: Column index of the starting pixel.
            color: The new color to fill the connected region with.

        Returns:
            The modified image after performing the flood fill.

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
    # Expected: [[0, 0, 0], [0, 0, 0]]
