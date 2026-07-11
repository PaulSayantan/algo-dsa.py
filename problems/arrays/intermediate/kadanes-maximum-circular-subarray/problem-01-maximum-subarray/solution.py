"""Maximum Subarray (LeetCode 53).

Fill in the body of `maxSubArray`. Do not modify the signature.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Return the largest sum of any contiguous, non-empty subarray.

        Args:
            nums: The input integer array (may contain negatives). Length >= 1.

        Returns:
            The maximum possible sum over all contiguous, non-empty subarrays
            of ``nums``.

        Example:
            >>> Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
            6
        """
        # TODO: implement standard Kadane. Track the best sum of a subarray
        # ending at the current index (extend the previous run or restart at
        # the current element), and the best seen overall.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: 6
    print(sol.maxSubArray([1]))                               # expected: 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                  # expected: 23
