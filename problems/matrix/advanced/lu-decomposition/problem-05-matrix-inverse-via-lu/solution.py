"""Matrix inverse via LU Decomposition.

Compute A^{-1} by factoring A = LU once, then solving A x_j = e_j for each
identity column e_j and assembling the results as the columns of the inverse.
"""

from typing import List

Matrix = List[List[float]]


def inverse(A: Matrix) -> Matrix:
    """Return the inverse of a non-singular square matrix using LU decomposition.

    Factor A = LU once, then solve A x_j = e_j (the j-th identity column) for
    each j via forward and back substitution; the solutions are the columns of
    A^{-1}.

    Args:
        A: An n x n non-singular matrix with non-zero pivots. Left unmodified.

    Returns:
        The n x n inverse matrix ``A_inv`` such that ``A @ A_inv == I``.

    Example:
        >>> inverse([[1, 2], [3, 4]])
        [[-2.0, 1.0], [1.5, -0.5]]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(inverse([[1, 2], [3, 4]]))
    # Expected: [[-2.0, 1.0], [1.5, -0.5]]
    print(inverse([[1, 2, 3], [0, 1, 4], [5, 6, 0]]))
    # Expected: [[-24.0, 18.0, 5.0], [20.0, -15.0, -4.0], [-5.0, 4.0, 1.0]]
