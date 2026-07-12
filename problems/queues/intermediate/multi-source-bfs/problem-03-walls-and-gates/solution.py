"""Walls and Gates — LeetCode 286."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> List[List[int]]:
        # TODO: multi-source BFS seeded from every gate (0)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.wallsAndGates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]))  # expected: [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
    print(sol.wallsAndGates([[0, 2147483647], [-1, 2147483647]]))  # expected: [[0, 1], [-1, 2]]
    print(sol.wallsAndGates([[2147483647, -1], [-1, 0]]))  # expected: [[2147483647, -1], [-1, 0]]
