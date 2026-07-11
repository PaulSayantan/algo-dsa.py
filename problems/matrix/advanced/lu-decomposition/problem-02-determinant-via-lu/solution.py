"""Determinant via LU Decomposition.

Compute det(A) as the signed product of the pivots of U from a PA = LU
factorization, in O(n^3) instead of O(n!).
"""

from typing import List

Matrix = List[List[float]]


def determinant(A: Matrix) -> float:
    """Return the determinant of a square matrix using LU decomposition.

    Factor A (with partial pivoting) as PA = LU; then
    det(A) = (-1)^(number of row swaps) * product(U[i][i]).

    Args:
        A: An n x n matrix given as a list of n lists of n floats. It is left
            unmodified.

    Returns:
        The determinant of ``A`` as a float. Returns ``0.0`` when ``A`` is
        singular.

    Example:
        >>> determinant([[4, 3], [6, 3]])
        -6.0
        >>> determinant([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]])
        24.0
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(determinant([[4, 3], [6, 3]]))                       # Expected: -6.0
    print(determinant([[2, -1, -2], [-4, 6, 3], [-4, -2, 8]]))  # Expected: 24.0
