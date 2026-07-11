"""LeetCode 583 — Delete Operation for Two Strings.

Fill in the body of `minDistance`. Do not edit the signature.
"""
from __future__ import annotations


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of single-character deletions to make the
        two words equal.

        Args:
            word1: The first string (1 <= len <= 500, lowercase letters).
            word2: The second string (1 <= len <= 500, lowercase letters).

        Returns:
            The minimum total number of characters to delete (from either
            string) so that the two strings become identical.

        Example:
            >>> Solution().minDistance("sea", "eat")
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("sea", "eat"))         # expected: 2
    print(sol.minDistance("leetcode", "etco"))   # expected: 4
    print(sol.minDistance("abc", "abc"))         # expected: 0
