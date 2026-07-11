"""Minimum Operations to Make the Array K-Increasing (LeetCode 2111).

Empty solution template — fill in the logic yourself.
"""
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        """Return the minimum number of element changes to make arr K-increasing.

        arr is K-increasing iff arr[i - k] <= arr[i] for every i in [k, n-1].
        One operation replaces a single element with any positive integer.

        Args:
            arr: A 0-indexed list of positive integers.
            k: The stride linking indices that must be non-decreasing.

        Returns:
            The minimum number of operations (single-element changes).

        Example:
            >>> Solution().kIncreasing([5, 4, 3, 2, 1], 1)
            4
            >>> Solution().kIncreasing([4, 1, 5, 2, 6, 2], 2)
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kIncreasing([5, 4, 3, 2, 1], 1))     # expected: 4
    print(sol.kIncreasing([4, 1, 5, 2, 6, 2], 2))  # expected: 0
    print(sol.kIncreasing([4, 1, 5, 2, 6, 2], 3))  # expected: 2
