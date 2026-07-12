"""Unique Number of Occurrences — LeetCode 1207."""
from collections import Counter  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # TODO: count values, then check the counts are all distinct
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # expected: True
    print(sol.uniqueOccurrences([1, 2]))  # expected: False
    print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # expected: True
