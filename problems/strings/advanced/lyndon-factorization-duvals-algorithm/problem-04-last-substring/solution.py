"""Last Substring in Lexicographical Order (LeetCode 1163).

Implement `Solution.lastSubstring` using the Duval-style two-pointer maximum-suffix scan.
"""
from __future__ import annotations


class Solution:
    def lastSubstring(self, s: str) -> str:
        """Return the lexicographically largest substring (== largest suffix) of `s`.

        Args:
            s: A non-empty string of lowercase English letters.

        Returns:
            The lexicographically maximum suffix of `s`.

        Example:
            >>> Solution().lastSubstring("abab")
            'bab'
            >>> Solution().lastSubstring("leetcode")
            'tcode'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lastSubstring("abab"))      # expected: 'bab'
    print(sol.lastSubstring("leetcode"))  # expected: 'tcode'
    print(sol.lastSubstring("banana"))    # expected: 'nana'
