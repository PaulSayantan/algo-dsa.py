"""Unique Number of Occurrences — LeetCode 1207."""
from typing import List  # noqa: F401


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # TODO: return True iff every value's occurrence-count is distinct
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # expected: True
    print(sol.uniqueOccurrences([1, 2]))  # expected: False
    print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))  # expected: True
    print(sol.uniqueOccurrences([1, 1, 2, 2, 3, 3]))  # expected: False
