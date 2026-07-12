"""Shortest Subarray with Sum at Least K — LeetCode 862."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # TODO: monotonic deque over prefix sums
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestSubarray([1], 1))  # expected: 1
    print(sol.shortestSubarray([1, 2], 4))  # expected: -1
    print(sol.shortestSubarray([2, -1, 2], 3))  # expected: 3
    print(sol.shortestSubarray([-28, 81, -20, 28, -29], 89))  # expected: 3
