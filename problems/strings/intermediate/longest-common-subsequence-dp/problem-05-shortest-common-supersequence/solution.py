"""LeetCode 1092 — Shortest Common Supersequence.

Fill in the body of `shortestCommonSupersequence`. Do not edit the signature.
"""
from __future__ import annotations


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """Return a shortest string that has both str1 and str2 as subsequences.

        Args:
            str1: The first string (1 <= len <= 1000, lowercase letters).
            str2: The second string (1 <= len <= 1000, lowercase letters).

        Returns:
            Any shortest common supersequence of str1 and str2. Its length is
            len(str1) + len(str2) - LCS(str1, str2).

        Example:
            >>> Solution().shortestCommonSupersequence("abac", "cab")
            'cabac'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # Multiple valid answers exist; "cabac" is one shortest (length 5).
    print(sol.shortestCommonSupersequence("abac", "cab"))          # expected len 5, e.g. "cabac"
    print(sol.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))  # expected: "aaaaaaaa"
