"""Sliding Window Rate Limiter — sliding-window-log throttling."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def rateLimit(self, requests: List[int], limit: int, window: int) -> List[bool]:
        # TODO: queue of allowed timestamps; pop fronts <= t - window,
        # allow only while the queue length stays below `limit`
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rateLimit([1, 2, 3, 11, 12], 2, 5))  # expected: [True, True, False, True, True]
    print(sol.rateLimit([], 2, 5))  # expected: []
    print(sol.rateLimit([1, 1, 1, 1], 2, 10))  # expected: [True, True, False, False]
    print(sol.rateLimit([5, 10, 15, 20], 1, 5))  # expected: [True, True, True, True]
