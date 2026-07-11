"""Count Substring Occurrences.

Given a text ``s`` and a list of query patterns, return for each pattern how many
times it occurs (with overlaps) as a substring of ``s``.

Intended technique: Suffix Automaton. The occurrence count of a substring equals
the size of its ``endpos`` set. Seed each non-clone state with count 1 and
propagate counts up the suffix-link tree; then each query is answered by walking
its characters through the automaton's transitions.
"""

from __future__ import annotations

from typing import List


class Solution:
    def count_occurrences(self, s: str, queries: List[str]) -> List[int]:
        """Count occurrences (with overlaps) of each query pattern in ``s``.

        Args:
            s: The text string to search within (lowercase English letters).
            queries: Patterns to count. Each is a lowercase string.

        Returns:
            A list of integers, one per query, giving the number of times that
            query occurs as a substring of ``s`` (0 if it never occurs).

        Example:
            >>> Solution().count_occurrences("abcbc", ["bc", "b", "abc", "xyz"])
            [2, 2, 1, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    # expected: [2, 2, 1, 0]
    print(sol.count_occurrences("abcbc", ["bc", "b", "abc", "xyz"]))
    # expected: [4, 3, 2, 1]
    print(sol.count_occurrences("aaaa", ["a", "aa", "aaa", "aaaa"]))
