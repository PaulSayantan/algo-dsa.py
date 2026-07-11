"""Sort the Boundary Elements of a Matrix.

Fill in the body of `sort_boundary`. Do not change the signature.
"""

from typing import List


def sort_boundary(matrix: List[List[int]]) -> List[List[int]]:
    """Sort only the boundary (outer ring) of ``matrix`` in ascending order.

    The boundary is read clockwise from the top-left corner, sorted, then written
    back along the same clockwise path. Interior cells are left unchanged.

    Args:
        matrix: An ``m x n`` rectangular matrix of integers with ``m, n >= 1``.
            May be modified in place.

    Returns:
        The matrix with its boundary sorted clockwise and its interior preserved.

    Example:
        >>> sort_boundary([[1, 4, 3], [7, 5, 2], [9, 6, 8]])
        [[1, 2, 3], [9, 5, 4], [8, 7, 6]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    grid = [
        [1, 4, 3],
        [7, 5, 2],
        [9, 6, 8],
    ]
    print(sort_boundary(grid))
    # Expected: [[1, 2, 3], [9, 5, 4], [8, 7, 6]]

    print(sort_boundary([[3, 1, 2]]))
    # Expected: [[1, 2, 3]]
