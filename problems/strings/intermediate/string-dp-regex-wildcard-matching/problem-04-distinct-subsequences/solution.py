"""LeetCode 115 - Distinct Subsequences.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """Count distinct subsequences of s that equal t.

        A subsequence keeps relative order but may drop characters. Two ways
        are distinct if they pick different index sets from s.

        Args:
            s: The source string.
            t: The target string to form as a subsequence of s.

        Returns:
            The number of distinct subsequences of s equal to t (fits in a
            32-bit signed integer).

        Example:
            >>> Solution().numDistinct("rabbbit", "rabbit")
            3
        """
        # TODO: implement using a 2D DP table where dp[i][j] is the number of
        # ways t[:j] is a subsequence of s[:i]. Always allow skipping s[i-1];
        # when s[i-1] == t[j-1] also allow using it.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numDistinct("rabbbit", "rabbit"))  # expected: 3
    print(sol.numDistinct("babgbag", "bag"))     # expected: 5
    print(sol.numDistinct("abc", "abcd"))        # expected: 0
