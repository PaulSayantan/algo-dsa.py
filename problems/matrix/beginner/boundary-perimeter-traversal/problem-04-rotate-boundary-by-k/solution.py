"""Rotate the Boundary of a Matrix by K (clockwise).

Fill in the body of `rotate_boundary`. Do not change the signature.
"""

from typing import List


def rotate_boundary(matrix: List[List[int]], k: int) -> List[List[int]]:
    """Rotate only the boundary (outer ring) of ``matrix`` clockwise by ``k``.

    The boundary is treated as a circular sequence read clockwise from the
    top-left corner. Interior cells are left unchanged. ``k`` may exceed the
    number of boundary cells and should be reduced modulo that count.

    Args:
        matrix: An ``m x n`` rectangular matrix of integers with ``m, n >= 1``.
            May be modified in place.
        k: Number of clockwise positions to rotate the boundary by (``k >= 0``).

    Returns:
        The matrix with its boundary rotated clockwise by ``k`` and its interior
        preserved.

    Example:
        >>> rotate_boundary([[1, 2, 3], [8, 9, 4], [7, 6, 5]], 1)
        [[8, 1, 2], [7, 9, 3], [6, 5, 4]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5],
    ]
    print(rotate_boundary(grid, 1))
    # Expected: [[8, 1, 2], [7, 9, 3], [6, 5, 4]]

    print(rotate_boundary([[1, 2, 3]], 4))
    # Expected: [[3, 1, 2]]
