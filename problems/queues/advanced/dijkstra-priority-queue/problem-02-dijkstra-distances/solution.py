"""Single-source Dijkstra: distance array."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def dijkstra(self, n: int, edges: List[List[int]], src: int) -> List[int]:
        # TODO
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.dijkstra(5, [[0, 1, 2], [0, 2, 4], [1, 2, 1], [2, 4, 3], [1, 3, 7]], 0))  # expected: [0, 2, 3, 9, 6]
    print(sol.dijkstra(3, [[0, 1, 5]], 0))  # expected: [0, 5, -1]
