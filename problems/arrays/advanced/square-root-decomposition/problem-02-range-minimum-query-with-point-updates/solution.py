"""Range Minimum Query with Point Updates.

Empty solution template. Fill in the body yourself using Square Root
Decomposition (per-block minima).
"""

from typing import List


class RangeMinQuery:
    def __init__(self, nums: List[int]) -> None:
        """Initialize the structure over ``nums``.

        Args:
            nums: The initial integer array.

        Example:
            >>> rmq = RangeMinQuery([1, 3, 2, 7, 9, 11])
            >>> rmq.query(1, 5)
            2
        """
        # TODO: implement — block size ~ sqrt(n) and per-block minima
        pass

    def update(self, index: int, val: int) -> None:
        """Set ``nums[index] = val`` and refresh the affected block minimum.

        Args:
            index: The position to overwrite (0-indexed).
            val: The new value stored at ``index``.

        Returns:
            None. Mutates internal state in place.
        """
        # TODO: implement — recompute (or maintain) the containing block's min
        pass

    def query(self, left: int, right: int) -> int:
        """Return the minimum of ``nums[left .. right]`` (inclusive).

        Args:
            left: Left endpoint of the range (0-indexed, inclusive).
            right: Right endpoint of the range (0-indexed, inclusive).

        Returns:
            The minimum value on the range ``[left, right]``.
        """
        # TODO: implement — combine partial ends with whole-block minima
        pass


if __name__ == "__main__":
    rmq = RangeMinQuery([1, 3, 2, 7, 9, 11])
    print(rmq.query(1, 5))  # expected: 2
    rmq.update(2, 10)
    print(rmq.query(1, 5))  # expected: 3

    rmq2 = RangeMinQuery([5, 2, 8, 1, 9])
    print(rmq2.query(0, 4))  # expected: 1
    print(rmq2.query(0, 1))  # expected: 2
    rmq2.update(3, 100)
    print(rmq2.query(2, 4))  # expected: 8
