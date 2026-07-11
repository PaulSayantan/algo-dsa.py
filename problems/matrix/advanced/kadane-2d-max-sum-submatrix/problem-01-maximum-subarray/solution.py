"""LeetCode 53 — Maximum Subarray.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum of any contiguous non-empty subarray.

        This is the 1D Kadane subroutine that Kadane 2D calls once per
        (top, bottom) row pair.

        Args:
            nums: A non-empty list of integers (may include negatives).

        Returns:
            The maximum possible sum over all contiguous subarrays of ``nums``.

        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    print(sol.maxSubArray([1]))                                # expected: 1
    print(sol.maxSubArray([-3, -1, -2]))                       # expected: -1
