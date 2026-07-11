"""LeetCode 363 — Max Sum of Rectangle No Larger Than K.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """Return the largest rectangle sum that does not exceed ``k``.

        Args:
            matrix: An ``m x n`` grid of integers (may include negatives).
            k: The upper bound; the returned sum must be ``<= k``.

        Returns:
            The maximum sum over all non-empty rectangular submatrices whose
            sum is at most ``k``. Guaranteed such a rectangle exists.

        Example:
            >>> Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))                 # expected: 2
    print(sol.maxSumSubmatrix([[2, 2, -1]], 3))                            # expected: 3
    print(sol.maxSumSubmatrix([[1, 2, -1], [-3, 4, 2], [1, -1, 5]], 8))    # expected: 8
