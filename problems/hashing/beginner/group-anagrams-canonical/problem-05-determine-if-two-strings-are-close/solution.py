"""Determine if Two Strings Are Close — LeetCode 1657."""
from collections import Counter  # noqa: F401


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # TODO: same character set AND same multiset of frequencies
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.closeStrings("abc", "bca"))  # expected: True
    print(sol.closeStrings("a", "aa"))  # expected: False
    print(sol.closeStrings("cabbba", "abbccc"))  # expected: True
    print(sol.closeStrings("uau", "ssx"))  # expected: False
