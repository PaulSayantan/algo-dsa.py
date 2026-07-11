"""Largest Uniform Square — empty solution template.

Fill in the logic yourself. Build 2D Sparse Tables for `max` and `min`, then
binary search on the side length L, checking every L x L window's spread in
O(1).
"""
from typing import List


class Solution:
    def largest_uniform_square(
        self,
        grid: List[List[int]],
        D: int,
    ) -> int:
        """Return the side length of the largest square with spread <= D.

        A square submatrix qualifies if (max value - min value) <= D. A single
        cell always qualifies, so the answer is at least 1.

        Args:
            grid: An `n x m` matrix of integers.
            D: The maximum allowed spread (max - min) inside a qualifying
                square; `D >= 0`.

        Returns:
            The side length L of the largest axis-aligned square submatrix whose
            value spread is at most D.

        Example:
            >>> Solution().largest_uniform_square(
            ...     [[1, 2, 3, 8], [2, 3, 4, 9],
            ...      [3, 4, 5, 10], [9, 9, 9, 1]], 2)
            2
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 2, 3, 8], [2, 3, 4, 9], [3, 4, 5, 10], [9, 9, 9, 1]]
    print(Solution().largest_uniform_square(grid, 2))
    # Expected: 2
    print(Solution().largest_uniform_square(grid, 4))
    # Expected: 3
