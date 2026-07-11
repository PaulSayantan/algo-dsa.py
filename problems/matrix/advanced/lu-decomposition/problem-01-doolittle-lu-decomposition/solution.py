"""Doolittle LU Decomposition.

Factor a square matrix A into L (unit lower triangular) and U (upper
triangular) so that A = L @ U, without pivoting.
"""

from typing import List, Tuple

Matrix = List[List[float]]


def lu_decompose(A: Matrix) -> Tuple[Matrix, Matrix]:
    """Factor A into unit-lower-triangular L and upper-triangular U (A = L @ U).

    Uses the Doolittle convention (L has 1's on its diagonal). Assumes every
    pivot U[k][k] encountered is non-zero, so no row pivoting is needed.

    Args:
        A: An n x n matrix given as a list of n lists of n floats. It is left
            unmodified.

    Returns:
        A tuple ``(L, U)`` where ``L`` is n x n unit lower triangular and ``U``
        is n x n upper triangular, satisfying ``L @ U == A``.

    Example:
        >>> L, U = lu_decompose([[4, 3], [6, 3]])
        >>> L
        [[1.0, 0.0], [1.5, 1.0]]
        >>> U
        [[4.0, 3.0], [0.0, -1.5]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    A = [[2, -1, -2],
         [-4, 6, 3],
         [-4, -2, 8]]
    print(lu_decompose(A))
    # Expected L = [[1, 0, 0], [-2, 1, 0], [-2, -1, 1]]
    # Expected U = [[2, -1, -2], [0, 4, -1], [0, 0, 3]]
