"""Minimum ASCII Delete Sum for Two Strings (LeetCode 712).

Empty solution template — fill in the logic yourself.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """Return the minimum total ASCII value of characters deleted to make s1 == s2.

        Only deletions are allowed; deleting a character costs its ASCII value (ord).

        Args:
            s1: The first string.
            s2: The second string.

        Returns:
            The smallest possible sum of ord(c) over all characters c deleted from either
            string so that the remaining strings are identical.

        Example:
            >>> Solution().minimumDeleteSum("sea", "eat")
            231
            >>> Solution().minimumDeleteSum("delete", "leet")
            403
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDeleteSum("sea", "eat"))     # expected: 231
    print(sol.minimumDeleteSum("delete", "leet"))  # expected: 403
    print(sol.minimumDeleteSum("abc", "abc"))      # expected: 0
    print(sol.minimumDeleteSum("a", "b"))          # expected: 195 (97 + 98)
