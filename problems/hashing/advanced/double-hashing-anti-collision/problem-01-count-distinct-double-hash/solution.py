"""Double hashing: combine two independent (base, mod) channels into a tuple key.

Using two moduli makes adversarial hash collisions astronomically unlikely, so a
tuple of the two hashes can stand in for the string itself as a dict/set key.
"""
from typing import List  # noqa: F401


class Solution:
    BASE1 = 911382323
    MOD1 = 972663749
    BASE2 = 998244353
    MOD2 = 1000000007

    def countDistinctOfLength(self, s: str, L: int) -> int:
        # TODO: hash every length-L window on TWO channels; count distinct (h1, h2) pairs
        pass

    def hasRepeatOfLength(self, s: str, L: int) -> bool:
        # TODO: detect whether any length-L window's (h1, h2) key repeats
        pass

    def stringsEqual(self, a: str, b: str) -> bool:
        # TODO: compare a and b via their double-hash keys
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.countDistinctOfLength("mississippi", 3))  # expected: 7
    print(sol.countDistinctOfLength("abcdefg", 2))  # expected: 6
    print(sol.countDistinctOfLength("aaaaaa", 1))  # expected: 1
    print(sol.countDistinctOfLength("banana", 3))  # expected: 3
