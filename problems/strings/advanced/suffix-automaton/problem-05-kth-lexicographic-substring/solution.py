"""K-th Lexicographically Smallest Distinct Substring.

Return the k-th (1-indexed) lexicographically smallest distinct non-empty
substring of ``s``, or "" if k exceeds the number of distinct substrings.

Intended technique: Suffix Automaton. Build the SAM, view it as a DAG, and for
each state precompute the count of distinct substrings reachable from it. Then
greedily descend the DAG, trying edges in increasing character order and
subtracting subtree counts to home in on the k-th path.
"""

from __future__ import annotations


class Solution:
    def kth_distinct_substring(self, s: str, k: int) -> str:
        """Find the k-th lexicographically smallest distinct substring of ``s``.

        Args:
            s: The input string (lowercase English letters).
            k: 1-indexed rank in the sorted list of distinct substrings.

        Returns:
            The k-th smallest distinct substring, or "" if k is out of range.

        Example:
            >>> Solution().kth_distinct_substring("aab", 3)
            'aab'
            >>> Solution().kth_distinct_substring("aba", 2)
            'ab'
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.kth_distinct_substring("aab", 3))  # expected: "aab"
    print(sol.kth_distinct_substring("aba", 2))  # expected: "ab"
    print(sol.kth_distinct_substring("aba", 6))  # expected: ""
