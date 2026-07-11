"""One Edit Distance (LeetCode 161).

Determine whether two strings are exactly one edit (insert / delete / replace)
apart.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """Return True iff s and t are exactly one edit distance apart.

        Args:
            s: The first string.
            t: The second string.

        Returns:
            True if s can be turned into t (or vice versa) using exactly one
            single-character insert, delete, or replace; False otherwise.
            Identical strings return False because they are zero edits apart.

        Example:
            >>> Solution().isOneEditDistance("ab", "acb")
            True
            >>> Solution().isOneEditDistance("abc", "abc")
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isOneEditDistance("ab", "acb"))   # expected: True
    print(sol.isOneEditDistance("cab", "ad"))   # expected: False
    print(sol.isOneEditDistance("1203", "1213"))  # expected: True
    print(sol.isOneEditDistance("abc", "abc"))  # expected: False
