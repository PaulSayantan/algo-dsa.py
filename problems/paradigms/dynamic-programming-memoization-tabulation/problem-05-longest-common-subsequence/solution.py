"""Longest Common Subsequence — LeetCode 1143.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """Return the length of the longest common subsequence of two strings.

        A subsequence keeps relative order but may skip characters.

        Args:
            text1: The first string (lowercase letters, length 1..1000).
            text2: The second string (lowercase letters, length 1..1000).

        Returns:
            The length of the longest subsequence common to both strings (0 if none).

        Example:
            >>> Solution().longestCommonSubsequence("abcde", "ace")
            3
        """
        # TODO: implement using memoization (top-down) or tabulation (bottom-up).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))  # expected: 3
    print(sol.longestCommonSubsequence("abc", "abc"))    # expected: 3
    print(sol.longestCommonSubsequence("abc", "def"))    # expected: 0
