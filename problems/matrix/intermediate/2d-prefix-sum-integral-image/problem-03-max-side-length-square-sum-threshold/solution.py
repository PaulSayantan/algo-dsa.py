"""Maximum Side Length of a Square with Sum <= Threshold (LeetCode 1292).

Fill in the body of maxSideLength. Do not change the signature.
"""

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        """Return the largest square side length whose sum is <= threshold.

        Args:
            mat: An m x n matrix of non-negative integers.
            threshold: The maximum allowed square sum.

        Returns:
            The maximum side length of a qualifying square, or 0 if none exists.

        Example:
            >>> Solution().maxSideLength(
            ...     [[1, 1, 3, 2, 4, 3, 2],
            ...      [1, 1, 3, 2, 4, 3, 2],
            ...      [1, 1, 3, 2, 4, 3, 2]], 4)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(
        Solution().maxSideLength(
            [
                [1, 1, 3, 2, 4, 3, 2],
                [1, 1, 3, 2, 4, 3, 2],
                [1, 1, 3, 2, 4, 3, 2],
            ],
            4,
        )
    )  # expected 2
    print(
        Solution().maxSideLength(
            [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]], 1
        )
    )  # expected 0
    print(
        Solution().maxSideLength(
            [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 6
        )
    )  # expected 3
