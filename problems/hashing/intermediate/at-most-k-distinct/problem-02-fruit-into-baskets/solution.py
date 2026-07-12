"""Fruit Into Baskets — LeetCode 904."""
from typing import List  # noqa: F401
from collections import defaultdict  # noqa: F401


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # TODO: longest window with at most 2 distinct fruit types
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit([1, 2, 1]))  # expected: 3
    print(sol.totalFruit([0, 1, 2, 2]))  # expected: 3
    print(sol.totalFruit([1, 2, 3, 2, 2]))  # expected: 4
    print(sol.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # expected: 5
