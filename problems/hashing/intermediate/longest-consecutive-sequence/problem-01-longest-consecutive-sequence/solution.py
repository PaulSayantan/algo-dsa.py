"""Longest Consecutive Sequence — LeetCode 128."""
from typing import List  # noqa: F401


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TODO: put values in a set; only expand runs starting where x-1 is absent
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # expected: 4
    print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # expected: 9
    print(sol.longestConsecutive([]))  # expected: 0
    print(sol.longestConsecutive([1, 2, 0, 1]))  # expected: 3
