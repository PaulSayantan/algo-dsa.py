"""Minimum Area Rectangle — LeetCode 939."""
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # TODO: store points in a set; for each diagonal pair check the other corners
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]]))  # expected: 4
    print(sol.minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]]))  # expected: 2
    print(sol.minAreaRect([[1, 1], [2, 2]]))  # expected: 0
