"""Throttling Gateway — multi-window request throttling (HackerRank classic)."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def droppedRequests(self, requestTime: List[int]) -> int:
        # TODO: per-window queues (1s, 10s, 60s); on each arrival pop timestamps
        # that left each window, then drop if any queue exceeds its limit
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.droppedRequests([1, 1, 1, 1, 2]))  # expected: 1
    print(sol.droppedRequests([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # expected: 0
    print(sol.droppedRequests([1, 1, 1, 2, 2, 2, 3, 3, 3]))  # expected: 0
    print(sol.droppedRequests([5] * 25))  # expected: 22
