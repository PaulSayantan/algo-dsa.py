"""Maximum Subarray — LeetCode 53.

Empty solution template. Solve it with Divide and Conquer (left / right /
crossing the midpoint), not Kadane's algorithm.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum of any contiguous non-empty subarray.

        Use Divide and Conquer: the answer for a range is the max of the best
        subarray in the left half, the best in the right half, and the best
        subarray that crosses the midpoint.

        Args:
            nums: Non-empty list of integers (may include negatives).

        Returns:
            The maximum contiguous subarray sum.

        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
            >>> Solution().maxSubArray([-3, -1, -2])
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    print(sol.maxSubArray([1]))                              # expected: 1
    print(sol.maxSubArray([-3, -1, -2]))                     # expected: -1
