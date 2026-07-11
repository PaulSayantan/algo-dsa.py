"""Longest Continuous Subarray With Absolute Diff <= Limit (LeetCode 1438).

Approach to implement: build a range-max and a range-min Sparse Table for O(1)
window extremes, then binary-search the longest feasible window length.
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """Return the length of the longest subarray with max - min <= limit.

        Args:
            nums: The input integer array.
            limit: The maximum allowed absolute difference between the
                maximum and minimum element of a chosen subarray.

        Returns:
            The length of the longest contiguous subarray satisfying the limit.

        Example:
            >>> Solution().longestSubarray([8, 2, 4, 7], 4)
            2
            >>> Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().longestSubarray([8, 2, 4, 7], 4))         # Expected: 2
    print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5))  # Expected: 4
    print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))  # Expected: 3
