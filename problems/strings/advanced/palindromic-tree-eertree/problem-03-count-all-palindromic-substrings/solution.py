"""Count all palindromic substring occurrences via a Palindromic Tree (Eertree).

Build the eertree, tally each node's occurrences, propagate along suffix links,
then sum.
"""

from __future__ import annotations


class Solution:
    def countSubstrings(self, s: str) -> int:
        """Return the total number of palindromic substring occurrences in ``s``.

        Every occurrence is counted separately, so equal palindromes starting at
        different indices each add to the total.

        Args:
            s: A non-empty string of lowercase English letters.

        Returns:
            The number of (start, end) index pairs for which the corresponding
            substring is a palindrome.

        Example:
            >>> Solution().countSubstrings("aaa")
            6
        """
        # TODO: implement
        # Suggested plan:
        #   1. Build the eertree. Each time `add(i)` sets `last` to a node,
        #      increment that node's cnt (it just occurred as a suffix).
        #   2. After building, process nodes in DECREASING length order and add
        #      each node's cnt to its suffix-link target's cnt. This turns the
        #      "as-longest-suffix" counts into true occurrence counts.
        #   3. Sum cnt over all non-root nodes.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countSubstrings("abc"))  # expected: 3
    print(sol.countSubstrings("aaa"))  # expected: 6
    print(sol.countSubstrings("aba"))  # expected: 4
