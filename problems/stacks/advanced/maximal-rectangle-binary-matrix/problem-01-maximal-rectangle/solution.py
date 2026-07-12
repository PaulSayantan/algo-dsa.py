"""Maximal Rectangle — LeetCode 85."""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[int]]) -> int:
        # TODO: per-row histogram + monotonic stack
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalRectangle([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))  # expected: 6
    print(sol.maximalRectangle([[0]]))  # expected: 0
    print(sol.maximalRectangle([[1]]))  # expected: 1
    print(sol.maximalRectangle([[1, 1], [1, 1]]))  # expected: 4
