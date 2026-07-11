"""Maximum Sum Circular Subarray (LeetCode 918).

Fill in the body of `maxSubarraySumCircular`. Do not modify the signature.
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Return the max sum of a non-empty subarray of a circular array.

        Args:
            nums: The input integer array, treated as circular so the element
                after ``nums[i]`` is ``nums[(i + 1) % len(nums)]``. Length >= 1.

        Returns:
            The maximum sum over all non-empty subarrays, where a subarray may
            wrap around from the end to the beginning but uses each element at
            most once.

        Example:
            >>> Solution().maxSubarraySumCircular([5, -3, 5])
            10
        """
        # TODO: compute maxKadane(nums) for the non-wrapping case and
        # total - minKadane(nums) for the wrapping case; return the larger.
        # Guard the all-negative case: if maxKadane < 0, return maxKadane.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1, -2, 3, -2]))   # expected: 3
    print(sol.maxSubarraySumCircular([5, -3, 5]))       # expected: 10
    print(sol.maxSubarraySumCircular([-3, -2, -3]))     # expected: -2
