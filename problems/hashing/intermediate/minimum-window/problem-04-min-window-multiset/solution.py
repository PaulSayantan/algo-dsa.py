"""Minimum window containing a multiset target (integer array)."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def minWindowMultiset(self, nums: List[int], target: List[int]) -> int:
        # TODO: need = Counter(target); shrink each covering window; return its min length (0 if none)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindowMultiset([1, 2, 3, 2, 1], [1, 2]))  # expected: 2
    print(sol.minWindowMultiset([1, 2, 2, 3], [2, 2]))  # expected: 2
    print(sol.minWindowMultiset([1, 1, 1], [2]))  # expected: 0
    print(sol.minWindowMultiset([7, 3, 7, 3, 7], [3, 3]))  # expected: 3
