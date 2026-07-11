"""Maximum Subset Value Under Weight Limit (MITM knapsack) —
empty solution template.

Fill in `max_value_under_weight` using the Meet in the Middle technique.
"""

from typing import List


def max_value_under_weight(
    weights: List[int], values: List[int], capacity: int
) -> int:
    """Maximize total value of a subset whose total weight is at most capacity.

    Args:
        weights: Positive integer weight of each of the n items (n <= 40).
        values: Non-negative integer value of each item; same length as weights.
        capacity: Maximum total weight allowed (can be as large as 10**15).

    Returns:
        The maximum achievable total value using any subset of items whose total
        weight does not exceed capacity. The empty subset (value 0) is always valid.

    Example:
        >>> max_value_under_weight([3, 4, 5, 2], [4, 5, 6, 3], 7)
        9
        >>> max_value_under_weight([5, 4, 6, 2, 3], [10, 40, 30, 50, 20], 10)
        110
    """
    # TODO: implement using Meet in the Middle
    pass


if __name__ == "__main__":
    print(max_value_under_weight([3, 4, 5, 2], [4, 5, 6, 3], 7))            # expected: 9
    print(max_value_under_weight([5, 4, 6, 2, 3], [10, 40, 30, 50, 20], 10))  # expected: 110
    print(max_value_under_weight([8, 9, 10], [100, 120, 130], 5))           # expected: 0
