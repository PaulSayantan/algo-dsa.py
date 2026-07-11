"""LeetCode 73 — Set Matrix Zeroes.

Fill in the body of `setZeroes`. Aim for the O(1) extra-space approach that
reuses the first row and first column of `matrix` as flag storage.
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Zero out the entire row and column of every cell that holds a 0.

        The mutation must happen **in place**: modify ``matrix`` directly and
        return ``None``. Target solution uses only O(1) extra space by treating
        the first row and first column as the row/column zero flags, with two
        booleans tracking whether the first row and first column themselves must
        be cleared.

        Args:
            matrix: An ``m x n`` grid of integers, modified in place.

        Returns:
            None. ``matrix`` is updated in place.

        Example:
            >>> m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
            >>> Solution().setZeroes(m)
            >>> m
            [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sol = Solution()

    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(m1)
    print(m1)  # expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(m2)
    print(m2)  # expected: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    m3 = [[1, 2, 3]]
    sol.setZeroes(m3)
    print(m3)  # expected: [[1, 2, 3]]
