"""Longest subarray with at most K distinct integers."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def longestKDistinct(self, nums: List[int], k: int) -> int:
        # TODO: variable window; track the max length while distinct count <= k
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestKDistinct([1, 2, 1, 2, 3], 2))  # expected: 4
    print(sol.longestKDistinct([1, 2, 3, 4, 5], 1))  # expected: 1
    print(sol.longestKDistinct([1, 1, 2, 2, 3, 3, 4], 2))  # expected: 4
    print(sol.longestKDistinct([4, 4, 4], 0))  # expected: 0
