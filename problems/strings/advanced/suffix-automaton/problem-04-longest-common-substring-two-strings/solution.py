"""Longest Common Substring of Two Strings.

Return the length of the longest contiguous substring common to ``s`` and ``t``.

Intended technique: Suffix Automaton. Build the SAM of ``s``, then stream ``t``
through it while maintaining a current state and current match length; on a
missing transition, follow suffix links to shorten the match. Track the maximum
match length reached.
"""

from __future__ import annotations


class Solution:
    def longest_common_substring(self, s: str, t: str) -> int:
        """Length of the longest common (contiguous) substring of ``s`` and ``t``.

        Args:
            s: First string (lowercase English letters).
            t: Second string (lowercase English letters).

        Returns:
            The length of the longest substring appearing in both strings, or 0
            if they share no common substring.

        Example:
            >>> Solution().longest_common_substring("abcde", "cdefg")
            3
            >>> Solution().longest_common_substring("banana", "ananas")
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_common_substring("abcde", "cdefg"))    # expected: 3
    print(sol.longest_common_substring("banana", "ananas"))  # expected: 5
    print(sol.longest_common_substring("abc", "xyz"))        # expected: 0
