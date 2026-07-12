"""Snakes and Ladders — LeetCode 909."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # TODO: BFS over squares 1..n*n; die rolls give up to 6 neighbors,
        # redirected by any snake/ladder on the landing square
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.snakesAndLadders([
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]))  # expected: 4
    print(sol.snakesAndLadders([[-1, -1], [-1, 3]]))  # expected: 1
    print(sol.snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]))  # expected: -1
    print(sol.snakesAndLadders([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]))  # expected: 2
