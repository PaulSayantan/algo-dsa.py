"""LeetCode 1143 - Longest Common Subsequence.

Empty solution template. Fill in the body yourself.
"""

from typing import List  # noqa: F401  (imported for convenience)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest common subsequence of two strings.

        Args:
            text1: The first string (lowercase English letters).
            text2: The second string (lowercase English letters).

        Returns:
            The length of the longest subsequence present in both strings,
            or 0 if they share no common subsequence.

        Example:
            >>> Solution().longestCommonSubsequence("abcde", "ace")
            3
        """
        # TODO: implement using a 2D DP table where dp[i][j] is the LCS length
        # of text1[:i] and text2[:j].
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))  # expected: 3
    print(sol.longestCommonSubsequence("abc", "abc"))     # expected: 3
    print(sol.longestCommonSubsequence("abc", "def"))     # expected: 0
