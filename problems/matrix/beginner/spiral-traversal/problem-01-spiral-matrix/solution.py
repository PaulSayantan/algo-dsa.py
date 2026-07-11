"""LeetCode 54 - Spiral Matrix.

Return all elements of an m x n matrix in clockwise spiral order.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Return the matrix elements in clockwise spiral order.

        Args:
            matrix: A non-empty m x n grid of integers.

        Returns:
            A list containing every element of ``matrix`` exactly once,
            ordered by a clockwise spiral that starts at the top-left cell.

        Example:
            >>> Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(grid))
    # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
