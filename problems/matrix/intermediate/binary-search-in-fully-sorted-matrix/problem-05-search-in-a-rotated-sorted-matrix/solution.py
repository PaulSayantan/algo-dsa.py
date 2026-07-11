"""Search in a Rotated Sorted Matrix (matrix variant of LeetCode 33).

Empty solution template — fill in the body yourself.
"""
from typing import List


class Solution:
    def searchRotated(self, matrix: List[List[int]], target: int) -> List[int]:
        """Locate ``target`` in a row-major rotated-sorted matrix of distinct ints.

        The row-major flattening of the matrix is a strictly-increasing array
        rotated left at an unknown pivot. Run a rotated-array binary search over
        the virtual index range ``[0, m*n - 1]``: at each ``mid``, one side of the
        range is sorted; check whether ``target`` falls within that sorted side to
        decide which half to keep. Map a flat index ``idx`` to the cell
        ``matrix[idx // n][idx % n]``.

        Args:
            matrix: An ``m x n`` grid whose row-major flattening is a rotated
                sorted array of distinct integers.
            target: The integer value to search for.

        Returns:
            ``[row, col]`` of ``target`` if present, otherwise ``[-1, -1]``.

        Example:
            >>> Solution().searchRotated([[4, 5, 6], [7, 8, 0], [1, 2, 3]], 8)
            [1, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[4, 5, 6], [7, 8, 0], [1, 2, 3]]
    print(Solution().searchRotated(grid, 8))   # expected: [1, 1]
    print(Solution().searchRotated(grid, 3))   # expected: [2, 2]
    print(Solution().searchRotated(grid, 10))  # expected: [-1, -1]
