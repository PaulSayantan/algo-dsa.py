"""LeetCode 1074 — Number of Submatrices That Sum to Target.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """Count non-empty submatrices whose element sum equals ``target``.

        Args:
            matrix: An ``n x m`` grid of integers (may include negatives).
            target: The desired submatrix sum.

        Returns:
            The number of distinct submatrices (by coordinate) that sum to
            ``target``.

        Example:
            >>> Solution().numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))  # expected: 4
    print(sol.numSubmatrixSumTarget([[1, -1], [-1, 1]], 0))                 # expected: 5
    print(sol.numSubmatrixSumTarget([[904]], 0))                            # expected: 0
