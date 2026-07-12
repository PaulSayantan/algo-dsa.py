"""Shortest Path in Binary Matrix — LeetCode 1091."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # TODO: 8-directional BFS
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0, 1], [1, 0]]))  # expected: 2
    print(sol.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))  # expected: 4
    print(sol.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))  # expected: -1
