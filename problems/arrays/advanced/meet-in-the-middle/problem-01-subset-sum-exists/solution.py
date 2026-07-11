"""Subset Sum Exists — empty solution template.

Fill in `subset_sum_exists` using the Meet in the Middle technique.
"""

from typing import List


def subset_sum_exists(nums: List[int], target: int) -> bool:
    """Return True iff some subset of `nums` sums to exactly `target`.

    Args:
        nums: A list of up to 40 integers (may be negative, zero, or positive).
        target: The desired subset sum.

    Returns:
        True if any subset (including the empty subset, which sums to 0) totals
        exactly `target`; False otherwise.

    Example:
        >>> subset_sum_exists([3, 34, 4, 12, 5, 2], 9)
        True
        >>> subset_sum_exists([3, 34, 4, 12, 5, 2], 30)
        False
    """
    # TODO: implement using Meet in the Middle
    pass


if __name__ == "__main__":
    print(subset_sum_exists([3, 34, 4, 12, 5, 2], 9))     # expected: True
    print(subset_sum_exists([3, 34, 4, 12, 5, 2], 30))    # expected: False
    print(subset_sum_exists([-7, 2, 5, 12], -5))          # expected: True
