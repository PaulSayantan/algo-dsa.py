"""LeetCode 84 - Largest Rectangle in Histogram.

Find the area of the largest axis-aligned rectangle that fits under a histogram,
using a monotonic stack that touches each bar a constant number of times (O(n)).
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Return the area of the largest rectangle fitting under the histogram.

        Args:
            heights: Bar heights; each bar has width 1.

        Returns:
            The maximum rectangular area contained within the histogram.

        Example:
            >>> Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
            10
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))       # expected: 10
    print(sol.largestRectangleArea([2, 4]))                    # expected: 4
    print(sol.largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))     # expected: 12
