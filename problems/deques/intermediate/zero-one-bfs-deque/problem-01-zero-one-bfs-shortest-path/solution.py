"""0-1 BFS: shortest path on a directed graph with edge weights in {0, 1}."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> int:
        # TODO: 0-1 BFS — appendleft for weight-0 edges, append for weight-1 edges
        pass


if __name__ == "__main__":
    sol = Solution()
    edges = [[0, 1, 1], [0, 2, 0], [2, 1, 1], [1, 3, 0], [2, 3, 1], [3, 4, 1]]
    print(sol.shortestPath(6, edges, 0, 4))  # expected: 2
    print(sol.shortestPath(6, edges, 0, 3))  # expected: 1
    print(sol.shortestPath(6, edges, 0, 5))  # expected: -1
    print(sol.shortestPath(6, edges, 0, 0))  # expected: 0
