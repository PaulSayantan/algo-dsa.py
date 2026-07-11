"""Longest palindromic substring using a Palindromic Tree (Eertree).

Build the eertree, then return the substring corresponding to the longest node.
"""

from __future__ import annotations


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """Return a longest palindromic substring of ``s``.

        Args:
            s: A non-empty string.

        Returns:
            One substring of ``s`` that is a palindrome and has maximum
            possible length. If multiple exist, any one may be returned.

        Example:
            >>> Solution().longestPalindrome("cbbd")
            'bb'
        """
        # TODO: implement
        # Suggested plan:
        #   1. Build the eertree over s, storing per node: length, suffix link,
        #      edges, and the end index at which the node was first created.
        #   2. When a new node is created at index i, its palindrome occupies
        #      s[i - length + 1 : i + 1]; remember (length, i) to reconstruct.
        #   3. Pick the node with the maximum length and slice s accordingly.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))             # expected: "bab" (or "aba")
    print(sol.longestPalindrome("cbbd"))              # expected: "bb"
    print(sol.longestPalindrome("forgeeksskeegfor"))  # expected: "geeksskeeg"
