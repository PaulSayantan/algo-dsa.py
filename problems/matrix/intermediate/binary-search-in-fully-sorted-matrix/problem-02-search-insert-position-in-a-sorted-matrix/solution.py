"""Search Insert Position in a Sorted Matrix (matrix variant of LeetCode 35).

Empty solution template — fill in the body yourself.
"""
from typing import List


class Solution:
    def searchInsert(self, matrix: List[List[int]], target: int) -> int:
        """Return the flat lower_bound index for ``target`` in a sorted matrix.

        The matrix is sorted in row-major order. Treat it as a virtual sorted
        array of ``m * n`` elements and binary search for the first flat index
        whose value is ``>= target``. Map a flat index ``idx`` to the cell
        ``matrix[idx // n][idx % n]``. If ``target`` exceeds every element,
        return ``m * n``.

        Args:
            matrix: An ``m x n`` grid sorted in row-major order (duplicates ok).
            target: The integer value to locate or insert.

        Returns:
            The flat index in ``[0, m * n]`` where ``target`` is or would be
            inserted to keep the row-major sequence sorted.

        Example:
            >>> Solution().searchInsert([[1, 3, 5], [6, 8, 9]], 7)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 3, 5], [6, 8, 9]]
    print(Solution().searchInsert(grid, 5))    # expected: 2
    print(Solution().searchInsert(grid, 7))    # expected: 4
    print(Solution().searchInsert(grid, 10))   # expected: 6
