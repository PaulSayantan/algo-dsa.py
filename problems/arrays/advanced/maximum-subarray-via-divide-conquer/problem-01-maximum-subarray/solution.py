"""Maximum Subarray (LeetCode 53) — divide & conquer template.

Fill in `maxSubArray` using the divide & conquer strategy:
  - split `nums` at the midpoint,
  - recurse on the left and right halves,
  - compute the best subarray that crosses the midpoint (best suffix of the
    left half + best prefix of the right half),
  - return the maximum of the three candidates.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum obtainable from any contiguous subarray.

        Args:
            nums: A non-empty list of integers (values may be negative).

        Returns:
            The maximum subarray sum. When every element is negative this is the
            largest single element.

        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        # TODO: implement using Maximum Subarray via Divide & Conquer
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    print(sol.maxSubArray([1]))                               # expected: 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                  # expected: 23
    print(sol.maxSubArray([-3, -1, -2]))                      # expected: -1
