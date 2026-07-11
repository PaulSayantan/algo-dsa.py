"""Palindrome Partitioning IV (LeetCode 1745).

Fill in the body of `checkPartitioning`. Precompute palindrome radii with
Manacher's Algorithm so each substring palindrome check is O(1).
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        """Return whether ``s`` can be split into three palindromic substrings.

        Args:
            s: The input string (lowercase English letters, length >= 3).

        Returns:
            True if there exist cuts producing three non-empty palindromes,
            otherwise False.

        Example:
            >>> Solution().checkPartitioning("abcbdd")
            True
        """
        # TODO: implement using Manacher's Algorithm for O(1) palindrome queries
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkPartitioning("abcbdd"))   # expected: True
    print(sol.checkPartitioning("bcbddxy"))  # expected: False
    print(sol.checkPartitioning("aaa"))      # expected: True
