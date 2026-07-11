"""Distinct Echo Substrings (LeetCode 1316).

Practice this by comparing substring halves via double hashing and deduping
echo substrings in a set.
"""

from __future__ import annotations


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """Count distinct substrings of `text` of the form a + a.

        Args:
            text: A string of lowercase English letters.

        Returns:
            The number of distinct non-empty substrings that equal some
            string concatenated with itself.

        Example:
            >>> Solution().distinctEchoSubstrings("abcabcabc")
            3
            >>> Solution().distinctEchoSubstrings("leetcodeleetcode")
            2
        """
        # TODO: implement
        # Suggested approach:
        #   1. Build prefix hashes h1, h2 and power tables for two moduli.
        #   2. Define O(1) sub_hash(l, r) -> (v1, v2) for text[l..r].
        #   3. For each start i and each half-length L, compare the hash of
        #      text[i..i+L-1] with text[i+L..i+2L-1]; if equal, record the
        #      echo's hash pair (its full-window hash) in a set.
        #   4. Return the size of the set.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.distinctEchoSubstrings("abcabcabc"))        # expected: 3
    print(sol.distinctEchoSubstrings("leetcodeleetcode"))  # expected: 2
    print(sol.distinctEchoSubstrings("aaa"))               # expected: 1
