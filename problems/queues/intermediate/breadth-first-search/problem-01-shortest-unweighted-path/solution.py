"""Shortest path length in an unweighted graph via BFS."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> int:
        # TODO: BFS with a distance array
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPath(6, [[0, 1], [1, 2], [2, 3], [0, 4], [4, 3], [3, 5]], 0, 5))  # expected: 3
    print(sol.shortestPath(4, [[0, 1], [2, 3]], 0, 3))  # expected: -1
    print(sol.shortestPath(3, [[0, 1], [1, 2]], 0, 2))  # expected: 2
