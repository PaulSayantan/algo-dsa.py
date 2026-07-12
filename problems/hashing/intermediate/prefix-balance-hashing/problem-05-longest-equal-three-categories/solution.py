"""Longest subarray with equal counts of three categories (values 0, 1, 2)."""
from typing import List  # noqa: F401


class Solution:
    def longestEqualThree(self, nums: List[int]) -> int:
        # TODO: track counts (c0, c1, c2); all-equal is a translation-invariant
        #       property, so key each prefix by the tuple (c0 - c1, c1 - c2) and
        #       store its earliest index (seed {(0, 0): -1}).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestEqualThree([0, 1, 2]))  # expected: 3
    print(sol.longestEqualThree([0, 1, 2, 0, 1, 2]))  # expected: 6
    print(sol.longestEqualThree([0, 0, 1, 2]))  # expected: 3
    print(sol.longestEqualThree([0, 0, 0]))  # expected: 0
    print(sol.longestEqualThree([1, 2, 0, 2, 0, 1]))  # expected: 6
