"""Shortest Palindrome — LeetCode 214.

Return the shortest palindrome formable by adding characters only in front of
`s`. Solve with KMP (Knuth-Morris-Pratt): build the LPS of s + '#' + reverse(s)
to find the longest palindromic prefix.
"""

from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """Return the shortest palindrome made by prepending characters to `s`.

        Args:
            s: The input string of lowercase letters (may be empty).

        Returns:
            The shortest palindrome that has `s` as its suffix.

        Example:
            >>> Solution().shortestPalindrome("aacecaaa")
            'aaacecaaa'
            >>> Solution().shortestPalindrome("abcd")
            'dcbabcd'
        """
        # TODO: implement
        pass

    def _build_lps(self, pattern: str) -> List[int]:
        """Build the KMP failure/prefix (LPS) array for `pattern`.

        Args:
            pattern: The pattern string.

        Returns:
            A list `lps` where `lps[i]` is the length of the longest proper
            prefix of `pattern[0..i]` that is also a suffix of `pattern[0..i]`.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestPalindrome("aacecaaa"))  # expected: "aaacecaaa"
    print(sol.shortestPalindrome("abcd"))      # expected: "dcbabcd"
    print(sol.shortestPalindrome("aba"))       # expected: "aba"
    print(sol.shortestPalindrome(""))          # expected: ""
