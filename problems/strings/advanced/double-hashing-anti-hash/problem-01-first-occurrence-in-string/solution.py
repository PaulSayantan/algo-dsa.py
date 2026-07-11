"""Find the Index of the First Occurrence in a String (LeetCode 28).

Practice this with Rabin-Karp double hashing.
"""

from __future__ import annotations


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the first index where `needle` occurs in `haystack`, else -1.

        Args:
            haystack: The text to search within.
            needle: The pattern to look for.

        Returns:
            The 0-based index of the first occurrence of `needle` in
            `haystack`, or -1 if `needle` does not occur.

        Example:
            >>> Solution().strStr("sadbutsad", "sad")
            0
            >>> Solution().strStr("leetcode", "leeto")
            -1
        """
        # TODO: implement
        # Suggested approach:
        #   1. Let m = len(needle), n = len(haystack). Handle m > n -> -1.
        #   2. Precompute needle's double hash (two moduli M1, M2, bases B1, B2).
        #   3. Roll a window hash of length m across haystack in O(1) per step.
        #   4. When both hash components match the needle's, return the index
        #      (optionally confirm with a direct slice comparison).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))   # expected: 0
    print(sol.strStr("leetcode", "leeto"))  # expected: -1
    print(sol.strStr("hello", "ll"))        # expected: 2
