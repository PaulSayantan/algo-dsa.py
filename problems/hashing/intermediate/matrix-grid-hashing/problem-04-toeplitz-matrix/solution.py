"""Toeplitz Matrix — LeetCode 766."""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # TODO: group cells by (r - c); every diagonal must be constant
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))  # expected: True
    print(sol.isToeplitzMatrix([[1, 2], [2, 2]]))  # expected: False
    print(sol.isToeplitzMatrix([[11]]))  # expected: True
