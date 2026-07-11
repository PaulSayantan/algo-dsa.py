"""Total Length of All Distinct Substrings.

Return the sum of the lengths of all distinct non-empty substrings of ``s``.

Intended technique: Suffix Automaton. A state ``v`` represents every substring
whose length lies in the interval ``(len[link[v]], len[v]]``; the sum of the
integers in that interval is an arithmetic series contributed in O(1) per state.
"""

from __future__ import annotations


class Solution:
    def total_length_distinct_substrings(self, s: str) -> int:
        """Sum the lengths of all distinct non-empty substrings of ``s``.

        Args:
            s: The input string (lowercase English letters).

        Returns:
            The total length summed over every distinct non-empty substring.

        Example:
            >>> Solution().total_length_distinct_substrings("abc")
            10
            >>> Solution().total_length_distinct_substrings("aaa")
            6
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.total_length_distinct_substrings("abc"))   # expected: 10
    print(sol.total_length_distinct_substrings("aaa"))   # expected: 6
    print(sol.total_length_distinct_substrings("abab"))  # expected: 16
