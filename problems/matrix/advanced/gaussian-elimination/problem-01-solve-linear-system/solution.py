"""Solve a system of n linear equations in n unknowns.

Empty solution template — fill in the logic yourself.
"""

from typing import List


def solve_linear_system(A: List[List[float]], b: List[float]) -> List[float]:
    """Solve A x = b for x, where A is a non-singular n x n matrix.

    Args:
        A: Coefficient matrix of size n x n (row-major). A[i][j] is the
            coefficient of unknown x_j in equation i.
        b: Right-hand-side vector of length n.

    Returns:
        The solution vector x of length n as floats. Values within 1e-6 of the
        true solution are accepted.

    Example:
        >>> solve_linear_system([[2, 1], [1, -1]], [5, 1])
        [2.0, 1.0]
    """
    # TODO: implement using Gaussian elimination with partial pivoting,
    #       then back-substitution.
    pass


if __name__ == "__main__":
    # Example 1 -> expected [2.0, 1.0]
    print(solve_linear_system([[2, 1], [1, -1]], [5, 1]))

    # Example 2 -> expected [1.0, 2.0, 3.0]
    print(solve_linear_system([[1, 1, 1], [2, 1, 1], [1, 3, 2]], [6, 7, 13]))
