"""Prim's Minimum Spanning Tree total weight (PQ-driven)."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def mstWeight(self, n: int, edges: List[List[int]]) -> int:
        # TODO: Prim's algorithm with a min-heap
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.mstWeight(4, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 4]]))  # expected: 6
    print(sol.mstWeight(3, [[0, 1, 5], [1, 2, 5], [0, 2, 1]]))  # expected: 6
    print(sol.mstWeight(1, []))  # expected: 0
