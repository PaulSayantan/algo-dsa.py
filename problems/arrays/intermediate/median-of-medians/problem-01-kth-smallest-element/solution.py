"""Kth Smallest Element in an Array.

Find the k-th smallest element (1-indexed) in worst-case O(n) time using the
Median of Medians deterministic selection algorithm.
"""
from typing import List


class Solution:
    def kth_smallest(self, nums: List[int], k: int) -> int:
        """Return the k-th smallest element of ``nums`` (1-indexed).

        Args:
            nums: Array of integers (may contain duplicates).
            k: 1-indexed rank; ``k == 1`` requests the minimum element.

        Returns:
            The value that would appear at index ``k - 1`` in the sorted array.

        Example:
            >>> Solution().kth_smallest([12, 3, 5, 7, 4, 19, 26], 3)
            5
        """
        # TODO: implement using Median of Medians selection
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kth_smallest([12, 3, 5, 7, 4, 19, 26], 3))  # expected: 5
    print(sol.kth_smallest([7, 10, 4, 3, 20, 15], 4))     # expected: 10
    print(sol.kth_smallest([2, 2, 3], 2))                 # expected: 2
