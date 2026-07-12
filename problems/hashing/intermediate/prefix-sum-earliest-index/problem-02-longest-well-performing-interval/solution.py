"""Longest Well-Performing Interval — LeetCode 1124."""
from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # TODO: tiring day = +1 else -1; longest interval with balance > 0
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestWPI([9, 9, 6, 0, 6, 6, 9]))  # expected: 3
    print(sol.longestWPI([6, 6, 6]))  # expected: 0
    print(sol.longestWPI([9, 9, 9]))  # expected: 3
