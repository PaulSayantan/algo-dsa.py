from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Search for ``target`` in a row- and column-sorted matrix.

        Each row is sorted ascending left-to-right and each column is sorted
        ascending top-to-bottom (a Young tableau). Aim for O(m + n) time and
        O(1) extra space using a staircase / saddleback walk.

        Args:
            matrix: An ``m x n`` grid where every row and every column is sorted
                in ascending order.
            target: The value to search for.

        Returns:
            ``True`` if ``target`` appears somewhere in ``matrix``, else ``False``.

        Example:
            >>> Solution().searchMatrix([[1, 4], [2, 5]], 5)
            True
            >>> Solution().searchMatrix([[1, 4], [2, 5]], 3)
            False
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(Solution().searchMatrix(grid, 5))   # expected: True
    print(Solution().searchMatrix(grid, 20))  # expected: False
