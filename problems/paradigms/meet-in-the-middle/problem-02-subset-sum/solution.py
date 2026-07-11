"""Count subsets with a given sum, n up to 40.

Return how many subsets (by index set, empty subset allowed) of `nums` sum to
exactly `target`.

Fill in `count_subsets_with_sum` using Meet in the Middle: split `nums` into
two halves, enumerate every subset sum of each half, then combine the two
multisets of sums so that a left sum plus a right sum equals `target`.
"""

from typing import List


def count_subsets_with_sum(nums: List[int], target: int) -> int:
    """Count subsets of `nums` whose elements sum to `target`.

    Args:
        nums: List of up to 40 integers (may be negative or large).
        target: The exact subset sum to count.

    Returns:
        The number of index-distinct subsets (including the empty subset when
        target == 0) whose elements sum to `target`.

    Example:
        >>> count_subsets_with_sum([1, 2, 3], 3)
        2
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    # Expected: 2  -> {3}, {1, 2}
    print(count_subsets_with_sum([1, 2, 3], 3))
    # Expected: 3  -> any two of the three 2's
    print(count_subsets_with_sum([2, 2, 2], 4))
    # Expected: 2  -> {}, {1, -1}
    print(count_subsets_with_sum([1, -1, 2], 0))
