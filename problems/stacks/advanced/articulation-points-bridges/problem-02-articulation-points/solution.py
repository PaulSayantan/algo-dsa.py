"""Articulation points (cut vertices) of an undirected graph."""
from typing import List


class Solution:
    def articulationPoints(self, n: int, edges: List[List[int]]) -> List[int]:
        # TODO: DFS low-link; root special case
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.articulationPoints(5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]))  # expected: [1, 3]
    print(sol.articulationPoints(3, [[0, 1], [1, 2], [2, 0]]))  # expected: []
    print(sol.articulationPoints(4, [[0, 1], [1, 2], [2, 3]]))  # expected: [1, 2]
