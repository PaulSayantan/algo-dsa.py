"""Shortest Subarray With Range At Least K (two-deque variable window)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # TODO: two monotonic deques (window max & min); shrink while max - min >= k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestSubarray([1, 3, 6, 2, 4], 5))  # expected: 3
    print(sol.shortestSubarray([4, 1, 7, 2], 3))  # expected: 2
    print(sol.shortestSubarray([1, 2, 3], 10))  # expected: -1
    print(sol.shortestSubarray([8, 2, 4, 7], 4))  # expected: 2
    print(sol.shortestSubarray([5, 5, 5, 5], 1))  # expected: -1
