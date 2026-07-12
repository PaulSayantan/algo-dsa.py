"""Find All Anagrams in a String — LeetCode 438."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # TODO: slide a window of len(p); compare its frequency map to Counter(p)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd", "abc"))  # expected: [0, 6]
    print(sol.findAnagrams("abab", "ab"))  # expected: [0, 1, 2]
    print(sol.findAnagrams("a", "aa"))  # expected: []
    print(sol.findAnagrams("baa", "aa"))  # expected: [1]
