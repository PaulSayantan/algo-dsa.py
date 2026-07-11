"""Classify a general linear system A x = b as unique / infinite / no solution.

Fill in `classify_system` below. The intended technique is Gauss-Jordan
elimination: reduce [A | b] to reduced row echelon form, count pivots to get the
rank, detect an inconsistent "0 = c" row, and compare the rank to the number of
unknowns.
"""

from typing import List, Tuple, Union

Result = Union[str, Tuple[str, List[float]]]


def classify_system(A: List[List[float]], b: List[float]) -> Result:
    """Classify and (when unique) solve the linear system A x = b.

    Args:
        A: An m x n coefficient matrix (not necessarily square).
        b: The length-m right-hand-side vector.

    Returns:
        - "NO SOLUTION"          if the system is inconsistent, or
        - "INFINITE"             if it has infinitely many solutions, or
        - ("UNIQUE", x)          where x is the length-n solution vector, if the
                                 solution is unique.

    Example:
        >>> classify_system([[1, 1], [1, -1]], [3, 1])
        ('UNIQUE', [2.0, 1.0])
        >>> classify_system([[1, 2], [2, 4]], [3, 6])
        'INFINITE'
        >>> classify_system([[1, 2], [2, 4]], [3, 7])
        'NO SOLUTION'
    """
    # TODO: implement using Gauss-Jordan elimination on [A | b] + rank analysis.
    pass


if __name__ == "__main__":
    print(classify_system([[1, 1], [1, -1]], [3, 1]))   # ('UNIQUE', [2.0, 1.0])
    print(classify_system([[1, 2], [2, 4]], [3, 6]))     # 'INFINITE'
    print(classify_system([[1, 2], [2, 4]], [3, 7]))     # 'NO SOLUTION'
