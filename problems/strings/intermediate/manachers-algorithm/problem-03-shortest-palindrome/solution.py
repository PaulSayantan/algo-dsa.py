"""Shortest Palindrome (LeetCode 214).

Fill in the body of `shortestPalindrome` using Manacher's Algorithm to locate
the longest palindromic prefix.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """Return the shortest palindrome formed by prepending characters to ``s``.

        Args:
            s: The input string (lowercase English letters, possibly empty).

        Returns:
            The shortest palindrome that has ``s`` as a suffix.

        Example:
            >>> Solution().shortestPalindrome("aacecaaa")
            'aaacecaaa'
        """
        # TODO: implement using Manacher's Algorithm (longest palindromic prefix)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))  # expected: "aaacecaaa"
    print(sol.shortestPalindrome("abcd"))       # expected: "dcbabcd"
    print(sol.shortestPalindrome("aba"))        # expected: "aba"
    print(sol.shortestPalindrome(""))           # expected: ""
