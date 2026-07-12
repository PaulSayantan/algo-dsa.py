"""Number of Distinct Islands — LeetCode 694."""
from collections import deque  # noqa: F401
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # TODO: normalize each island's cells relative to its top-left; hash the shape
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))  # expected: 1
    print(sol.numDistinctIslands([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]))  # expected: 3
    print(sol.numDistinctIslands([[0, 0], [0, 0]]))  # expected: 0
