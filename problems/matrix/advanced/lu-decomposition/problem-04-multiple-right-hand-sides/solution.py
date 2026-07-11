"""Solve many right-hand sides with a single LU factorization.

Factor A = LU once (O(n^3)), then solve each A x_j = b_j with a forward and a
back substitution (O(n^2) each), for O(n^3 + m*n^2) total.
"""

from typing import List

Matrix = List[List[float]]
Vector = List[float]


def solve_multiple(A: Matrix, B: List[Vector]) -> List[Vector]:
    """Solve ``A x_j = b_j`` for every right-hand side ``b_j`` in ``B``.

    Factor A once into unit-lower-triangular L and upper-triangular U, then
    reuse that factorization for each right-hand side via forward and back
    substitution.

    Args:
        A: An n x n non-singular matrix with non-zero pivots. Left unmodified.
        B: A list of m right-hand-side vectors, each of length n.

    Returns:
        A list of m solution vectors ``[x_1, ..., x_m]``, each of length n,
        where ``A @ x_j == b_j``.

    Example:
        >>> solve_multiple([[2, 1], [1, 3]], [[5, 10], [3, 4]])
        [[1.0, 3.0], [1.0, 1.0]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(solve_multiple([[2, 1], [1, 3]], [[5, 10], [3, 4]]))
    # Expected: [[1.0, 3.0], [1.0, 1.0]]
    print(solve_multiple([[1, 1, 1], [0, 2, 5], [2, 5, -1]], [[6, -4, 27], [3, 7, 6]]))
    # Expected: [[5.0, 3.0, -2.0], [1.0, 1.0, 1.0]]
