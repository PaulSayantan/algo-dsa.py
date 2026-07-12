"""Rabin-Karp pattern matching via a polynomial rolling hash.

Use a fixed base and modulus and roll the window hash in O(1) per shift; verify
every hash hit with a direct slice comparison to rule out collisions.
"""
from typing import List  # noqa: F401


class Solution:
    BASE = 911382323
    MOD = 972663749

    def matchIndices(self, text: str, pattern: str) -> List[int]:
        # TODO: rolling polynomial hash; return all match start indices
        pass

    def countOccurrences(self, text: str, pattern: str) -> int:
        # TODO
        pass

    def strStr(self, haystack: str, needle: str) -> int:
        # TODO: index of first occurrence, or -1 (empty needle -> 0)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countOccurrences("mississippi", "iss"))  # expected: 2
    print(sol.countOccurrences("aaaa", "a"))  # expected: 4
    print(sol.countOccurrences("abcabcabc", "abc"))  # expected: 3
    print(sol.countOccurrences("abcabcabc", "d"))  # expected: 0
