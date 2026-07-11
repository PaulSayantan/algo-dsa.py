"""LeetCode 28 - Find the Index of the First Occurrence in a String.

Solve this with the Z-Algorithm: build `needle + separator + haystack`,
compute the Z-array, and find the first index whose Z-value equals the length
of the needle.
"""

from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """Return the index of the first occurrence of needle in haystack.

        Args:
            haystack: The text to search within.
            needle: The pattern to search for (non-empty per constraints).

        Returns:
            The 0-based index of the first occurrence of ``needle`` in
            ``haystack``, or ``-1`` if it does not occur.

        Example:
            >>> Solution().strStr("sadbutsad", "sad")
            0
            >>> Solution().strStr("leetcode", "leeto")
            -1
        """
        # TODO: implement
        pass

    def _z_array(self, s: str) -> List[int]:
        """Optional helper: compute the Z-array of ``s`` in O(len(s)) time.

        Args:
            s: The string whose Z-array should be computed.

        Returns:
            A list ``z`` where ``z[i]`` is the length of the longest substring
            starting at ``i`` that is also a prefix of ``s``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))          # expected: 0
    print(sol.strStr("leetcode", "leeto"))          # expected: -1
    print(sol.strStr("abcabcabca", "abcabca"))      # expected: 0
