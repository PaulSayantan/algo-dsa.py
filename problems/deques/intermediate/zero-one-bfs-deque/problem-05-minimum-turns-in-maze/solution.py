"""Minimum turns to cross a maze — 0-1 BFS over (row, col, direction) states."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def minTurns(self, grid: List[List[int]]) -> int:
        # TODO: 0-1 BFS on states (r, c, dir) — same direction weight 0 (appendleft),
        # a turn weight 1 (append); a sentinel direction marks the free first move
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minTurns([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # expected: 1
    print(sol.minTurns([[0, 0, 0, 0]]))  # expected: 0
    print(sol.minTurns([[0]]))  # expected: 0
    print(sol.minTurns([[0, 1, 0], [0, 1, 0], [0, 0, 0]]))  # expected: 1
    print(sol.minTurns([[0, 1], [1, 0]]))  # expected: -1
