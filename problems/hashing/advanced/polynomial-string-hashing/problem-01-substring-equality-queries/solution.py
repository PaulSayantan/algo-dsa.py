"""Polynomial prefix hashing for O(1) substring-equality queries.

Precompute prefix hashes H[0..n] and powers PW[0..n] with a fixed base/modulus;
the hash of s[l..r] is (H[r+1] - H[l]*PW[r-l+1]) % MOD.
"""
from typing import List, Tuple  # noqa: F401


class Solution:
    BASE = 911382323
    MOD = 972663749

    def equalSubstrings(self, s: str, queries: List[Tuple[int, int, int]]) -> List[bool]:
        # TODO: prefix hashes; answer each (a, b, length) query in O(1)
        pass

    def countDistinctOfLength(self, s: str, L: int) -> int:
        # TODO: collect the hash of every length-L window in a set
        pass

    def substringsEqual(self, s: str, a: int, b: int, L: int) -> bool:
        # TODO: compare hash(s[a:a+L]) with hash(s[b:b+L])
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.equalSubstrings("ababab", [(0, 2, 2), (0, 1, 2), (0, 2, 4)]))  # expected: [True, False, True]
    print(sol.equalSubstrings("aaaaa", [(0, 1, 3), (2, 2, 2), (0, 3, 2)]))  # expected: [True, True, True]
    print(sol.equalSubstrings("mississippi", [(1, 4, 4), (0, 0, 5), (2, 5, 2)]))  # expected: [True, True, True]
