"""Transpose Matrix (LeetCode 867).

Empty solution template — implement the logic yourself.
"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        """Return the transpose of an ``m x n`` matrix.

        Args:
            matrix: A 2D list with ``m`` rows and ``n`` columns.

        Returns:
            A new 2D list with ``n`` rows and ``m`` columns such that
            ``result[j][i] == matrix[i][j]`` for all valid ``i`` and ``j``.

        Example:
            >>> Solution().transpose([[1, 2, 3], [4, 5, 6]])
            [[1, 4], [2, 5], [3, 6]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().transpose(sample))
    # Expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    sample2 = [[1, 2, 3], [4, 5, 6]]
    print(Solution().transpose(sample2))
    # Expected: [[1, 4], [2, 5], [3, 6]]
