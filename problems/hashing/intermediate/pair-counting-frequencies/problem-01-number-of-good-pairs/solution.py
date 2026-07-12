"""Number of Good Pairs — LeetCode 1512."""
from typing import List  # noqa: F401
from collections import Counter  # noqa: F401


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # TODO: for each value with frequency f, add f*(f-1)//2 pairs
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIdenticalPairs([1, 2, 3, 1, 1, 3]))  # expected: 4
    print(sol.numIdenticalPairs([1, 1, 1, 1]))  # expected: 6
    print(sol.numIdenticalPairs([1, 2, 3]))  # expected: 0
    print(sol.numIdenticalPairs([1, 1, 1]))  # expected: 3
