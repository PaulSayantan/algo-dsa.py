"""Matrix Chain Multiplication (CLRS Chapter 15 classic).

Fill in the body of `matrix_chain_order` using Range / Interval DP.
"""

from typing import List


def matrix_chain_order(dims: List[int]) -> int:
    """Return the minimum number of scalar multiplications for the chain.

    The chain has ``len(dims) - 1`` matrices, where matrix i (1-indexed) has
    dimensions ``dims[i-1] x dims[i]``.

    Args:
        dims: Dimension array of length n + 1 (n = number of matrices).

    Returns:
        The minimum total scalar multiplications over all parenthesizations.
        If there are 0 or 1 matrices, no multiplication is needed, so return 0.

    Example:
        >>> matrix_chain_order([40, 20, 30, 10, 30])
        26000
    """
    # TODO: implement using interval DP over dp[i][j] for sub-chain A[i..j]
    pass


if __name__ == "__main__":
    print(matrix_chain_order([40, 20, 30, 10, 30]))  # expected: 26000
    print(matrix_chain_order([10, 20, 30]))          # expected: 6000
    print(matrix_chain_order([10, 30, 5, 60]))       # expected: 4500
