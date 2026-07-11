class Solution:
    def validPalindrome(self, s: str) -> bool:
        """Return whether ``s`` can be made a palindrome by deleting at most
        one character.

        Args:
            s: The input string of lowercase English letters.

        Returns:
            True if deleting zero or one character yields a palindrome;
            False otherwise.

        Example:
            >>> Solution().validPalindrome("abca")
            True
            >>> Solution().validPalindrome("abc")
            False
        """
        # TODO: implement using two pointers; on the first mismatch, try
        # skipping the left character or the right character.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.validPalindrome("aba"))   # expected: True
    print(sol.validPalindrome("abca"))  # expected: True
    print(sol.validPalindrome("abc"))   # expected: False
