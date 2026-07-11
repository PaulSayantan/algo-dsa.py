"""Find Rotation Count in a Rotated Sorted Array.

Fill in `count_rotations` using the Search in Rotated Sorted Array technique.
"""
from typing import List


def count_rotations(nums: List[int]) -> int:
    """Return how many times an ascending array of distinct ints was rotated.

    The rotation count equals the index of the minimum element.

    Args:
        nums: An ascending array of distinct integers rotated k times
            (0 <= k < len(nums)).

    Returns:
        The number of rotations k (equivalently, the index of the minimum).

    Example:
        >>> count_rotations([15, 18, 2, 3, 6, 12])
        2
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    print(count_rotations([15, 18, 2, 3, 6, 12]))  # expected: 2
    print(count_rotations([7, 9, 11, 12, 5]))       # expected: 4
    print(count_rotations([1, 2, 3, 4]))            # expected: 0
