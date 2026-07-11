"""Largest Rectangle in Histogram — LeetCode 84.

Empty solution template. Fill in the body yourself.
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Return the area of the largest rectangle fitting under the histogram.

        Each bar has width 1. A rectangle may span any contiguous range of bars,
        and its height is bounded by the shortest bar in that range.

        Args:
            heights: Non-negative bar heights, left to right.

        Returns:
            The maximum rectangular area that fits entirely within the histogram.

        Example:
            >>> Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
            10
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))     # expected: 10
    print(sol.largestRectangleArea([2, 4]))                 # expected: 4
    print(sol.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))  # expected: 12
