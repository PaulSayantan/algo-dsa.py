"""Maximum bipartite matching (Hopcroft-Karp)."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def maxMatching(self, left: int, right: int, edges: List[List[int]]) -> int:
        # TODO: Hopcroft-Karp (BFS layering + DFS augmenting)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxMatching(3, 3, [[0, 0], [0, 1], [1, 0], [2, 2]]))  # expected: 3
    print(sol.maxMatching(2, 2, [[0, 0], [1, 0]]))  # expected: 1
    print(sol.maxMatching(4, 4, [[0, 0], [1, 1], [2, 2], [3, 3]]))  # expected: 4
