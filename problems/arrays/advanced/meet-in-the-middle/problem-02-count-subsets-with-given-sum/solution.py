"""Count Subsets With Given Sum — empty solution template.

Fill in `count_subsets_with_sum` using the Meet in the Middle technique.
"""

from typing import List


def count_subsets_with_sum(nums: List[int], target: int) -> int:
    """Count the subsets (by index) of `nums` that sum to exactly `target`.

    Args:
        nums: A list of up to 40 integers (may be negative, zero, or positive).
        target: The desired subset sum.

    Returns:
        The number of distinct index-subsets whose elements sum to `target`.
        The empty subset (sum 0) is included when target == 0.

    Example:
        >>> count_subsets_with_sum([1, 2, 3], 3)
        2
        >>> count_subsets_with_sum([2, 2, 2], 4)
        3
    """
    # TODO: implement using Meet in the Middle
    pass


if __name__ == "__main__":
    print(count_subsets_with_sum([1, 2, 3], 3))      # expected: 2
    print(count_subsets_with_sum([2, 2, 2], 4))      # expected: 3
    print(count_subsets_with_sum([1, -1, 2], 0))     # expected: 2
