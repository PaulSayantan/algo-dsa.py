"""Histogram largest rectangle — edge-case variant."""
from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # TODO
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([]))  # expected: 0
    print(sol.maxArea([6, 2, 5, 4, 5, 1, 6]))  # expected: 12
    print(sol.maxArea([3, 3, 3]))  # expected: 9
