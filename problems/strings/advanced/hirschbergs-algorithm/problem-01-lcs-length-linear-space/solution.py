"""Longest Common Subsequence — length only, in O(min(n, m)) space.

Fill in `longestCommonSubsequence`. Do NOT allocate the full (n+1)*(m+1) table;
use a single rolling row whose width is min(len(text1), len(text2)) + 1.
"""

from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest common subsequence of text1 and text2.

        Args:
            text1: First string (lowercase English letters).
            text2: Second string (lowercase English letters).

        Returns:
            The length of the longest common subsequence. 0 if none exists.

        Example:
            >>> Solution().longestCommonSubsequence("abcde", "ace")
            3
        """
        # TODO: implement using a single rolling DP row of width min(n, m) + 1
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))  # expected: 3
    print(sol.longestCommonSubsequence("abc", "abc"))    # expected: 3
    print(sol.longestCommonSubsequence("abc", "def"))    # expected: 0
