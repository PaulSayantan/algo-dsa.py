"""Largest Rectangle in Histogram — LeetCode 84."""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # TODO: monotonic increasing stack of indices
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # expected: 10
    print(sol.largestRectangleArea([2, 4]))  # expected: 4
    print(sol.largestRectangleArea([5]))  # expected: 5
    print(sol.largestRectangleArea([1, 1, 1, 1]))  # expected: 4
