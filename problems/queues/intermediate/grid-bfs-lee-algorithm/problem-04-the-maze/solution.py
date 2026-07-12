"""The Maze — LeetCode 490."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # TODO: BFS where each edge rolls until a wall; enqueue stopping cells
        pass


if __name__ == "__main__":
    sol = Solution()
    maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]
    print(sol.hasPath(maze, [0, 4], [4, 4]))  # expected: True
    print(sol.hasPath(maze, [0, 4], [3, 2]))  # expected: False
    print(sol.hasPath([[0, 0], [0, 0]], [0, 0], [1, 1]))  # expected: True
