"""LeetCode 44 - Wildcard Matching.

Empty solution template. Fill in the body yourself.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """Return whether pattern p matches the entire string s.

        Pattern operators:
            '?' matches any single character.
            '*' matches any sequence of characters, including the empty one.

        Args:
            s: The input string (lowercase English letters, may be empty).
            p: The pattern, containing lowercase letters, '?', and '*'.

        Returns:
            True if p matches all of s, False otherwise.

        Example:
            >>> Solution().isMatch("adceb", "*a*b")
            True
        """
        # TODO: implement using a 2D DP table where dp[i][j] answers
        # "does s[:i] match p[:j]?". Handle '*' with two branches:
        # match the empty sequence, or absorb one more character of s.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aa", "a"))       # expected: False
    print(sol.isMatch("aa", "*"))       # expected: True
    print(sol.isMatch("cb", "?a"))      # expected: False
    print(sol.isMatch("adceb", "*a*b")) # expected: True
