"""Implement strStr() — first occurrence of needle in haystack.

Solve this using Boyer–Moore (string search): preprocess the pattern
(bad-character + good-suffix tables) and scan the text with right-to-left
comparisons, jumping ahead on a mismatch.
"""
from typing import Dict, List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of needle in haystack.

        Args:
            haystack: The text to search within.
            needle: The pattern to search for. If empty, return 0.

        Returns:
            The 0-based index of the first occurrence of `needle` inside
            `haystack`, or -1 if it does not occur.

        Example:
            >>> Solution().strStr("sadbutsad", "sad")
            0
            >>> Solution().strStr("leetcode", "leeto")
            -1
        """
        # TODO: implement using Boyer–Moore (bad-character + good-suffix rules)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))     # expected: 0
    print(sol.strStr("leetcode", "leeto"))    # expected: -1
    print(sol.strStr("GCAATGCC", "GCC"))      # expected: 5
