"""Longest Duplicate Substring (LeetCode 1044).

Practice this with binary search on the length plus double hashing to test
for a repeated window.
"""

from __future__ import annotations


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        """Return a longest substring of `s` that occurs at least twice.

        Args:
            s: A string of lowercase English letters.

        Returns:
            Any longest duplicated (contiguous) substring, or "" if none
            exists. Occurrences may overlap.

        Example:
            >>> Solution().longestDupSubstring("banana")
            'ana'
            >>> Solution().longestDupSubstring("abcd")
            ''
        """
        # TODO: implement
        # Suggested approach:
        #   1. Precompute prefix hashes h1, h2 and power tables for two moduli.
        #   2. has_dup(L): scan all windows of length L; store each (v1, v2)
        #      in a dict mapping hash pair -> start index; on a repeat, return
        #      the start index (candidate answer). Otherwise return -1.
        #   3. Binary search the largest L in [1, n-1] for which has_dup(L)
        #      succeeds, remembering the winning start index and length.
        #   4. Return s[start : start + best_len], or "" if best_len == 0.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(repr(sol.longestDupSubstring("banana")))  # expected: 'ana'
    print(repr(sol.longestDupSubstring("abcd")))     # expected: ''
    print(repr(sol.longestDupSubstring("aaaaa")))    # expected: 'aaaa'
