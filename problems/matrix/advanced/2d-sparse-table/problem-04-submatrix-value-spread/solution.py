"""Submatrix Value Spread — empty solution template.

Fill in the logic yourself. Build one 2D Sparse Table for `max` and one for
`min`; each query's answer is maxQuery - minQuery.
"""
from typing import List


class Solution:
    def submatrix_spreads(
        self,
        grid: List[List[int]],
        queries: List[List[int]],
    ) -> List[int]:
        """Answer submatrix (max - min) spread queries on a fixed matrix.

        Args:
            grid: An `n x m` matrix of integers that never changes.
            queries: A list of queries, each `[r1, c1, r2, c2]` giving the
                inclusive top-left `(r1, c1)` and bottom-right `(r2, c2)`
                corners of a rectangle (all 0-indexed).

        Returns:
            A list where the i-th element is `max - min` over the rectangle
            described by `queries[i]`.

        Example:
            >>> Solution().submatrix_spreads(
            ...     [[7, 2, 9, 1], [4, 6, 3, 8], [5, 0, 2, 7], [1, 9, 4, 6]],
            ...     [[0, 0, 1, 1], [1, 1, 3, 3], [2, 2, 2, 2]],
            ... )
            [5, 9, 0]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [[7, 2, 9, 1], [4, 6, 3, 8], [5, 0, 2, 7], [1, 9, 4, 6]]
    queries = [[0, 0, 1, 1], [1, 1, 3, 3], [2, 2, 2, 2]]
    print(Solution().submatrix_spreads(grid, queries))
    # Expected: [5, 9, 0]
