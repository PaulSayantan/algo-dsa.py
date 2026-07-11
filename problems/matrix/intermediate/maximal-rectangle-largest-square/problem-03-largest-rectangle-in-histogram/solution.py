from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Return the area of the largest rectangle fitting inside a histogram.

        Args:
            heights: Bar heights, each bar having width 1, left to right.

        Returns:
            The maximum area of any axis-aligned rectangle bounded by the bars,
            where a rectangle spanning a contiguous range of bars is capped at
            the height of the shortest bar in that range.

        Example:
            >>> Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
            10
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Expected: 10
    print(Solution().largestRectangleArea([6, 2, 5, 4, 5, 1, 6]))  # Expected: 12
