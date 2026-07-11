"""Maximum Sum Rectangle with Coordinates.

Empty solution template. Fill in the body yourself.
"""
from typing import List, Tuple


class Solution:
    def maxSumRectangle(self, matrix: List[List[int]]) -> Tuple[int, Tuple[int, int, int, int]]:
        """Return the max rectangle sum together with its bounding box.

        Args:
            matrix: An ``n x m`` grid of integers (may include negatives),
                with at least one cell.

        Returns:
            A tuple ``(best_sum, (top, left, bottom, right))`` where the four
            indices are inclusive 0-based bounds of a rectangle achieving
            ``best_sum``. If several rectangles tie, any one is acceptable.

        Example:
            >>> Solution().maxSumRectangle([
            ...     [ 1,  2, -1, -4, -20],
            ...     [-8, -3,  4,  2,   1],
            ...     [ 3,  8, 10,  1,   3],
            ...     [-4, -1,  1,  7,  -6],
            ... ])
            (29, (1, 1, 3, 3))
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSumRectangle([
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6],
    ]))  # expected: (29, (1, 1, 3, 3))
    print(sol.maxSumRectangle([[-1, -2], [-3, -4]]))  # expected: (-1, (0, 0, 0, 0))
