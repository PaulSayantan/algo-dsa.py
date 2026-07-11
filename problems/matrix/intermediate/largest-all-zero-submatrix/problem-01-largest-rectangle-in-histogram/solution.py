"""Largest Rectangle in Histogram (LeetCode 84).

Empty solution template — fill in the logic yourself.
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Return the area of the largest rectangle in the histogram.

        Args:
            heights: Heights of the histogram bars, each of width 1.

        Returns:
            The maximum rectangular area that fits entirely under the bars.

        Example:
            >>> Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
            10
        """
        # TODO: implement using a monotonic (increasing) stack of bar indices.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # expected: 10
    print(sol.largestRectangleArea([2, 4]))              # expected: 4
    print(sol.largestRectangleArea([2, 1, 2]))           # expected: 3
