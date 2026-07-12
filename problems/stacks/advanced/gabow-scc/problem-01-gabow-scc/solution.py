"""Strongly Connected Components — Gabow's two-stack algorithm."""
from typing import List


class Solution:
    def scc(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # TODO: Gabow with a path stack and a boundary stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.scc(5, [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]))  # expected: [[0, 1, 2], [3], [4]]
    print(sol.scc(4, [[0, 1], [1, 2], [2, 3]]))  # expected: [[0], [1], [2], [3]]
    print(sol.scc(3, [[0, 1], [1, 2], [2, 0]]))  # expected: [[0, 1, 2]]
