"""LeetCode 10 - Regular Expression Matching.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Return whether pattern p matches the entire string s.

        Pattern operators:
            '.' matches any single character.
            '*' matches zero or more of the PRECEDING element.

        Args:
            s: The input string (lowercase English letters).
            p: The pattern, containing lowercase letters, '.', and '*'.

        Returns:
            True if p matches all of s, False otherwise.

        Example:
            >>> Solution().isMatch("aa", "a*")
            True
        """
        # TODO: implement using a 2D DP table where dp[i][j] answers
        # "does s[:i] match p[:j]?". When p[j-1] == '*', consider the pair
        # p[j-2]p[j-1]: match zero occurrences (dp[i][j-2]) or one more
        # occurrence when p[j-2] matches s[i-1] (dp[i-1][j]).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))                    # expected: False
    print(sol.isMatch("aa", "a*"))                   # expected: True
    print(sol.isMatch("ab", ".*"))                   # expected: True
    print(sol.isMatch("mississippi", "mis*is*p*."))  # expected: False
