"""Binary Subarrays With Sum (LeetCode 930).

Fill in the body of `numSubarraysWithSum`. Do not modify the signature.
"""
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """Count contiguous subarrays of a binary array that sum to ``goal``.

        Args:
            nums: A binary array whose elements are each 0 or 1.
            goal: The target subarray sum (0 <= goal <= len(nums)).

        Returns:
            The number of non-empty contiguous subarrays whose elements sum to
            exactly ``goal``.

        Example:
            >>> Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2)
            4
        """
        # TODO: keep a running prefix sum and a hash map counting occurrences
        # of each prefix sum; for each index add count[prefix - goal].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarraysWithSum([1, 0, 1, 0, 1], 2))   # expected: 4
    print(sol.numSubarraysWithSum([0, 0, 0, 0, 0], 0))   # expected: 15
    print(sol.numSubarraysWithSum([1, 0, 1], 1))         # expected: 4
