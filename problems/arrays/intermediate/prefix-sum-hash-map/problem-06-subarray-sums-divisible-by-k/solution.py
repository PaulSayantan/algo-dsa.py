"""Subarray Sums Divisible by K (LeetCode 974).

Fill in the body of `subarraysDivByK`. Do not modify the signature.
"""
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """Count contiguous subarrays whose sum is divisible by ``k``.

        Args:
            nums: The input integer array (may contain negatives).
            k: The divisor (k >= 2).

        Returns:
            The number of non-empty contiguous subarrays of ``nums`` whose sum
            is divisible by ``k``.

        Example:
            >>> Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)
            7
        """
        # TODO: track the running prefix sum's remainder mod k (normalized to
        # 0..k-1) and a hash map counting how many prefixes produced each
        # remainder; for each index add count[remainder] before incrementing it.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))   # expected: 7
    print(sol.subarraysDivByK([5], 9))                    # expected: 0
    print(sol.subarraysDivByK([-1, 2, 9], 2))             # expected: 2
