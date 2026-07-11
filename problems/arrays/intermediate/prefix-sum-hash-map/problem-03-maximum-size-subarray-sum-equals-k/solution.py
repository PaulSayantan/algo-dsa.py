"""Maximum Size Subarray Sum Equals k (LeetCode 325).

Fill in the body of `maxSubArrayLen`. Do not modify the signature.
"""
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        """Return the length of the longest subarray summing to ``k``.

        Args:
            nums: The input integer array (may contain negatives and zeros).
            k: The target subarray sum.

        Returns:
            The maximum length of a contiguous subarray whose elements sum to
            exactly ``k``, or 0 if no such subarray exists.

        Example:
            >>> Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3)
            4
        """
        # TODO: keep a running prefix sum and a hash map from prefix-sum value
        # to its EARLIEST index; when (running - k) was seen before, update the
        # best length with the distance between indices.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArrayLen([1, -1, 5, -2, 3], 3))   # expected: 4
    print(sol.maxSubArrayLen([-2, -1, 2, 1], 1))      # expected: 2
    print(sol.maxSubArrayLen([1, 0, -1], 0))          # expected: 3
