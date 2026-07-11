"""Minimum Sum Circular Subarray (mirror of LeetCode 918).

Fill in the body of `minSubarraySumCircular`. Do not modify the signature.
"""
from typing import List


class Solution:
    def minSubarraySumCircular(self, nums: List[int]) -> int:
        """Return the min sum of a non-empty subarray of a circular array.

        Args:
            nums: The input integer array, treated as circular so the element
                after ``nums[i]`` is ``nums[(i + 1) % len(nums)]``. Length >= 1.

        Returns:
            The minimum sum over all non-empty subarrays, where a subarray may
            wrap around from the end to the beginning but uses each element at
            most once.

        Example:
            >>> Solution().minSubarraySumCircular([-5, 3, 4, -2])
            -7
        """
        # TODO: compute minKadane(nums) for the non-wrapping case and
        # total - maxKadane(nums) for the wrapping case; return the smaller.
        # Guard the all-positive case: if minKadane > 0, return minKadane.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSubarraySumCircular([-5, 3, 4, -2]))   # expected: -7
    print(sol.minSubarraySumCircular([1, 2, 3]))        # expected: 1
    print(sol.minSubarraySumCircular([5, -3, 5]))       # expected: -3
