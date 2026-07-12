"""Reorganize String — LeetCode 767."""
import heapq  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def reorganizeString(self, s: str) -> str:
        # TODO: max-heap by frequency; emit top char, cool it down one slot before reuse
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.reorganizeString("aab"))  # expected: 'aba'
    print(sol.reorganizeString("aaab"))  # expected: ''
    print(sol.reorganizeString("vvvlo"))  # expected: 'vlvov'
    print(sol.reorganizeString("aaabbbcc"))  # expected: 'ababcabc'
