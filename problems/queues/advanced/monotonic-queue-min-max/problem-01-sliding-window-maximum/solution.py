"""Sliding Window Maximum — LeetCode 239."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: monotonic decreasing deque of indices
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindow([1], 1))  # expected: [1]
    print(sol.maxSlidingWindow([9, 8, 7, 6], 2))  # expected: [9, 8, 7]
