"""Minimum Cost to Make at Least One Valid Path in a Grid — LeetCode 1368."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # TODO: 0-1 BFS — following the arrow costs 0, redirecting costs 1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minCost([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]))  # expected: 3
    print(sol.minCost([[1, 1, 3], [3, 2, 2], [1, 1, 4]]))  # expected: 0
    print(sol.minCost([[1, 2], [4, 3]]))  # expected: 1
    print(sol.minCost([[1]]))  # expected: 0
