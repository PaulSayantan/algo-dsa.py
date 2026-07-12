"""Nearest Exit from Entrance in Maze — LeetCode 1926."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # TODO: 4-directional BFS from entrance; first non-entrance border cell wins
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]))  # expected: 1
    print(sol.nearestExit([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]], [1, 0]))  # expected: 2
    print(sol.nearestExit([[".", "+"]], [0, 0]))  # expected: -1
