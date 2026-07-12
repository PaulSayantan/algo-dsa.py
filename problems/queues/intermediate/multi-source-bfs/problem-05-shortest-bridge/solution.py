"""Shortest Bridge — LeetCode 934."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # TODO: flood-fill one island, then multi-source BFS to the other
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))  # expected: 2
    print(sol.shortestBridge([[0, 1], [1, 0]]))  # expected: 1
    print(sol.shortestBridge([[1, 0, 0], [0, 0, 0], [0, 0, 1]]))  # expected: 3
