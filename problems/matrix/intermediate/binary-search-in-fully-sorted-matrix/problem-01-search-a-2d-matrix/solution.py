"""Search a 2D Matrix (LeetCode 74).

Empty solution template — fill in the body yourself.
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Return True if ``target`` appears in the fully-sorted matrix.

        The matrix is sorted in row-major order: each row is non-decreasing and
        every row's first element exceeds the previous row's last element. Treat
        it as a virtual sorted array of ``m * n`` elements and binary search,
        mapping a flat index ``idx`` to the cell ``matrix[idx // n][idx % n]``.

        Args:
            matrix: An ``m x n`` grid sorted in row-major order.
            target: The integer value to search for.

        Returns:
            True if ``target`` is present in ``matrix``, otherwise False.

        Example:
            >>> Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20]], 16)
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(Solution().searchMatrix(grid, 3))    # expected: True
    print(Solution().searchMatrix(grid, 13))   # expected: False
