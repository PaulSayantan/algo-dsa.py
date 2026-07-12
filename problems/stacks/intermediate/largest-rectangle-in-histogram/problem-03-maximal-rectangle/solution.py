"""Maximal Rectangle — largest all-ones rectangle in a binary matrix."""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[int]]) -> int:
        # TODO: build a per-row histogram of consecutive 1s, then run largest-rectangle-in-histogram per row
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalRectangle([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]))  # expected: 6
    print(sol.maximalRectangle([]))  # expected: 0
    print(sol.maximalRectangle([[0]]))  # expected: 0
    print(sol.maximalRectangle([[1]]))  # expected: 1
    print(sol.maximalRectangle([[1, 1], [1, 1]]))  # expected: 4
