"""Implement strStr() — LeetCode 28.

Find the index of the first occurrence of `needle` in `haystack`, or -1.
Solve this with KMP (Knuth-Morris-Pratt) in O(n + m) time.
"""

from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of needle in haystack.

        Args:
            haystack: The text to search within.
            needle: The pattern to search for. If empty, the answer is 0.

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
    print(sol.strStr("sadbutsad", "sad"))  # expected: 0
    print(sol.strStr("leetcode", "leeto"))  # expected: -1
    print(sol.strStr("hello", "ll"))        # expected: 2
