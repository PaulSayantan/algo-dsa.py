"""Submatrix GCD Query — empty solution template.

Fill in the logic yourself. Build a 2D Sparse Table whose merge function is
`math.gcd`, then answer each query in O(1).
"""
from typing import List


class Solution:
    def submatrix_gcds(
        self,
        grid: List[List[int]],
        queries: List[List[int]],
    ) -> List[int]:
        """Answer submatrix-gcd queries on a fixed matrix.

        Args:
            grid: An `n x m` matrix of positive integers that never changes.
            queries: A list of queries, each `[r1, c1, r2, c2]` giving the
                inclusive top-left `(r1, c1)` and bottom-right `(r2, c2)`
                corners of a rectangle (all 0-indexed).

        Returns:
            A list where the i-th element is the gcd of all values inside the
            rectangle described by `queries[i]`.

        Example:
            >>> Solution().submatrix_gcds(
            ...     [[12, 18, 6, 24], [9, 15, 30, 3],
            ...      [8, 16, 12, 20], [21, 7, 14, 28]],
            ...     [[0, 0, 1, 1], [3, 0, 3, 3], [0, 2, 1, 3], [0, 0, 3, 3]],
            ... )
            [3, 7, 3, 1]
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    grid = [
        [12, 18, 6, 24],
        [9, 15, 30, 3],
        [8, 16, 12, 20],
        [21, 7, 14, 28],
    ]
    queries = [[0, 0, 1, 1], [3, 0, 3, 3], [0, 2, 1, 3], [0, 0, 3, 3]]
    print(Solution().submatrix_gcds(grid, queries))
    # Expected: [3, 7, 3, 1]
