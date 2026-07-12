"""Parallel Courses — LeetCode 1136."""
from typing import List
from collections import deque  # noqa: F401


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # TODO: Kahn's level-by-level BFS; count levels, return -1 if a cycle remains
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSemesters(3, [[1, 3], [2, 3]]))  # expected: 2
    print(sol.minimumSemesters(3, [[1, 2], [2, 3], [3, 1]]))  # expected: -1
    print(sol.minimumSemesters(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))  # expected: 5
    print(sol.minimumSemesters(4, []))  # expected: 1
