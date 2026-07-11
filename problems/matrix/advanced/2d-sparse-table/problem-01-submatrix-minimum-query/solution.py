"""Submatrix Minimum Query — empty solution template.

Fill in the logic yourself. Build a 2D Sparse Table for `min` once, then
answer each query in O(1).
"""
from typing import List


class Solution:
    def submatrix_minimums(
        self,
        grid: List[List[int]],
        queries: List[List[int]],
    ) -> List[int]:
        """Answer submatrix-minimum queries on a fixed matrix.

        Args:
            grid: An `n x m` matrix of integers that never changes.
            queries: A list of queries, each `[r1, c1, r2, c2]` giving the
                inclusive top-left `(r1, c1)` and bottom-right `(r2, c2)`
                corners of a rectangle (all 0-indexed).

        Returns:
            A list where the i-th element is the minimum value inside the
            rectangle described by `queries[i]`.

        Example:
            >>> Solution().submatrix_minimums(
            ...     [[7, 2, 9, 1], [4, 6, 3, 8], [5, 0, 2, 7], [1, 9, 4, 6]],
            ...     [[0, 0, 1, 1], [1, 1, 3, 3], [0, 2, 2, 3]],
            ... )
            [2, 0, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[7, 2, 9, 1], [4, 6, 3, 8], [5, 0, 2, 7], [1, 9, 4, 6]]
    queries = [[0, 0, 1, 1], [1, 1, 3, 3], [0, 2, 2, 3]]
    print(Solution().submatrix_minimums(grid, queries))
    # Expected: [2, 0, 1]
