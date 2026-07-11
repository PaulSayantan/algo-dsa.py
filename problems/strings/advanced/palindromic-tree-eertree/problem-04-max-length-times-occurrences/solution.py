"""Maximize length * occurrences over palindromic substrings via an Eertree.

Build the eertree, propagate occurrence counts up the suffix links, then take
the best length * count.
"""

from __future__ import annotations


class Solution:
    def maxPalindromeValue(self, s: str) -> int:
        """Return max over palindromes P of (len(P) * number_of_occurrences(P)).

        Args:
            s: A non-empty string of lowercase English letters.

        Returns:
            The maximum of ``length(P) * occ(P)`` across all palindromic
            substrings ``P`` of ``s``, where ``occ`` counts overlapping
            occurrences.

        Example:
            >>> Solution().maxPalindromeValue("aaaaa")
            9
        """
        # TODO: implement
        # Suggested plan:
        #   1. Build the eertree; each node stores length, suffix link, edges.
        #   2. Increment cnt[last] on every add (occurrence as longest suffix).
        #   3. Propagate cnt up suffix links in decreasing-length order to get
        #      true occurrence counts occ[v].
        #   4. Return max(length[v] * cnt[v]) over all non-root nodes v.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPalindromeValue("aaaaa"))    # expected: 9
    print(sol.maxPalindromeValue("ababa"))    # expected: 6
    print(sol.maxPalindromeValue("abacaba"))  # expected: 7
