"""Minimum Knight Moves — LeetCode 1197."""
from collections import deque  # noqa: F401


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # TODO: BFS over the 8 knight moves; fold target into one quadrant
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minKnightMoves(2, 1))  # expected: 1
    print(sol.minKnightMoves(5, 5))  # expected: 4
    print(sol.minKnightMoves(0, 0))  # expected: 0
    print(sol.minKnightMoves(1, 1))  # expected: 2
