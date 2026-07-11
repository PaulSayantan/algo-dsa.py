"""Solve a linear system A x = b using LU Decomposition.

Factor A = LU once, then solve L y = b (forward substitution) followed by
U x = y (back substitution). Each triangular solve is O(n^2).
"""

from typing import List

Matrix = List[List[float]]
Vector = List[float]


def solve(A: Matrix, b: Vector) -> Vector:
    """Solve the linear system ``A x = b`` and return ``x``.

    Factor A into unit-lower-triangular L and upper-triangular U (Doolittle),
    then forward-substitute ``L y = b`` and back-substitute ``U x = y``.

    Args:
        A: An n x n non-singular matrix with non-zero pivots (no pivoting
            required). Left unmodified.
        b: The right-hand-side vector of length n.

    Returns:
        The solution vector ``x`` of length n such that ``A @ x == b``.

    Example:
        >>> solve([[4, 3], [6, 3]], [10, 12])
        [1.0, 2.0]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(solve([[4, 3], [6, 3]], [10, 12]))                       # Expected: [1.0, 2.0]
    print(solve([[1, 1, 1], [0, 2, 5], [2, 5, -1]], [6, -4, 27]))   # Expected: [5.0, 3.0, -2.0]
