"""Sum of Boundary Elements of a Matrix.

Fill in the body of `boundary_sum`. Do not change the signature.
"""

from typing import List


def boundary_sum(matrix: List[List[int]]) -> int:
    """Return the sum of all boundary (perimeter) elements of ``matrix``.

    Each of the four corner cells belongs to two sides but must be counted only
    once. Interior cells are excluded entirely.

    Args:
        matrix: An ``m x n`` rectangular matrix of integers with ``m, n >= 1``.

    Returns:
        The integer sum of every distinct boundary element.

    Example:
        >>> boundary_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        40
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print(boundary_sum(grid))
    # Expected: 40

    print(boundary_sum([[5, 6, 7]]))
    # Expected: 18
