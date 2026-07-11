"""Longest Palindromic Subsequence (LeetCode 516).

Fill in the body of `longestPalindromeSubseq` using Range / Interval DP.
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Return the length of the longest palindromic subsequence of ``s``.

        Args:
            s: A non-empty string of lowercase English letters.

        Returns:
            The length of the longest subsequence of ``s`` that is a palindrome.

        Example:
            >>> Solution().longestPalindromeSubseq("bbbab")
            4
        """
        # TODO: implement using interval DP over dp[i][j] for substring s[i..j]
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindromeSubseq("bbbab"))   # expected: 4
    print(sol.longestPalindromeSubseq("cbbd"))    # expected: 2
    print(sol.longestPalindromeSubseq("agbdba"))  # expected: 5
