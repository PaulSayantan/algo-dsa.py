"""Minimum Window Substring — LeetCode 76."""
from collections import Counter  # noqa: F401


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # TODO: two-map (need vs have) window + a satisfaction counter; keep the smallest
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # expected: 'BANC'
    print(sol.minWindow("a", "a"))  # expected: 'a'
    print(sol.minWindow("a", "aa"))  # expected: ''
    print(sol.minWindow("ab", "b"))  # expected: 'b'
