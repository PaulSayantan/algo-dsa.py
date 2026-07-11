"""The Skyline Problem (LeetCode 218).

Fill in `Solution.getSkyline` using a 1D sweep line with a max-heap of active
building heights. This file is an intentionally empty template — no working
solution is provided.
"""

from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """Compute the skyline key points from the given buildings.

        Sweep a vertical line across the x-axis over building start/end events.
        Keep the multiset of heights of buildings currently crossing the line
        (a max-heap, typically with lazy deletion). At each event the skyline
        height is the current maximum active height; emit a key point [x, h]
        only when that maximum changes from the previously emitted height.

        Args:
            buildings: List of [left, right, height] rectangles on the ground,
                sorted by left in non-decreasing order.

        Returns:
            The skyline as a list of [x, height] key points sorted by x, with no
            two consecutive points of equal height and a trailing height-0 point.

        Example:
            >>> Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12],
            ...                        [15, 20, 10], [19, 24, 8]])
            [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
    # expected: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print(sol.getSkyline([[0, 2, 3], [2, 5, 3]]))
    # expected: [[0, 3], [5, 0]]
    print(sol.getSkyline([[1, 2, 1], [1, 2, 2], [1, 2, 3]]))
    # expected: [[1, 3], [2, 0]]
