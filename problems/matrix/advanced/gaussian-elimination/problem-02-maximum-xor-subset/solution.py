"""Maximum XOR of any subset of an integer array.

Empty solution template — fill in the logic yourself.
"""

from typing import List


def max_subset_xor(nums: List[int]) -> int:
    """Return the maximum XOR obtainable from any subset of ``nums``.

    The empty subset (XOR value 0) is always allowed, so the answer is >= 0.

    Args:
        nums: List of non-negative integers.

    Returns:
        The largest value equal to the XOR of some subset of ``nums``.

    Example:
        >>> max_subset_xor([3, 8, 1])
        11
    """
    # TODO: implement using a GF(2) linear basis (Gaussian elimination on bits),
    #       then greedily maximize from the highest bit down.
    pass


if __name__ == "__main__":
    # Example 1 -> expected 3
    print(max_subset_xor([1, 2, 3]))

    # Example 2 -> expected 11
    print(max_subset_xor([3, 8, 1]))

    # Example 3 -> expected 0
    print(max_subset_xor([0, 0]))
