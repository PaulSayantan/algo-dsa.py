"""LeetCode 59 - Spiral Matrix II.

Generate an n x n matrix filled with 1..n^2 in clockwise spiral order.
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """Build an n x n matrix filled 1..n^2 along a clockwise spiral.

        Args:
            n: The side length of the square matrix (n >= 1).

        Returns:
            An n x n list of lists where the integers 1 through n*n are
            placed following a clockwise spiral that starts at the
            top-left cell.

        Example:
            >>> Solution().generateMatrix(3)
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().generateMatrix(3))
    # Expected: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
