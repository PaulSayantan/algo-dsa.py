"""Cyclical Quest (Codeforces 235C).

Given a text ``s`` and query strings, for each query ``x`` count the number of
substrings of ``s`` that are cyclically isomorphic to ``x`` (i.e., sum, over the
distinct cyclic rotations of ``x``, of each rotation's occurrence count in ``s``).

Intended technique: Suffix Automaton with endpos (occurrence) counts. Feed the
doubled string ``x + x`` through the automaton as a sliding window of length
``len(x)``; whenever a full-length match lands on a state, add that state's
occurrence count, marking states so each distinct rotation is counted once.
"""

from __future__ import annotations

from typing import List


class Solution:
    def cyclical_quest(self, s: str, queries: List[str]) -> List[int]:
        """For each query, count substrings of ``s`` cyclically isomorphic to it.

        Args:
            s: The text string (lowercase English letters).
            queries: The query strings; each is matched against all its distinct
                cyclic rotations.

        Returns:
            A list of integers, one per query: the total number of occurrences in
            ``s`` (counted by position, overlaps included) summed over the
            distinct cyclic rotations of the query.

        Example:
            >>> Solution().cyclical_quest("baabaabaaa", ["a", "ba", "baa", "aaba"])
            [7, 5, 7, 5]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected: [7, 5, 7, 5]
    print(sol.cyclical_quest("baabaabaaa", ["a", "ba", "baa", "aaba"]))
    # expected: [2, 2, 3]
    print(sol.cyclical_quest("aabbaa", ["aa", "ab", "abba"]))
