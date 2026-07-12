"""Sliding Window Minimum (CSES-style)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: keep an increasing monotonic deque of indices; the front is the min
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # expected: [-1, -3, -3, -3, 3, 3]
    print(sol.minSlidingWindow([2, 1, 4, 5, 3, 4, 1, 2], 2))  # expected: [1, 1, 4, 3, 3, 1, 1]
    print(sol.minSlidingWindow([5, 5, 5], 2))  # expected: [5, 5]
