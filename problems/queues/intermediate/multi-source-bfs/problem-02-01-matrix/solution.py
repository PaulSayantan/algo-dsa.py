"""01 Matrix — LeetCode 542."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # TODO: multi-source BFS seeded from all zeros
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # expected: [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))  # expected: [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
