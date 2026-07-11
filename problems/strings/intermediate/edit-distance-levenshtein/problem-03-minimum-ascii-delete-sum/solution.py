"""Minimum ASCII Delete Sum for Two Strings (LeetCode 712).

Find the minimum total ASCII value of characters that must be deleted (from
either string) to make the two strings equal.
"""


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """Return the minimum ASCII sum of deleted characters to make s1 == s2.

        Only deletion is allowed. The cost of deleting a character is its ASCII
        code point (ord), so the objective is to minimize the summed ASCII value
        of everything removed rather than the number of deletions.

        Args:
            s1: The first string.
            s2: The second string.

        Returns:
            The minimum possible sum of ord(c) over every deleted character c,
            taken across both strings, such that the two strings become equal.

        Example:
            >>> Solution().minimumDeleteSum("sea", "eat")
            231
            >>> Solution().minimumDeleteSum("abc", "abc")
            0
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDeleteSum("sea", "eat"))       # expected: 231
    print(sol.minimumDeleteSum("delete", "leet"))   # expected: 403
    print(sol.minimumDeleteSum("abc", "abc"))       # expected: 0
