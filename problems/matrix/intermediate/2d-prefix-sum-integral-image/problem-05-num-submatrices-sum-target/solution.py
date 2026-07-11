"""Number of Submatrices That Sum to Target (LeetCode 1074).

Fill in the body of numSubmatrixSumTarget. Do not change the signature.
"""

from typing import List


class Solution:
    def numSubmatrixSumTarget(
        self, matrix: List[List[int]], target: int
    ) -> int:
        """Count non-empty submatrices whose element sum equals target.

        Args:
            matrix: An m x n grid of integers (may be negative).
            target: The desired submatrix sum.

        Returns:
            The number of distinct submatrices (by corner coordinates) that
            sum to target.

        Example:
            >>> Solution().numSubmatrixSumTarget(
            ...     [[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0)
            4
            >>> Solution().numSubmatrixSumTarget([[1, -1], [-1, 1]], 0)
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(
        Solution().numSubmatrixSumTarget(
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0
        )
    )  # expected 4
    print(Solution().numSubmatrixSumTarget([[1, -1], [-1, 1]], 0))  # expected 5
    print(Solution().numSubmatrixSumTarget([[904]], 0))  # expected 0
