"""Maximum Sum Rectangle in a 2D Matrix.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def maxSumRectangle(self, matrix: List[List[int]]) -> int:
        """Return the largest sum over all rectangular submatrices.

        Args:
            matrix: An ``n x m`` grid of integers (may include negatives),
                with at least one cell.

        Returns:
            The maximum sum achievable by any non-empty axis-aligned
            rectangular submatrix.

        Example:
            >>> Solution().maxSumRectangle([
            ...     [ 1,  2, -1, -4, -20],
            ...     [-8, -3,  4,  2,   1],
            ...     [ 3,  8, 10,  1,   3],
            ...     [-4, -1,  1,  7,  -6],
            ... ])
            29
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumRectangle([
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]))  # expected: 29
    print(sol.maxSumRectangle([[-1, -2], [-3, -4]]))  # expected: -1
