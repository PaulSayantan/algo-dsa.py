"""Maximum in Every k×k Window — empty solution template.

Fill in the logic yourself. Build a 2D Sparse Table for `max`, then query the
top-left corner of every k x k window in O(1).
"""
from typing import List


class Solution:
    def max_in_k_windows(
        self,
        grid: List[List[int]],
        k: int,
    ) -> List[List[int]]:
        """Return the maximum of every k x k window in the grid.

        Args:
            grid: An `n x m` matrix of integers.
            k: The side length of each square window; `1 <= k <= min(n, m)`.

        Returns:
            A `(n - k + 1) x (m - k + 1)` matrix where entry `(i, j)` is the
            maximum value in the `k x k` window whose top-left corner is
            `(i, j)`.

        Example:
            >>> Solution().max_in_k_windows(
            ...     [[1, 5, 2, 9], [4, 3, 8, 1],
            ...      [7, 2, 6, 3], [2, 9, 4, 5]], 2)
            [[5, 8, 9], [7, 8, 8], [9, 9, 6]]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[1, 5, 2, 9], [4, 3, 8, 1], [7, 2, 6, 3], [2, 9, 4, 5]]
    print(Solution().max_in_k_windows(grid, 2))
    # Expected: [[5, 8, 9], [7, 8, 8], [9, 9, 6]]
    print(Solution().max_in_k_windows(grid, 3))
    # Expected: [[8, 9], [9, 9]]
