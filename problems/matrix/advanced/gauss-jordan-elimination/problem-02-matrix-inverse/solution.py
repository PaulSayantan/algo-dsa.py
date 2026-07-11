"""Invert an n x n matrix via Gauss-Jordan elimination, or report singularity.

Fill in `invert_matrix` below. The intended technique is Gauss-Jordan
elimination on the augmented block [A | I]: reduce the left block to the identity
and the right block becomes A^{-1}. If a pivot column has no usable pivot, A is
singular and you should return None.
"""

from typing import List, Optional


def invert_matrix(A: List[List[float]]) -> Optional[List[List[float]]]:
    """Return the inverse of A, or None if A is singular.

    Args:
        A: An n x n matrix.

    Returns:
        The n x n inverse matrix A^{-1} as a list of lists of floats, or None if
        A is not invertible (determinant zero / a pivot cannot be found).

    Example:
        >>> invert_matrix([[4, 7], [2, 6]])
        [[0.6, -0.7], [-0.2, 0.4]]
        >>> invert_matrix([[1, 2], [2, 4]]) is None
        True
    """
    # TODO: implement using Gauss-Jordan elimination on [A | I].
    pass


if __name__ == "__main__":
    print(invert_matrix([[4, 7], [2, 6]]))      # expected: [[0.6, -0.7], [-0.2, 0.4]]
    print(invert_matrix([[1, 2], [2, 4]]))      # expected: None (singular)
    print(invert_matrix([[1, 2, 3],
                         [0, 1, 4],
                         [5, 6, 0]]))
    # expected: [[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]
