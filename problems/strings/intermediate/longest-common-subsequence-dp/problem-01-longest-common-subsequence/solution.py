"""LeetCode 1143 — Longest Common Subsequence.

Fill in the body of `longestCommonSubsequence`. Do not edit the signature.
"""
from __future__ import annotations


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest common subsequence of two strings.

        Args:
            text1: The first string (1 <= len <= 1000, lowercase letters).
            text2: The second string (1 <= len <= 1000, lowercase letters).

        Returns:
            The length of the longest subsequence present in both strings.

        Example:
            >>> Solution().longestCommonSubsequence("abcde", "ace")
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))  # expected: 3
    print(sol.longestCommonSubsequence("abc", "abc"))     # expected: 3
    print(sol.longestCommonSubsequence("abc", "def"))     # expected: 0
