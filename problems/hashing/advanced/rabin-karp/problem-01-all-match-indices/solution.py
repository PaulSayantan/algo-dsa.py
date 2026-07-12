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
    print(sol.matchIndices("abababab", "ab"))  # expected: [0, 2, 4, 6]
    print(sol.matchIndices("aaaaa", "aa"))  # expected: [0, 1, 2, 3]
    print(sol.matchIndices("abcabc", "xyz"))  # expected: []
    print(sol.matchIndices("mississippi", "issi"))  # expected: [1, 4]
