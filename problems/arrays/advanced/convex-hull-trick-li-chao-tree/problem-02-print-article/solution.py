"""Print Article (HDU 3507).

Partition an array into consecutive batches minimizing sum of (batch_sum)^2 + M.
Solve with the monotonic Convex Hull Trick.
This is an EMPTY TEMPLATE: fill in the body yourself.
"""
from typing import List


def min_print_cost(cost: List[int], m: int) -> int:
    """Return the minimum total printing cost.

    The words must be printed in order, grouped into consecutive batches. A batch
    whose word costs sum to s costs s**2 + m. Minimize the total over all consecutive
    partitions of the whole list.

    Args:
        cost: Non-negative per-word costs, length N (1 <= N <= 5e5).
        m: Non-negative per-batch penalty (0 <= m <= 1000).

    Returns:
        The minimum total cost to print all N words.

    Example:
        >>> min_print_cost([5, 9, 5, 7, 5], 5)
        230
    """
    # TODO: implement using the Convex Hull Trick / Li Chao Tree
    pass


if __name__ == "__main__":
    # Expected output: 230
    print(min_print_cost([5, 9, 5, 7, 5], 5))
    # Expected output: 600
    print(min_print_cost([10, 10, 10], 100))
    # Expected output: 133
    print(min_print_cost([3, 1, 4, 1, 5, 9], 0))
