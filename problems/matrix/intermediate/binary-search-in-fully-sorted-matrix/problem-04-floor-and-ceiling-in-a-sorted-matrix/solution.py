"""Floor and Ceiling in a Sorted Matrix.

Empty solution template — fill in the body yourself.
"""
from typing import List


class Solution:
    def floorAndCeil(self, matrix: List[List[int]], target: int) -> List[int]:
        """Return ``[floor, ceil]`` of ``target`` in a row-major sorted matrix.

        Treat the matrix as a virtual sorted array of ``m * n`` elements. Binary
        search for ``lower_bound(target)`` (first flat index whose value is
        ``>= target``): the ceiling is the value there (or -1 if the bound is past
        the end), and the floor is the value just before it (or -1 if the bound is
        at index 0 and that first value already exceeds target). Map a flat index
        ``idx`` to the cell ``matrix[idx // n][idx % n]``.

        Args:
            matrix: An ``m x n`` grid sorted in row-major order (duplicates ok).
            target: The reference integer value.

        Returns:
            A two-element list ``[floor, ceil]``. ``floor`` is the largest value
            ``<= target`` or -1 if none; ``ceil`` is the smallest value
            ``>= target`` or -1 if none.

        Example:
            >>> Solution().floorAndCeil([[1, 4, 7], [10, 13, 16]], 12)
            [10, 13]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 4, 7], [10, 13, 16]]
    print(Solution().floorAndCeil(grid, 12))  # expected: [10, 13]
    print(Solution().floorAndCeil(grid, 7))   # expected: [7, 7]
    print(Solution().floorAndCeil(grid, 20))  # expected: [16, -1]
