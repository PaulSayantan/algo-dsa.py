class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return a longest palindromic substring of ``s``.

        Args:
            s: The input string of digits and English letters.

        Returns:
            The longest contiguous substring of ``s`` that is a palindrome.
            If several achieve the maximum length, any one may be returned.

        Example:
            >>> Solution().longestPalindrome("babad")  # "bab" or "aba"
            'bab'
            >>> Solution().longestPalindrome("cbbd")
            'bb'
        """
        # TODO: for each center (odd and even), expand two pointers outward
        # while characters match; keep the longest span seen.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # expected: "bab" (or "aba")
    print(sol.longestPalindrome("cbbd"))   # expected: "bb"
    print(sol.longestPalindrome("a"))      # expected: "a"
