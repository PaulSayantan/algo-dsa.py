"""Count Distinct Substrings.

Return the number of distinct non-empty substrings of ``s``.

Intended technique: Suffix Automaton. Each SAM state ``v`` (except the initial
state) accounts for exactly ``len[v] - len[link[v]]`` distinct substrings, so
the answer is the sum of that quantity over all states.
"""

from __future__ import annotations


class Solution:
    def count_distinct_substrings(self, s: str) -> int:
        """Count the number of distinct non-empty substrings of ``s``.

        Args:
            s: The input string (lowercase English letters).

        Returns:
            The number of distinct non-empty substrings of ``s``.

        Example:
            >>> Solution().count_distinct_substrings("abc")
            6
            >>> Solution().count_distinct_substrings("aaa")
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_distinct_substrings("abc"))   # expected: 6
    print(sol.count_distinct_substrings("aaa"))   # expected: 3
    print(sol.count_distinct_substrings("abab"))  # expected: 7
