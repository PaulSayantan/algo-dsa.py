"""Course Schedule — LeetCode 207."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TODO: Kahn's topological sort; cycle iff not all emitted
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))  # expected: True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # expected: False
    print(sol.canFinish(4, [[1, 0], [2, 1], [3, 2]]))  # expected: True
