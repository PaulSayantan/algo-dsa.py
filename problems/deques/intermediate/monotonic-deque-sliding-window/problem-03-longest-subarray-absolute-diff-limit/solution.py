"""Longest Continuous Subarray With Absolute Diff <= Limit — LeetCode 1438."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # TODO: two monotonic deques (max + min); shrink left while max - min > limit
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestSubarray([8, 2, 4, 7], 4))  # expected: 2
    print(sol.longestSubarray([10, 1, 2, 4, 7, 2], 5))  # expected: 4
    print(sol.longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0))  # expected: 3
    print(sol.longestSubarray([1], 0))  # expected: 1
    print(sol.longestSubarray([1, 5, 6, 7, 8, 10, 6, 5, 6], 4))  # expected: 5
