"""Minimum Obstacle Removal to Reach Corner — LeetCode 2290."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # TODO: 0-1 BFS — stepping into an empty cell (0) is weight 0, into an
        # obstacle (1) is weight 1; appendleft on 0, append on 1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumObstacles([[0, 1, 1], [1, 1, 0], [1, 1, 0]]))  # expected: 2
    print(sol.minimumObstacles([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))  # expected: 0
    print(sol.minimumObstacles([[0]]))  # expected: 0
    print(sol.minimumObstacles([[0, 1], [1, 0]]))  # expected: 1
    print(sol.minimumObstacles([[0, 1, 1], [1, 1, 1], [1, 1, 0]]))  # expected: 3
