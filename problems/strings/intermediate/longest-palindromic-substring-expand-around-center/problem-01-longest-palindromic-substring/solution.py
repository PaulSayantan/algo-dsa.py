"""Longest Palindromic Substring — LeetCode 5.

Fill in the body using the expand-around-center technique.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return the longest palindromic substring of ``s``.

        Args:
            s: The input string (1 <= len(s) <= 1000), digits and letters.

        Returns:
            The longest substring of ``s`` that is a palindrome. If several
            palindromes tie for the maximum length, any one of them is a valid
            return value.

        Example:
            >>> Solution().longestPalindrome("cbbd")
            'bb'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # expected: "bab" (or "aba")
    print(sol.longestPalindrome("cbbd"))   # expected: "bb"
    print(sol.longestPalindrome("a"))      # expected: "a"
