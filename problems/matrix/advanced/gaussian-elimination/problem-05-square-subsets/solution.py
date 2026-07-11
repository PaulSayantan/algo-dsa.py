"""Square Subsets: count non-empty subsets whose product is a perfect square.

Empty solution template — fill in the logic yourself.
"""

from typing import List

MOD = 10**9 + 7


def count_square_subsets(nums: List[int]) -> int:
    """Count non-empty subsets of ``nums`` whose product is a perfect square.

    Subsets are distinguished by index set, so equal values count separately.

    Args:
        nums: List of integers, each in [1, 70].

    Returns:
        The number of qualifying non-empty subsets, modulo 1_000_000_007.

    Example:
        >>> count_square_subsets([2, 3, 6])
        1
    """
    # TODO: map each value to its prime-parity vector over primes <= 70,
    #       build a GF(2) linear basis (Gaussian elimination) of rank r,
    #       then return (2^(n - r) - 1) mod MOD  (subtract the empty subset).
    pass


if __name__ == "__main__":
    # Example 1 -> expected 15
    print(count_square_subsets([1, 1, 1, 1]))

    # Example 2 -> expected 7
    print(count_square_subsets([2, 2, 2, 2]))

    # Example 3 -> expected 1
    print(count_square_subsets([2, 3, 6]))
