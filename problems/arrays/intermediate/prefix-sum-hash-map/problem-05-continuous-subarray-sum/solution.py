"""Continuous Subarray Sum (LeetCode 523).

Fill in the body of `checkSubarraySum`. Do not modify the signature.
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """Return True if some length >= 2 subarray sums to a multiple of ``k``.

        Args:
            nums: The input array of non-negative integers.
            k: The divisor; a good subarray's sum must be a multiple of k.

        Returns:
            True if there exists a contiguous subarray of length at least 2
            whose sum is a multiple of ``k``; otherwise False.

        Example:
            >>> Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
            True
        """
        # TODO: track the running prefix sum modulo k and a hash map from each
        # remainder to its EARLIEST index (seed remainder 0 -> index -1). If a
        # remainder repeats with an index gap of at least 2, return True.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))    # expected: True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))    # expected: True
    print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))   # expected: False
