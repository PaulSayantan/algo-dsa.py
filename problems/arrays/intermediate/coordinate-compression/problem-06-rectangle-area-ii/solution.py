"""Rectangle Area II (LeetCode 850).

Fill in the body of `rectangleArea`. The intended approach compresses the
x-coordinates and sweeps a line over the y-edges. Do NOT read SOLUTION.md until you
have attempted it.
"""

from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """Return the total area covered by the union of the rectangles, modulo 1e9+7.

        Each rectangle is [x1, y1, x2, y2] with (x1, y1) the bottom-left corner and
        (x2, y2) the top-right corner. Overlapping area is counted only once.

        Args:
            rectangles: A list of [x1, y1, x2, y2] rectangles.

        Returns:
            The area of the union of all rectangles, taken modulo 10**9 + 7.

        Example:
            >>> Solution().rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]])
            6
        """
        # TODO: implement
        # Hint: compress the distinct x values into strips. Build y-events
        #       (y, x1, x2, +1 at bottom edge / -1 at top edge). Sweep y upward;
        #       between consecutive event ys, sum the widths of strips currently
        #       covered (active count > 0) and add covered_width * delta_y.
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]))  # expected: 6
    print(sol.rectangleArea([[0, 0, 1000000000, 1000000000]]))            # expected: 49
