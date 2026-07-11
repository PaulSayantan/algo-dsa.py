"""Range Minimum Query - Mutable (classic RMQ).

Support point updates and range-minimum queries, both in O(log n), with a
Segment Tree whose nodes store the minimum of their range.

Fill in the method bodies. Do NOT rescan the range on every query.
"""
from typing import List


class RangeMin:
    """Segment-tree backed mutable range-minimum structure.

    Example:
        rm = RangeMin([2, 5, 1, 4, 9, 3])
        rm.query(1, 3)   # -> 1
        rm.update(4, -2)
        rm.query(3, 5)   # -> -2
    """

    def __init__(self, arr: List[int]) -> None:
        """Build the segment tree over `arr`.

        Args:
            arr: The initial integer array.
        """
        # TODO: implement
        pass

    def update(self, index: int, val: int) -> None:
        """Set arr[index] = val and repair affected node minima.

        Args:
            index: 0-based position to overwrite.
            val: New value to store at `index`.
        """
        # TODO: implement
        pass

    def query(self, left: int, right: int) -> int:
        """Return the minimum of arr[left..right] inclusive.

        Args:
            left: Inclusive left index of the query range.
            right: Inclusive right index of the query range.

        Returns:
            The smallest element in [left, right].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rm = RangeMin([2, 5, 1, 4, 9, 3])
    print(rm.query(1, 3))  # expected: 1
    rm.update(4, -2)
    print(rm.query(3, 5))  # expected: -2
