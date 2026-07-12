"""Number of Equivalent Domino Pairs — LeetCode 1128."""
from collections import defaultdict  # noqa: F401
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # TODO: canonical (min,max) key; add running count then increment
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))  # expected: 1
    print(sol.numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))  # expected: 3
    print(sol.numEquivDominoPairs([[1, 1]]))  # expected: 0
