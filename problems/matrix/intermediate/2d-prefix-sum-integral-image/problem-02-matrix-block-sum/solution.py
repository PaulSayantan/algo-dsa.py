"""Matrix Block Sum (LeetCode 1314).

Fill in the body of matrixBlockSum. Do not change the signature.
"""

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        """Return the clamped block-sum matrix.

        For each cell (i, j), answer[i][j] is the sum of mat[r][c] for every
        valid (r, c) with i-k <= r <= i+k and j-k <= c <= j+k.

        Args:
            mat: An m x n matrix of integers.
            k: Non-negative block radius (Chebyshev distance).

        Returns:
            An m x n matrix of block sums.

        Example:
            >>> Solution().matrixBlockSum(
            ...     [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
            [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
    # expected [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
    print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2))
    # expected [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
