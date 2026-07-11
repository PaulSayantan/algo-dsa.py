"""Reshape the Matrix (LeetCode 566).

Fill in the body of ``matrixReshape`` using Row/Column Traversal.
"""

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """Reshape ``mat`` into an ``r x c`` matrix in row-major order.

        Args:
            mat: The original ``m x n`` matrix.
            r: Desired number of rows in the reshaped matrix.
            c: Desired number of columns in the reshaped matrix.

        Returns:
            The reshaped ``r x c`` matrix if ``m * n == r * c``; otherwise the
            original matrix ``mat`` unchanged.

        Example:
            >>> Solution().matrixReshape([[1, 2], [3, 4]], 1, 4)
            [[1, 2, 3, 4]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.matrixReshape([[1, 2], [3, 4]], 1, 4))        # expected: [[1, 2, 3, 4]]
    print(sol.matrixReshape([[1, 2], [3, 4]], 2, 4))        # expected: [[1, 2], [3, 4]]
    print(sol.matrixReshape([[1, 2, 3], [4, 5, 6]], 3, 2))  # expected: [[1, 2], [3, 4], [5, 6]]
