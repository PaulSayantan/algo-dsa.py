"""Solve a linear system A x = b over the finite field GF(p) (p prime).

Fill in `solve_mod_p` below. The intended technique is Gauss-Jordan elimination
done entirely in modular arithmetic: normalise each pivot row by multiplying by the
pivot's modular inverse (pow(pivot, p - 2, p)), reduce to RREF, detect
inconsistency, and count solutions from the number of free variables.
"""

from typing import List, Tuple, Union

Result = Union[str, Tuple[int, List[int]]]


def solve_mod_p(A: List[List[int]], b: List[int], p: int) -> Result:
    """Solve A x = b (mod p) over GF(p) and count the solutions.

    Args:
        A: An m x n coefficient matrix with entries in [0, p).
        b: The length-m right-hand-side vector with entries in [0, p).
        p: A prime modulus.

    Returns:
        "NO SOLUTION" if the system is inconsistent mod p, otherwise a tuple
        (count, x) where x is one particular solution (length-n, each in [0, p))
        and count is the number of solutions in GF(p)^n: p^(free variables), given
        modulo 1_000_000_007 when it would overflow a 64-bit integer.

    Example:
        >>> solve_mod_p([[2, 3], [1, 2]], [1, 2], 7)
        (1, [3, 3])
        >>> solve_mod_p([[1, 1, 1]], [0], 3)
        (9, [0, 0, 0])
    """
    # TODO: implement using Gauss-Jordan elimination over GF(p).
    pass


if __name__ == "__main__":
    print(solve_mod_p([[2, 3], [1, 2]], [1, 2], 7))    # expected: (1, [3, 3])
    print(solve_mod_p([[1, 1, 1]], [0], 3))            # expected: (9, [0, 0, 0])
    print(solve_mod_p([[1, 1], [2, 3]], [3, 4], 5))    # expected: (1, [0, 3])
