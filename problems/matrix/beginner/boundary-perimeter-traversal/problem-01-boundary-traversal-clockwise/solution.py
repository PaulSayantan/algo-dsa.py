"""Boundary Traversal of a Matrix (Clockwise).

Fill in the body of `boundary_traversal`. Do not change the signature.
"""

from typing import List


def boundary_traversal(matrix: List[List[int]]) -> List[int]:
    """Return the boundary (outer ring) of ``matrix`` in clockwise order.

    Args:
        matrix: An ``m x n`` rectangular matrix of integers with ``m, n >= 1``.

    Returns:
        A list containing every boundary element exactly once, ordered clockwise
        starting at the top-left corner: top row left-to-right, right column
        top-to-bottom, bottom row right-to-left, left column bottom-to-top.

    Example:
        >>> boundary_traversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(boundary_traversal(grid))
    # Expected: [1, 2, 3, 6, 9, 8, 7, 4]

    print(boundary_traversal([[10, 20, 30]]))
    # Expected: [10, 20, 30]
