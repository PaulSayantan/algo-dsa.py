"""Dial's algorithm: shortest paths via a bucket queue."""
from typing import List


class Solution:
    def shortestPaths(self, n: int, edges: List[List[int]], src: int) -> List[int]:
        # TODO: array of buckets indexed by distance
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPaths(5, [[0, 1, 4], [0, 2, 1], [2, 1, 1], [1, 3, 1], [2, 3, 5]], 0))  # expected: [0, 2, 1, 3, -1]
    print(sol.shortestPaths(3, [[0, 1, 2]], 0))  # expected: [0, 2, -1]
