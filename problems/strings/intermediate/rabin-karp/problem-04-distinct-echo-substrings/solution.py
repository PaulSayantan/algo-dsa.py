"""Distinct Echo Substrings (LeetCode 1316).

Solve this with Rabin-Karp: precompute prefix hashes, then test each even-length
window for "left half == right half" in O(1) and deduplicate with a set.
"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """Count distinct substrings of ``text`` of the form ``a + a``.

        Args:
            text: The input string of lowercase English letters.

        Returns:
            The number of distinct non-empty substrings that equal some string
            concatenated with itself (an "echo" substring).

        Example:
            >>> Solution().distinctEchoSubstrings("abcabcabc")
            3
            >>> Solution().distinctEchoSubstrings("leetcodeleetcode")
            2
        """
        # TODO: implement using Rabin-Karp (prefix hashes + set for distinctness)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.distinctEchoSubstrings("abcabcabc"))         # expected: 3
    print(sol.distinctEchoSubstrings("leetcodeleetcode"))  # expected: 2
    print(sol.distinctEchoSubstrings("aaa"))               # expected: 1
