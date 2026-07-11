"""Count Distinct Common Substrings.

Count how many distinct non-empty substrings are common to ALL of the given
strings (the size of the intersection of their substring sets).

Intended technique: Generalized Suffix Structure. Build a single generalized
suffix automaton over all k strings, mark each state with a k-bit ownership mask
(which strings occur there), propagate masks up the suffix-link tree, and sum
``len[v] - len[link[v]]`` over every state whose mask has all k bits set.
"""

from __future__ import annotations

from typing import List


class Solution:
    def count_common_substrings(self, strings: List[str]) -> int:
        """Number of distinct substrings common to every string in ``strings``.

        Args:
            strings: A list of ``k`` strings over a fixed alphabet.

        Returns:
            The count of distinct non-empty substrings that occur in all ``k``
            strings simultaneously; 0 if no substring is common to all of them.

        Example:
            >>> Solution().count_common_substrings(["aaa", "aa"])
            2
            >>> Solution().count_common_substrings(["abab", "baba"])
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_common_substrings(["ab", "ab"]))       # expected: 3
    print(sol.count_common_substrings(["aaa", "aa"]))      # expected: 2
    print(sol.count_common_substrings(["abab", "baba"]))   # expected: 6
