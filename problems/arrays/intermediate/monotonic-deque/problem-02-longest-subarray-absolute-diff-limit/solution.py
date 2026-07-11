"""Longest Continuous Subarray With Absolute Diff <= Limit — LeetCode 1438.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Return the length of the longest subarray with max-min <= limit.

        Args:
            nums: The input array of integers.
            limit: The maximum allowed absolute difference between the maximum
                and minimum element of a valid subarray.

        Returns:
            The length of the longest contiguous subarray in which
            ``max(subarray) - min(subarray) <= limit``.

        Example:
            >>> Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([8, 2, 4, 7], 4))  # expected: 2
    print(sol.longestSubarray([10, 1, 2, 4, 7, 2], 5))  # expected: 4
    print(sol.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))  # expected: 3
