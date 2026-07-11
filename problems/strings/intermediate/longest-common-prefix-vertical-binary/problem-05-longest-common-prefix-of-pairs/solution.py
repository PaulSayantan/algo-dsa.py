"""LeetCode 3043 — Find the Length of the Longest Common Prefix.

Fill in `Solution.longestCommonPrefix` so it returns the length of the longest common
digit-prefix among all cross pairs (x from arr1, y from arr2).
"""
from __future__ import annotations

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """Return the longest common prefix length over all pairs (x, y).

        Args:
            arr1: A non-empty list of positive integers.
            arr2: A non-empty list of positive integers.

        Returns:
            The maximum number of shared leading decimal digits over every pair
            (x, y) with x in arr1 and y in arr2. Returns 0 if no pair shares a prefix.

        Example:
            >>> Solution().longestCommonPrefix([1, 10, 100], [1000])
            3
            >>> Solution().longestCommonPrefix([1, 2, 3], [4, 4, 4])
            0
        """
        # TODO: implement
        #   Efficient idea: collect every digit-prefix of the arr1 numbers into a set
        #   (or a trie), then for each arr2 number walk its digit prefixes and track the
        #   longest one present in the set. The per-pair primitive is the vertical LCP
        #   scan of two digit strings.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix([1, 10, 100], [1000]))  # expected: 3
    print(sol.longestCommonPrefix([1, 2, 3], [4, 4, 4]))  # expected: 0
    print(sol.longestCommonPrefix([12, 34], [123, 340]))  # expected: 2
    print(sol.longestCommonPrefix([5], [59, 512]))        # expected: 1
