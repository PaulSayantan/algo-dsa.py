"""Repeated String Match — LeetCode 686.

Return the minimum number of copies of `a` whose concatenation contains `b`
as a substring, or -1 if impossible. Use KMP (Knuth-Morris-Pratt) to perform
the substring test in linear time over a bounded concatenation.
"""

from typing import List


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """Return the fewest repetitions of `a` that contain `b`, else -1.

        Args:
            a: The string to repeat.
            b: The target substring to locate.

        Returns:
            The minimum count k >= 1 such that b is a substring of a repeated
            k times, or -1 if no such k exists.

        Example:
            >>> Solution().repeatedStringMatch("abcd", "cdabcdab")
            3
            >>> Solution().repeatedStringMatch("a", "aa")
            2
        """
        # TODO: implement
        pass

    def _kmp_contains(self, text: str, pattern: str) -> bool:
        """Return True iff `pattern` occurs in `text` (KMP search).

        Args:
            text: The string to search within.
            pattern: The pattern to search for.

        Returns:
            True if `pattern` is a substring of `text`, else False.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.repeatedStringMatch("abcd", "cdabcdab"))  # expected: 3
    print(sol.repeatedStringMatch("a", "aa"))           # expected: 2
    print(sol.repeatedStringMatch("abc", "cabcabca"))   # expected: 4
    print(sol.repeatedStringMatch("abc", "wxyz"))       # expected: -1
