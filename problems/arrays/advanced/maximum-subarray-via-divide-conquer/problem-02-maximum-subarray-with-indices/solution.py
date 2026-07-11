"""Maximum Subarray With Indices (CLRS FIND-MAXIMUM-SUBARRAY) — template.

Return the boundaries AND the sum of the best contiguous subarray, using divide
& conquer. The combine step must track indices, not just the crossing sum.
"""
from typing import List, Tuple


def find_maximum_subarray(nums: List[int]) -> Tuple[int, int, int]:
    """Find the maximum-sum contiguous subarray and its boundaries.

    Args:
        nums: A non-empty list of integers (values may be negative).

    Returns:
        A tuple ``(start, end, total)`` where ``start`` and ``end`` are 0-based
        inclusive indices of the best subarray and ``total`` is its sum. On ties,
        prefer the left-only candidate, then the crossing, then the right-only.

    Example:
        >>> find_maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        (3, 6, 6)
    """
    # TODO: implement using Maximum Subarray via Divide & Conquer
    pass


if __name__ == "__main__":
    print(find_maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expected: (3, 6, 6)
    print(find_maximum_subarray([2, -1, 2]))                        # expected: (0, 2, 3)
    print(find_maximum_subarray([-5, -2, -3]))                      # expected: (1, 1, -2)
