"""BFS distances from a source to all nodes."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def bfsDistances(self, n: int, edges: List[List[int]], src: int) -> List[int]:
        # TODO
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.bfsDistances(5, [[0, 1], [0, 2], [1, 3], [2, 4]], 0))  # expected: [0, 1, 1, 2, 2]
    print(sol.bfsDistances(4, [[0, 1]], 0))  # expected: [0, 1, -1, -1]
