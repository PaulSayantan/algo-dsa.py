"""Max Sum of Rectangle No Larger Than K (LeetCode 363).

Fill in the body of maxSumSubmatrix. Do not change the signature.
"""

from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """Return the maximum rectangle sum that is <= k.

        Args:
            matrix: An m x n grid of integers (may be negative).
            k: The upper bound the rectangle sum must not exceed.

        Returns:
            The largest achievable rectangle sum that does not exceed k. It is
            guaranteed at least one rectangle has sum <= k.

        Example:
            >>> Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2)
            2
            >>> Solution().maxSumSubmatrix([[2, 2, -1]], 3)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().maxSumSubmatrix([[1, 0, 1], [0, -2, 3]], 2))  # expected 2
    print(Solution().maxSumSubmatrix([[2, 2, -1]], 3))  # expected 3
    print(
        Solution().maxSumSubmatrix(
            [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 8
        )
    )  # expected 8
