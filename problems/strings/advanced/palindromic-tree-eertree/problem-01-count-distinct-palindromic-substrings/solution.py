"""Count distinct palindromic substrings using a Palindromic Tree (Eertree).

Fill in the eertree construction and return the number of distinct palindromes.
"""

from __future__ import annotations


class Solution:
    def countDistinctPalindromes(self, s: str) -> int:
        """Return the number of distinct palindromic substrings of ``s``.

        Args:
            s: A non-empty string of lowercase English letters.

        Returns:
            The count of unique substrings of ``s`` that read the same
            forwards and backwards. Equal palindromes occurring in multiple
            places are counted once.

        Example:
            >>> Solution().countDistinctPalindromes("aabaa")
            5
        """
        # TODO: implement
        # Suggested plan:
        #   1. Maintain eertree nodes: length[], suffix_link[], edges[] and a
        #      `last` pointer. Seed with the two roots (len -1 and len 0).
        #   2. For each index i, walk suffix links from `last` to find the
        #      largest palindromic suffix that can be extended by s[i].
        #   3. If the extended palindrome is new, create a node (and its own
        #      suffix link); otherwise just move `last`.
        #   4. The answer is (number of nodes) - 2 for the two roots.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinctPalindromes("aba"))    # expected: 3
    print(sol.countDistinctPalindromes("aabaa"))  # expected: 5
    print(sol.countDistinctPalindromes("abc"))    # expected: 3
