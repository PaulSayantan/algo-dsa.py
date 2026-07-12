"""Snakes and Ladders — LeetCode 909."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # TODO: number the board in boustrophedon order, then BFS
        pass


if __name__ == "__main__":
    sol = Solution()
    board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]
    print(sol.snakesAndLadders(board))  # expected: 4
    print(sol.snakesAndLadders([[-1, -1], [-1, 3]]))  # expected: 1
    print(sol.snakesAndLadders([[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]))  # expected: 1
