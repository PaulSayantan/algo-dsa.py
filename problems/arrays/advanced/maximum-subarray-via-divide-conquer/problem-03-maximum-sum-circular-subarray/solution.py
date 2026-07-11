"""Maximum Sum Circular Subarray (LeetCode 918) — divide & conquer template.

Plan:
  - Compute the ordinary maximum subarray with a divide & conquer merge
    (non-wrapping answer).
  - Compute the minimum subarray with the mirror-image merge.
  - The wrapping answer is total(nums) - min_subarray.
  - Return max(non_wrapping, wrapping), guarding the all-negative case.
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Return the maximum sum of a non-empty subarray of a circular array.

        Args:
            nums: A non-empty list of integers, treated circularly (the element
                after the last wraps to the first). Each element may be used at
                most once.

        Returns:
            The largest achievable subarray sum, considering both non-wrapping and
            wrapping subarrays.

        Example:
            >>> Solution().maxSubarraySumCircular([5, -3, 5])
            10
        """
        # TODO: implement using Maximum Subarray via Divide & Conquer
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1, -2, 3, -2]))  # expected: 3
    print(sol.maxSubarraySumCircular([5, -3, 5]))       # expected: 10
    print(sol.maxSubarraySumCircular([-3, -2, -3]))     # expected: -2
