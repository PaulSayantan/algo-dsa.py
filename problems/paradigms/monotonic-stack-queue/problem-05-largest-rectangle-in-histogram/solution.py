"""Largest Rectangle in Histogram — LeetCode 84.

Fill in the body of `largestRectangleArea`. Do not modify the signature.
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Return the area of the largest rectangle that fits in the histogram.

        Args:
            heights: A list of non-negative bar heights, each bar having width 1.

        Returns:
            The maximum rectangular area bounded by the histogram bars.

        Example:
            >>> Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
            10
        """
        # TODO: implement using a monotonic increasing stack of indices.
        # When the current bar is shorter than the stack top, pop and compute the
        # area with the popped bar as the limiting height; width spans from the new
        # stack top (exclusive) to the current index (exclusive).
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # expected: 10
    print(sol.largestRectangleArea([2, 4]))              # expected: 4
