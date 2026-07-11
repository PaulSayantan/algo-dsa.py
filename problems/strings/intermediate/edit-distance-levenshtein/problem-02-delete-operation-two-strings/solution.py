"""Delete Operation for Two Strings (LeetCode 583).

Find the minimum number of single-character deletions (from either string)
needed to make two strings equal.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of deletions to make word1 == word2.

        Only deletion is allowed: in one step you remove one character from
        either word1 or word2.

        Args:
            word1: The first string.
            word2: The second string.

        Returns:
            The minimum total number of characters that must be deleted
            (counting both strings) so that the two strings become identical.

        Example:
            >>> Solution().minDistance("sea", "eat")
            2
            >>> Solution().minDistance("abc", "abc")
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("sea", "eat"))         # expected: 2
    print(sol.minDistance("leetcode", "etco"))   # expected: 4
    print(sol.minDistance("abc", "abc"))         # expected: 0
