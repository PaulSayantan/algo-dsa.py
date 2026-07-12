"""Longest subarray with equal counts of two given values a and b."""
from typing import List  # noqa: F401


class Solution:
    def longestEqualCount(self, nums: List[int], a: int, b: int) -> int:
        # TODO: map a -> +1, b -> -1, everything else -> 0; equal counts of a and b
        #       means equal running balance at the window ends. Earliest-index map.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestEqualCount([1, 2, 1, 2, 3], 1, 2))  # expected: 5
    print(sol.longestEqualCount([1, 1, 2, 3, 3], 1, 3))  # expected: 5
    print(sol.longestEqualCount([5, 5, 5], 1, 2))  # expected: 3
    print(sol.longestEqualCount([1, 1, 1], 1, 2))  # expected: 0
    print(sol.longestEqualCount([2, 1, 2, 1], 1, 2))  # expected: 4
