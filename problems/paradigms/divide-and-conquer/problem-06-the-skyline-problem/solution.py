"""The Skyline Problem — LeetCode 218.

Empty solution template. Solve it with Divide and Conquer: recursively compute
each half's skyline, then merge the two skylines.
"""
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """Return the skyline as key points [x, y] sorted by x.

        Split the buildings into two halves, recursively compute each half's
        skyline, and merge the two contours with a left-to-right sweep that
        tracks the current height on each side and emits a key point whenever
        the running max changes. Collapse consecutive equal-height segments.

        Args:
            buildings: Each entry is [left, right, height] with left < right.
                The list is sorted by left in non-decreasing order.

        Returns:
            The skyline key points [x, y], sorted by x, with no two consecutive
            segments of equal height; the final point has height 0.

        Example:
            >>> Solution().getSkyline([[0, 2, 3], [2, 5, 3]])
            [[0, 3], [5, 0]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # expected: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(sol.getSkyline([[0, 2, 3], [2, 5, 3]]))
    # expected: [[0, 3], [5, 0]]
