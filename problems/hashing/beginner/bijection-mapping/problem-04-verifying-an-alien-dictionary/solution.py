"""Verifying an Alien Dictionary — LeetCode 953."""
from typing import List  # noqa: F401


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # TODO: map each letter to its rank, then check adjacent words are non-decreasing
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))  # expected: True
    print(sol.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"))  # expected: False
    print(sol.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"))  # expected: False
