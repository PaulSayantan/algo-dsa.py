"""Palindrome Partitioning IV — LeetCode 1745.

Fill in the body using the expand-around-center technique to build a
palindrome-membership table, then test every pair of cut points.
"""


class Solution:
    def checkPartitioning(self, s: str) -> bool:
        """Return True if ``s`` splits into three non-empty palindromes.

        Args:
            s: The input string (3 <= len(s) <= 2000), lowercase letters.

        Returns:
            True if there exist cut points producing three non-empty
            palindromic substrings whose concatenation is ``s``; else False.

        Example:
            >>> Solution().checkPartitioning("abcbdd")
            True
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkPartitioning("abcbdd"))   # expected: True
    print(sol.checkPartitioning("bcbddxy"))  # expected: False
    print(sol.checkPartitioning("aabbaa"))   # expected: True
