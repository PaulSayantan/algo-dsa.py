"""Subarray Sum Equals K — empty solution template.

Fill in the body of `subarraySum` using a hash map of prefix-sum frequencies.
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Count contiguous subarrays of `nums` that sum to exactly `k`.

        Args:
            nums: List of integers (may include negatives and zeros).
            k: Target subarray sum.

        Returns:
            The number of contiguous, non-empty subarrays whose elements sum to k.

        Example:
            >>> Solution().subarraySum([1, 1, 1], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))   # expected: 2
    print(sol.subarraySum([1, 2, 3], 3))   # expected: 2
    print(sol.subarraySum([1, -1, 0], 0))  # expected: 3
