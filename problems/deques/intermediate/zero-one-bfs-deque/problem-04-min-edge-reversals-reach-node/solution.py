"""Minimum edge reversals to reach a node on a directed graph (0-1 BFS)."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def minReversals(self, n: int, edges: List[List[int]], src: int, dst: int) -> int:
        # TODO: 0-1 BFS — forward arc costs 0 (appendleft), reversed arc costs 1 (append)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minReversals(4, [[0, 1], [1, 2], [3, 2]], 0, 3))  # expected: 1
    print(sol.minReversals(4, [[0, 1], [1, 2], [2, 3]], 0, 3))  # expected: 0
    print(sol.minReversals(3, [[1, 0], [2, 1]], 0, 2))  # expected: 2
    print(sol.minReversals(2, [[0, 1]], 1, 0))  # expected: 1
    print(sol.minReversals(3, [[0, 1]], 0, 2))  # expected: -1
