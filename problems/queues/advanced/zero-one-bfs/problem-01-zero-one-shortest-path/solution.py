"""0-1 BFS shortest path with a deque."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]]) -> int:
        # TODO: 0-1 BFS (appendleft for 0-edges, append for 1-edges)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPath(4, [[0, 1, 0], [1, 2, 1], [0, 2, 1], [2, 3, 0]]))  # expected: 1
    print(sol.shortestPath(3, [[0, 1, 1], [1, 2, 1]]))  # expected: 2
    print(sol.shortestPath(3, [[0, 1, 1]]))  # expected: -1
