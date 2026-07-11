"""LeetCode 712 — Minimum ASCII Delete Sum for Two Strings.

Fill in the body of `minimumDeleteSum`. Do not edit the signature.
"""
from __future__ import annotations


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """Return the lowest ASCII sum of deleted characters needed to make the
        two strings equal.

        Args:
            s1: The first string (1 <= len <= 1000, lowercase letters).
            s2: The second string (1 <= len <= 1000, lowercase letters).

        Returns:
            The minimum total ASCII value of characters deleted (from either
            string) so that the two strings become identical.

        Example:
            >>> Solution().minimumDeleteSum("sea", "eat")
            231
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDeleteSum("sea", "eat"))        # expected: 231
    print(sol.minimumDeleteSum("delete", "leet"))    # expected: 403
