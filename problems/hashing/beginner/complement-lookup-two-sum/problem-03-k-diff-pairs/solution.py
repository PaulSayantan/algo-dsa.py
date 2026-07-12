"""K-diff Pairs in an Array — LeetCode 532. Count unique pairs with abs diff k."""
from typing import List  # noqa: F401


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # TODO: over the DISTINCT values, complement is x + k (special-case k == 0)
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findPairs([3, 1, 4, 1, 5], 2))  # expected: 2
    print(sol.findPairs([1, 2, 3, 4, 5], 1))  # expected: 4
    print(sol.findPairs([1, 3, 1, 5, 4], 0))  # expected: 1
    print(sol.findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3))  # expected: 2
    print(sol.findPairs([-1, -2, -3], 1))  # expected: 2
