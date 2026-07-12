"""Trapping Rain Water — LeetCode 42 (stack method)."""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # TODO: monotonic decreasing stack of indices
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # expected: 6
    print(sol.trap([4, 2, 0, 3, 2, 5]))  # expected: 9
    print(sol.trap([1, 2, 3]))  # expected: 0
