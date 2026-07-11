"""Implement strStr() with the Bitap (shift-or) exact-matching technique.

Fill in `strStr` yourself. This file is an empty template on purpose.
"""

from __future__ import annotations


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of `needle` in `haystack`.

        Solve this with the Bitap shift-or formulation:
          1. If `needle` is empty, return 0.
          2. Precompute `peq[c]`: a bitmask whose bit j is set iff needle[j] == c.
          3. Sweep a single register R over the text using the shift-or update.
          4. The first time the bit `1 << (len(needle) - 1)` is set in R, a full
             match ends at the current index i; return the start index
             `i - len(needle) + 1`.
          5. If the sweep finishes with no match, return -1.

        Args:
            haystack: The text to search within (lowercase English letters).
            needle:   The pattern to find (lowercase English letters, possibly empty).

        Returns:
            The 0-based index of the first occurrence of `needle` in `haystack`,
            or -1 if `needle` does not occur. Returns 0 when `needle` is empty.

        Example:
            >>> Solution().strStr("mississippi", "issip")
            4
        """
        # TODO: implement using the Bitap shift-or register update.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))     # expected: 0
    print(sol.strStr("leetcode", "leeto"))    # expected: -1
    print(sol.strStr("mississippi", "issip")) # expected: 4
    print(sol.strStr("hello", ""))            # expected: 0
