"""Solve a non-singular square linear system Ax = b via Gauss-Jordan elimination.

Fill in `solve_linear_system` below. The intended technique is Gauss-Jordan
elimination with partial pivoting: build the augmented matrix [A | b], reduce the
left block to the identity (reduced row echelon form), and read the solution off
the final column.
"""

from typing import List


def solve_linear_system(A: List[List[float]], b: List[float]) -> List[float]:
    """Return the unique solution x of the system A x = b.

    Args:
        A: An n x n coefficient matrix. A is guaranteed to be non-singular.
        b: The length-n right-hand-side vector.

    Returns:
        A length-n list of floats: the solution vector x = (x0, ..., x_{n-1}).

    Example:
        >>> solve_linear_system([[2, 1], [1, 3]], [3, 4])
        [1.0, 1.0]
    """
    # TODO: implement using Gauss-Jordan elimination (partial pivoting).
    pass


if __name__ == "__main__":
    A = [[1, 1, 1],
         [0, 2, 5],
         [2, 5, -1]]
    b = [6, -4, 27]
    print(solve_linear_system(A, b))  # expected: [5.0, 3.0, -2.0]

    print(solve_linear_system([[2, 1], [1, 3]], [3, 4]))  # expected: [1.0, 1.0]
