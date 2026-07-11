"""Delete Operation for Two Strings (LeetCode 583).

Empty solution template — fill in the logic yourself.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Return the minimum number of single-character deletions to make the words equal.

        In one step you delete one character from either word1 or word2. Only deletions
        are permitted (no inserts, no substitutions).

        Args:
            word1: The first string.
            word2: The second string.

        Returns:
            The minimum total number of deletions needed for word1 and word2 to become
            identical strings.

        Example:
            >>> Solution().minDistance("sea", "eat")
            2
            >>> Solution().minDistance("leetcode", "etco")
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDistance("sea", "eat"))        # expected: 2
    print(sol.minDistance("leetcode", "etco"))  # expected: 4
    print(sol.minDistance("abc", "abc"))        # expected: 0
    print(sol.minDistance("a", "b"))            # expected: 2
