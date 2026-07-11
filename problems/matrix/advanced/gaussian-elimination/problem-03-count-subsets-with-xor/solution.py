"""Count subsets of an array whose XOR equals a target k (mod 1e9+7).

Empty solution template — fill in the logic yourself.
"""

from typing import List

MOD = 10**9 + 7


def count_subsets_with_xor(nums: List[int], k: int) -> int:
    """Count subsets of ``nums`` (including the empty subset) with XOR == k.

    Subsets are distinguished by index set, so equal values count separately.

    Args:
        nums: List of non-negative integers.
        k: Target XOR value.

    Returns:
        The number of qualifying subsets, taken modulo 1_000_000_007.

    Example:
        >>> count_subsets_with_xor([1, 2, 3], 3)
        2
    """
    # TODO: build a GF(2) linear basis (Gaussian elimination), find its rank r,
    #       test whether k is in the span, and return 2^(n - r) mod MOD if so
    #       (else 0).
    pass


if __name__ == "__main__":
    # Example 1 -> expected 2
    print(count_subsets_with_xor([1, 2, 3], 0))

    # Example 2 -> expected 2
    print(count_subsets_with_xor([1, 2, 3], 3))

    # Example 3 -> expected 0
    print(count_subsets_with_xor([5, 5], 1))
