"""Course Schedule IV — LeetCode 1462."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # TODO: Kahn's topo order; propagate ancestor sets, then answer set membership
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkIfPrerequisite(4, [[0, 1], [1, 2], [2, 3]], [[0, 3], [3, 0], [0, 1], [2, 0]]))  # expected: [True, False, True, False]
    print(sol.checkIfPrerequisite(3, [], [[0, 1], [1, 2]]))  # expected: [False, False]
    print(sol.checkIfPrerequisite(5, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 2]]))  # expected: [True, False, False]
    print(sol.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))  # expected: [False, True]
