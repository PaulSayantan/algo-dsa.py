"""Longest zero-sum subarray (return its length)."""
from typing import List


class Solution:
    def longestZeroSum(self, nums: List[int]) -> int:
        # TODO: earliest index of each prefix sum; longest gap between equal sums
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestZeroSum([15, -2, 2, -8, 1, 7, 10, 23]))  # expected: 5
    print(sol.longestZeroSum([1, 2, 3]))  # expected: 0
    print(sol.longestZeroSum([0, 0, 0, 0]))  # expected: 4
