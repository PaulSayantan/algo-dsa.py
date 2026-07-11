"""Longest Common Substring of K Strings (SPOJ LCS2).

Return the length of the longest contiguous substring that appears in every one
of the given strings.

Intended technique: Generalized Suffix Structure. Build a single generalized
suffix automaton over all k strings, give each state a k-bit ownership mask
(which strings occur there), propagate the masks up the suffix-link tree, and
return the largest len[v] among states whose mask has all k bits set.
"""

from __future__ import annotations

from typing import List


class Solution:
    def longest_common_substring_k(self, strings: List[str]) -> int:
        """Length of the longest substring common to all ``strings``.

        Args:
            strings: A list of ``k`` strings over a fixed alphabet.

        Returns:
            The length of the longest contiguous substring present in every
            string, or 0 if no non-empty substring is common to all of them.

        Example:
            >>> Solution().longest_common_substring_k(["abab", "baba", "aabb"])
            2
            >>> Solution().longest_common_substring_k(["abc", "def", "xyz"])
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_common_substring_k(
        ["alsdfkjfjkdsal", "fdjskalajfkdsla", "aaaajfaaaa"]))  # expected: 2
    print(sol.longest_common_substring_k(["abab", "baba", "aabb"]))  # expected: 2
    print(sol.longest_common_substring_k(["abc", "def", "xyz"]))     # expected: 0
