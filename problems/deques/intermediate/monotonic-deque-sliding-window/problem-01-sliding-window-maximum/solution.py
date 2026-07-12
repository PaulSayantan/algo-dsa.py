"""Sliding Window Maximum — LeetCode 239."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: keep a decreasing monotonic deque of indices; the front is the max
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [3, 3, 5, 5, 6, 7]
    print(sol.maxSlidingWindow([9, 11], 2))  # expected: [11]
    print(sol.maxSlidingWindow([4, -2], 2))  # expected: [4]
    print(sol.maxSlidingWindow([1, 3, 1, 2, 0, 5], 1))  # expected: [1, 3, 1, 2, 0, 5]
