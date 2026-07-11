"""Distinct Echo Substrings (LeetCode 1316).

Return the number of DISTINCT (by content) non-empty substrings that equal a
string concatenated with itself (form a + a).

Fill in the body yourself. The recommended approach is the Main-Lorentz
algorithm to enumerate square occurrences, combined with a rolling hash keyed on
(length, hash) to deduplicate by content.
"""

from __future__ import annotations


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """Count distinct echo substrings (substrings of the form a + a).

        Args:
            text: The input string (lowercase English letters).

        Returns:
            The number of distinct-by-content substrings of ``text`` that are the
            concatenation of some non-empty string with itself.

        Example:
            >>> Solution().distinctEchoSubstrings("abcabcabc")
            3
            >>> Solution().distinctEchoSubstrings("leetcodeleetcode")
            2
        """
        # TODO: implement using the Main-Lorentz algorithm + rolling hash.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.distinctEchoSubstrings("abcabcabc"))        # expected: 3
    print(sol.distinctEchoSubstrings("leetcodeleetcode"))  # expected: 2
    print(sol.distinctEchoSubstrings("abcde"))             # expected: 0
    print(sol.distinctEchoSubstrings("aaaa"))              # expected: 2
