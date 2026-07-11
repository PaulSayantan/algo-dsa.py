"""Longest Palindromic Substring (LeetCode 5).

Fill in the body of `longestPalindrome` using Manacher's Algorithm.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return the longest palindromic substring of ``s``.

        Args:
            s: The input string (letters and digits).

        Returns:
            A longest palindromic substring. If several are tied for the
            maximum length, any one of them may be returned.

        Example:
            >>> Solution().longestPalindrome("babad")
            'bab'  # "aba" is also acceptable
        """
        # TODO: implement using Manacher's Algorithm
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # expected: "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))   # expected: "bb"
    print(sol.longestPalindrome("a"))      # expected: "a"
