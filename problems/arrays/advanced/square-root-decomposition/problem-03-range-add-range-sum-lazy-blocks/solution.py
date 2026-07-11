"""Range Add & Range Sum (Lazy Blocks).

Empty solution template. Fill in the body yourself using Square Root
Decomposition with a per-block lazy add.
"""

from typing import List


class RangeAddSum:
    def __init__(self, nums: List[int]) -> None:
        """Initialize the structure over ``nums``.

        Args:
            nums: The initial integer array.

        Example:
            >>> ras = RangeAddSum([1, 2, 3, 4, 5])
            >>> ras.range_sum(0, 4)
            15
        """
        # TODO: implement — block size ~ sqrt(n), per-block sums, per-block lazy
        pass

    def range_add(self, left: int, right: int, delta: int) -> None:
        """Add ``delta`` to every element in ``[left, right]`` (inclusive).

        Args:
            left: Left endpoint of the range (0-indexed, inclusive).
            right: Right endpoint of the range (0-indexed, inclusive).
            delta: Amount to add to each element in the range.

        Returns:
            None. Mutates internal state in place.
        """
        # TODO: implement — whole blocks get lazy delta; partial ends elementwise
        pass

    def range_sum(self, left: int, right: int) -> int:
        """Return the inclusive sum over ``[left, right]``.

        Args:
            left: Left endpoint of the range (0-indexed, inclusive).
            right: Right endpoint of the range (0-indexed, inclusive).

        Returns:
            The sum of the range, accounting for any pending lazy adds.
        """
        # TODO: implement — include element values, block sums, and lazy adds
        pass


if __name__ == "__main__":
    ras = RangeAddSum([1, 2, 3, 4, 5])
    print(ras.range_sum(0, 4))  # expected: 15
    ras.range_add(1, 3, 10)
    print(ras.range_sum(0, 4))  # expected: 45
    print(ras.range_sum(2, 2))  # expected: 13

    ras2 = RangeAddSum([0, 0, 0, 0])
    ras2.range_add(0, 2, 5)
    print(ras2.range_sum(0, 3))  # expected: 15
    ras2.range_add(1, 3, 2)
    print(ras2.range_sum(1, 2))  # expected: 14
