"""Longest Happy Prefix (LeetCode 1392).

Practice this with prefix hashing under two moduli (anti-hash).
"""

from __future__ import annotations


class Solution:
    def longestPrefix(self, s: str) -> str:
        """Return the longest non-empty proper prefix that is also a suffix.

        Args:
            s: A string of lowercase English letters.

        Returns:
            The longest string that is both a prefix and a suffix of `s`
            without being all of `s`; the empty string if none exists.

        Example:
            >>> Solution().longestPrefix("level")
            'l'
            >>> Solution().longestPrefix("ababab")
            'abab'
        """
        # TODO: implement
        # Suggested approach:
        #   1. Build prefix-hash arrays h1, h2 and power arrays for two moduli.
        #   2. Define O(1) sub_hash(l, r) returning (v1, v2) for s[l..r].
        #   3. For L from n-1 down to 1, compare hash of s[0..L-1] with
        #      hash of s[n-L..n-1]. Return the first L that matches on both.
        #   4. If nothing matches, return "".
        pass


if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.longestPrefix("level")))    # expected: 'l'
    print(repr(sol.longestPrefix("ababab")))   # expected: 'abab'
    print(repr(sol.longestPrefix("abcdef")))   # expected: ''
