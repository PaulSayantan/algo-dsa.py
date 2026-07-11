"""One Edit Distance (LeetCode 161).

Empty solution template — fill in the logic yourself.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """Return True iff s and t are exactly one edit distance apart.

        An edit is a single-character insertion, deletion, or substitution.
        The distance must be exactly 1 (equal strings return False).

        Args:
            s: The first string.
            t: The second string.

        Returns:
            True if the Levenshtein distance between s and t equals 1, else False.

        Example:
            >>> Solution().isOneEditDistance("ab", "acb")
            True
            >>> Solution().isOneEditDistance("", "")
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isOneEditDistance("ab", "acb"))   # expected: True
    print(sol.isOneEditDistance("cab", "ad"))   # expected: False
    print(sol.isOneEditDistance("", ""))        # expected: False
    print(sol.isOneEditDistance("a", ""))       # expected: True
