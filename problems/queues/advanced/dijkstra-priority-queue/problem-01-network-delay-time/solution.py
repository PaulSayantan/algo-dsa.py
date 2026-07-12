"""Network Delay Time — LeetCode 743."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # TODO: Dijkstra with a min-heap
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # expected: 2
    print(sol.networkDelayTime([[1, 2, 1]], 2, 1))  # expected: 1
    print(sol.networkDelayTime([[1, 2, 1]], 2, 2))  # expected: -1
