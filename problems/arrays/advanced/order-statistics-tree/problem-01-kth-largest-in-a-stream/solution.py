"""LeetCode 703 - Kth Largest Element in a Stream.

Solve with an Order-Statistics Tree: keep the stream as a dynamic multiset
augmented with subtree sizes, then answer each query with `select`.

This is an EMPTY TEMPLATE. Fill in the logic yourself.
"""
from typing import List, Optional


class KthLargest:
    """Streaming k-th largest via an order-statistics multiset.

    Example:
        obj = KthLargest(3, [4, 5, 8, 2])
        obj.add(3)   # -> 4
        obj.add(5)   # -> 5
    """

    def __init__(self, k: int, nums: List[int]) -> None:
        """Initialize with the rank `k` and the initial stream `nums`.

        Args:
            k: Which order statistic to report (k-th largest, 1-indexed).
            nums: Initial elements of the stream (may be empty).
        """
        # TODO: implement (build the order-statistics tree; store k)
        pass

    def add(self, val: int) -> int:
        """Insert `val` into the stream and return the current k-th largest.

        Args:
            val: The new value appended to the stream.

        Returns:
            The k-th largest element of the stream after inserting `val`.
        """
        # TODO: implement (insert val, then select the (size - k + 1)-th smallest)
        pass


if __name__ == "__main__":
    kth = KthLargest(3, [4, 5, 8, 2])
    print(kth.add(3))   # expected 4
    print(kth.add(5))   # expected 5
    print(kth.add(10))  # expected 5
    print(kth.add(9))   # expected 8
    print(kth.add(4))   # expected 8
