"""Range Count of Elements Not Exceeding K (with Point Updates).

Empty solution template. Fill in the body yourself using Square Root
Decomposition where each block keeps a sorted copy of its elements.
"""

from typing import List


class RangeCountLE:
    def __init__(self, nums: List[int]) -> None:
        """Initialize the structure over ``nums``.

        Args:
            nums: The initial integer array.

        Example:
            >>> rc = RangeCountLE([2, 1, 5, 3, 4, 6])
            >>> rc.query(0, 5, 3)
            3
        """
        # TODO: implement — block size ~ sqrt(n) plus a sorted copy per block
        pass

    def update(self, index: int, val: int) -> None:
        """Set ``nums[index] = val`` and repair the block's sorted copy.

        Args:
            index: The position to overwrite (0-indexed).
            val: The new value stored at ``index``.

        Returns:
            None. Mutates internal state in place.
        """
        # TODO: implement — remove old value, insert new value in one block
        pass

    def query(self, left: int, right: int, k: int) -> int:
        """Count elements in ``[left, right]`` whose value is ``<= k``.

        Args:
            left: Left endpoint of the range (0-indexed, inclusive).
            right: Right endpoint of the range (0-indexed, inclusive).
            k: The inclusive upper bound to count against.

        Returns:
            The number of in-range elements with value ``<= k``.
        """
        # TODO: implement — scan partial ends, binary-search whole blocks
        pass


if __name__ == "__main__":
    rc = RangeCountLE([2, 1, 5, 3, 4, 6])
    print(rc.query(0, 5, 3))  # expected: 3
    rc.update(2, 0)
    print(rc.query(0, 5, 3))  # expected: 4
    print(rc.query(1, 4, 3))  # expected: 3

    rc2 = RangeCountLE([10, 20, 30, 40, 50])
    print(rc2.query(0, 4, 25))  # expected: 2
    print(rc2.query(2, 4, 50))  # expected: 3
    rc2.update(0, 100)
    print(rc2.query(0, 2, 50))  # expected: 2
