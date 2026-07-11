"""Subarray Sum Equals K — LeetCode 560.

Fill in the body of `subarraySum`. Do not change the signature.
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """Return the number of contiguous subarrays whose sum equals ``k``.

        Args:
            nums: A list of integers (may include negatives and zeros).
            k: The target subarray sum.

        Returns:
            The count of non-empty contiguous subarrays that sum to ``k``.

        Example:
            >>> Solution().subarraySum([1, 1, 1], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraySum([1, 1, 1], 2))    # expected: 2
    print(sol.subarraySum([1, 2, 3], 3))    # expected: 2
    print(sol.subarraySum([1, -1, 0], 0))   # expected: 3
