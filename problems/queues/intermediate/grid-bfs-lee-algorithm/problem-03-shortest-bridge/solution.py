"""Shortest Bridge — LeetCode 934."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # TODO: flood-fill island 1 into a BFS queue, then Lee-expand to island 2
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestBridge([[0, 1], [1, 0]]))  # expected: 1
    print(sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))  # expected: 2
    print(sol.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))  # expected: 1
