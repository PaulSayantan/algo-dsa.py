"""Josephus last two survivors: stop at two remaining, return them sorted ascending."""
from collections import deque  # noqa: F401
from typing import List  # noqa: F401


class Solution:
    def lastTwoSurvivors(self, n: int, k: int) -> List[int]:
        # TODO: seat 1..n in a queue; rotate k-1 to the back and remove the k-th,
        # but stop while more than two remain; return the final two sorted ascending
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.lastTwoSurvivors(7, 3))  # expected: [1, 4]
    print(sol.lastTwoSurvivors(5, 2))  # expected: [3, 5]
    print(sol.lastTwoSurvivors(6, 2))  # expected: [1, 5]
    print(sol.lastTwoSurvivors(2, 5))  # expected: [1, 2]
