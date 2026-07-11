"""Maximum Absolute Sum of Any Subarray (LeetCode 1749).

Fill in the body of `maxAbsoluteSum`. Do not modify the signature.
"""
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """Return the largest absolute value of any subarray sum.

        The empty subarray (sum 0) is allowed, so the result is always >= 0.

        Args:
            nums: The input integer array (may contain negatives). Length >= 1.

        Returns:
            The maximum of ``abs(sum(nums[l..r]))`` over all subarrays
            ``nums[l..r]`` (including the empty subarray, whose sum is 0).

        Example:
            >>> Solution().maxAbsoluteSum([1, -3, 2, 3, -4])
            5
        """
        # TODO: run a maximizing Kadane and a minimizing Kadane together;
        # the answer is max(maxKadane, -minKadane) (>= 0 by construction).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAbsoluteSum([1, -3, 2, 3, -4]))        # expected: 5
    print(sol.maxAbsoluteSum([2, -5, 1, -4, 3, -2]))    # expected: 8
    print(sol.maxAbsoluteSum([-1, -2, -3]))             # expected: 6
