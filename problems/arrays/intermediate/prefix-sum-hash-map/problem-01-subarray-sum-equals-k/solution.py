"""Subarray Sum Equals K (LeetCode 560).

Fill in the body of `subarraySum`. Do not modify the signature.
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Count the number of contiguous subarrays whose sum equals ``k``.

        Args:
            nums: The input integer array (may contain negatives and zeros).
            k: The target subarray sum.

        Returns:
            The total number of contiguous, non-empty subarrays of ``nums``
            whose elements sum to exactly ``k``.

        Example:
            >>> Solution().subarraySum([1, 1, 1], 2)
            2
        """
        # TODO: implement using a running prefix sum and a hash map that
        # counts how many times each prefix sum has been seen.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))      # expected: 2
    print(sol.subarraySum([1, 2, 3], 3))      # expected: 2
    print(sol.subarraySum([1, -1, 0], 0))     # expected: 3
