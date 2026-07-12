"""Longest variable-width window where max <= multiplier * min, via two deques."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def longestBoundedRatio(self, nums: List[int], multiplier: int) -> int:
        # TODO: two monotonic deques over a variable window; shrink while max > multiplier*min
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestBoundedRatio([2, 4, 3, 8, 5], 2))  # expected: 3
    print(sol.longestBoundedRatio([10, 1, 10, 1], 2))  # expected: 1
    print(sol.longestBoundedRatio([1, 5, 2, 6, 3], 3))  # expected: 4
    print(sol.longestBoundedRatio([3, 3, 3], 1))  # expected: 3
    print(sol.longestBoundedRatio([], 2))  # expected: 0
