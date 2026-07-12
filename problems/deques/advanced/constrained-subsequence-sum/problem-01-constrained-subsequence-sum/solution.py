"""Constrained Subsequence Sum — LeetCode 1425."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # TODO: DP + monotonic deque for the window max of dp
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.constrainedSubsetSum([10, 2, -10, 5, 20], 2))  # expected: 37
    print(sol.constrainedSubsetSum([-1, -2, -3], 1))  # expected: -1
    print(sol.constrainedSubsetSum([10, -2, -10, -5, 20], 2))  # expected: 23
