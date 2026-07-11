"""LeetCode 516 — Longest Palindromic Subsequence.

Fill in the body of `longestPalindromeSubseq`. Do not edit the signature.
"""
from __future__ import annotations


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Return the length of the longest palindromic subsequence of s.

        Args:
            s: The input string (1 <= len <= 1000, lowercase letters).

        Returns:
            The length of the longest subsequence of s that is a palindrome.

        Example:
            >>> Solution().longestPalindromeSubseq("bbbab")
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindromeSubseq("bbbab"))   # expected: 4
    print(sol.longestPalindromeSubseq("cbbd"))    # expected: 2
    print(sol.longestPalindromeSubseq("agbdba"))  # expected: 5
