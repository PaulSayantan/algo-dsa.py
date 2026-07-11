"""
Submatrix Maximum with Point Updates.

Given an n x m matrix, support:
    ("update", r, c, v)            -> set cell (r, c) to v
    ("query",  r1, c1, r2, c2)     -> max value over the inclusive submatrix

Return the answer to every "query", in order.

Because max is NOT invertible, a Fenwick tree cannot do range-max with general
point updates. Use a 2D Segment Tree: an outer segment tree over rows whose
every node owns an inner segment tree over columns storing the max.

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List, Tuple, Union

Operation = Union[Tuple[str, int, int, int], Tuple[str, int, int, int, int]]


class Matrix2DSegmentTree:
    def __init__(self, matrix: List[List[int]]) -> None:
        """
        Build a 2D segment tree over the given matrix for range-max queries.

        Args:
            matrix: The initial n x m integer grid (n >= 1, m >= 1).

        Returns:
            None.
        """
        # TODO: implement
        # Typical layout: self.tree is a 2D array of size (4*n) x (4*m).
        # Build the outer tree over rows; at each outer node build/merge the
        # inner column tree. Leaf outer nodes copy a row; internal outer nodes
        # store the element-wise max of their two children's inner trees.
        pass

    def update(self, r: int, c: int, v: int) -> None:
        """
        Set matrix[r][c] = v and refresh all affected tree nodes.

        Args:
            r: 0-indexed row of the cell.
            c: 0-indexed column of the cell.
            v: New value to store.

        Returns:
            None.
        """
        # TODO: implement
        # Recurse the outer (row) tree to the leaf covering r; on the way back
        # up, update the inner (column) tree at each visited outer node at
        # position c, taking maxima of children where appropriate.
        pass

    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        Return the maximum value in the inclusive submatrix
        [r1..r2] x [c1..c2].

        Args:
            r1: Top row (inclusive).
            c1: Left column (inclusive).
            r2: Bottom row (inclusive).
            c2: Right column (inclusive).

        Returns:
            The maximum cell value in the submatrix.
        """
        # TODO: implement
        # Descend the outer tree collecting the O(log n) canonical row-bands
        # that cover [r1..r2]; on each, run an inner column query over [c1..c2]
        # and combine the results with max.
        pass


def process(matrix: List[List[int]], operations: List[Operation]) -> List[int]:
    """
    Run all operations against a 2D segment tree and collect query answers.

    Args:
        matrix: The initial n x m grid.
        operations: Each item is either ("update", r, c, v) or
            ("query", r1, c1, r2, c2).

    Returns:
        A list of the answers to the "query" operations, in order.

    Example:
        process([[1,3,2],[4,0,5],[7,6,1]],
                [("query",0,0,1,1), ("update",0,1,9),
                 ("query",0,0,1,1), ("query",1,1,2,2)])
        # -> [4, 9, 6]
    """
    # TODO: implement (construct Matrix2DSegmentTree, dispatch each op)
    pass


if __name__ == "__main__":
    mat = [[1, 3, 2], [4, 0, 5], [7, 6, 1]]
    ops = [
        ("query", 0, 0, 1, 1),
        ("update", 0, 1, 9),
        ("query", 0, 0, 1, 1),
        ("query", 1, 1, 2, 2),
    ]
    print(process(mat, ops))  # expected: [4, 9, 6]
