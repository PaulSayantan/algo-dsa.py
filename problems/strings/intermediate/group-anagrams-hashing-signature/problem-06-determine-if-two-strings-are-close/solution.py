"""Determine if Two Strings Are Close — LeetCode 1657.

Decide whether two strings are "close" (reachable via character swaps and
whole-character relabelings) by comparing their character-set and
count-multiset signatures.
"""


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """Return True if ``word1`` and ``word2`` are close.

        Two strings are close when one can be turned into the other using any
        number of (1) swaps of existing characters and (2) global relabelings
        that exchange all occurrences of two existing characters.

        Args:
            word1: First string of lowercase English letters.
            word2: Second string of lowercase English letters.

        Returns:
            True if the strings are close, otherwise False.

        Example:
            >>> Solution().closeStrings("abc", "bca")
            True
            >>> Solution().closeStrings("a", "aa")
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.closeStrings("abc", "bca"))         # expected: True
    print(sol.closeStrings("a", "aa"))            # expected: False
    print(sol.closeStrings("cabbba", "abbccc"))   # expected: True
