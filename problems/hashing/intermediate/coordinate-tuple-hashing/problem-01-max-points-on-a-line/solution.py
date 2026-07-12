"""Max Points on a Line — LeetCode 149."""
from collections import defaultdict  # noqa: F401
import math  # noqa: F401
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # TODO: for each anchor, hash GCD+sign-normalized slope tuples
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxPoints([[1, 1], [2, 2], [3, 3]]))  # expected: 3
    print(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))  # expected: 4
    print(sol.maxPoints([[0, 0]]))  # expected: 1
