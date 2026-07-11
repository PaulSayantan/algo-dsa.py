"""Rectangle Area II (LeetCode 850).

Return the total area of the union of axis-aligned rectangles, modulo 1e9+7.
Solve with coordinate compression + a 2D difference array to mark covered cells.
"""

from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """Return the union area of all rectangles, modulo 10**9 + 7.

        Args:
            rectangles: List of [x1, y1, x2, y2] with x1 < x2 and y1 < y2;
                (x1, y1) is the bottom-left and (x2, y2) the top-right corner.
                Coordinates can be as large as 10**9.

        Returns:
            The area of the union of all rectangles, taken modulo 10**9 + 7.
            Overlapping regions are counted only once.

        Example:
            >>> Solution().rectangleArea([[0, 0, 2, 2], [1, 1, 3, 3]])
            7
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))
    # Expected: 6

    print(sol.rectangleArea([[0, 0, 2, 2], [1, 1, 3, 3]]))
    # Expected: 7
