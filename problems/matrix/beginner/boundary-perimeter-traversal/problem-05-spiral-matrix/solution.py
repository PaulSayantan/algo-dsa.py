"""Spiral Matrix (LeetCode 54).

Fill in the body of `Solution.spiralOrder`. Do not change the signature.
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Return all elements of ``matrix`` in clockwise spiral order.

        The traversal starts at the top-left corner, walks the outer ring
        clockwise, then spirals inward ring by ring until every cell has been
        visited exactly once.

        Args:
            matrix: An ``m x n`` rectangular matrix of integers with ``m, n >= 1``.

        Returns:
            A list of all ``m * n`` elements in spiral (clockwise, inward) order.

        Example:
            >>> Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            [1, 2, 3, 6, 9, 8, 7, 4, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(Solution().spiralOrder(grid))
    # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    print(Solution().spiralOrder([[7], [9], [6]]))
    # Expected: [7, 9, 6]
