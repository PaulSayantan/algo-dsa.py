"""Count Distinct Palindromic Substrings.

Fill in the body using the expand-around-center technique.
"""


class Solution:
    def countDistinctPalindromes(self, s: str) -> int:
        """Count the number of distinct palindromic substrings of ``s``.

        Distinct means by content: two equal palindrome strings occurring at
        different positions count as one.

        Args:
            s: The input string (1 <= len(s) <= 1000), lowercase letters.

        Returns:
            The number of unique substrings of ``s`` that are palindromes.

        Example:
            >>> Solution().countDistinctPalindromes("aaa")
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinctPalindromes("aaa"))    # expected: 3
    print(sol.countDistinctPalindromes("abaaa"))  # expected: 5
    print(sol.countDistinctPalindromes("abc"))    # expected: 3
