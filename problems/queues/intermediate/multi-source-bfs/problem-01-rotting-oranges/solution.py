"""Rotting Oranges — LeetCode 994."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # TODO: multi-source BFS from all rotten oranges
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # expected: 4
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # expected: -1
    print(sol.orangesRotting([[0, 2]]))  # expected: 0
