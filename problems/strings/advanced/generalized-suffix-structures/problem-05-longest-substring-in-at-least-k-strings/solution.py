"""Longest Substring in At Least K Strings.

Return the length of the longest substring that occurs in at least ``k`` of the
``n`` given strings.

Intended technique: Generalized Suffix Structure. Build a single generalized
suffix automaton over all n strings, give each state a bitmask of which strings
occur there, propagate the masks up the suffix-link tree, and return the largest
len[v] among states whose mask has at least k set bits (popcount >= k).
"""

from __future__ import annotations

from typing import List


class Solution:
    def longest_substring_in_at_least_k(self, strings: List[str], k: int) -> int:
        """Length of the longest substring present in at least ``k`` strings.

        Args:
            strings: A list of ``n`` strings over a fixed alphabet.
            k: Minimum number of distinct strings that must contain the substring
                (1 <= k <= len(strings)).

        Returns:
            The length of the longest substring occurring in at least ``k`` of the
            input strings, or 0 if no non-empty substring qualifies.

        Example:
            >>> Solution().longest_substring_in_at_least_k(
            ...     ["abcd", "bcde", "cdef"], 2)
            3
            >>> Solution().longest_substring_in_at_least_k(
            ...     ["abcd", "bcde", "cdef"], 3)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.longest_substring_in_at_least_k(["abcd", "bcde", "cdef"], 2))  # 3
    print(sol.longest_substring_in_at_least_k(["abcd", "bcde", "cdef"], 3))  # 2
    print(sol.longest_substring_in_at_least_k(["aaa", "aaa", "bbb"], 2))     # 3
