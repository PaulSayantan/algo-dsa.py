"""Course Schedule II — lexicographically smallest topological order."""
from typing import List
import heapq  # noqa: F401


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TODO: Kahn's with a min-heap; return [] on a cycle
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # expected: [0, 1, 2, 3]
    print(sol.findOrder(2, [[0, 1]]))  # expected: [1, 0]
    print(sol.findOrder(2, [[0, 1], [1, 0]]))  # expected: []
