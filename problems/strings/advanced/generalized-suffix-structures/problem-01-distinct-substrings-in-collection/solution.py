"""Distinct Substrings in a Collection.

Count the number of distinct non-empty substrings across the union of all the
given strings. A substring that appears in more than one string (or repeatedly
within one string) is counted only once.

Intended technique: Generalized Suffix Structure. Build a single suffix
automaton over all the strings (resetting the ``last`` pointer to the root
before inserting each string, and reusing/cloning existing states when a
transition already exists). Then the answer is the sum over every non-initial
state ``v`` of ``len[v] - len[link[v]]``.
"""

from __future__ import annotations

from typing import List


class Solution:
    def count_distinct_substrings(self, words: List[str]) -> int:
        """Number of distinct substrings in the union of all ``words``.

        Args:
            words: A list of strings over a fixed alphabet (lowercase letters).

        Returns:
            The count of distinct non-empty substrings appearing in at least one
            of the input strings.

        Example:
            >>> Solution().count_distinct_substrings(["ab", "ba"])
            4
            >>> Solution().count_distinct_substrings(["aa", "aaa"])
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_distinct_substrings(["ab", "ba"]))    # expected: 4
    print(sol.count_distinct_substrings(["aa", "aaa"]))   # expected: 3
    print(sol.count_distinct_substrings(["abc", "bcd"]))  # expected: 9
