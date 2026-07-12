"""Longest subarray with sum divisible by k (return length)."""
from typing import List


class Solution:
    def longestDivByK(self, nums: List[int], k: int) -> int:
        # TODO: earliest index of each prefix remainder; longest equal-remainder gap
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestDivByK([2, 7, 6, 1, 4, 5], 3))  # expected: 4
    print(sol.longestDivByK([1, 2, 3], 7))  # expected: 0
    print(sol.longestDivByK([5, 5, 5, 5], 5))  # expected: 4
