"""Range Add and Range Sum Query.

Fill in the segment-tree-with-lazy-propagation logic. The public API is fixed by
the problem statement; do not change the method signatures.
"""
from typing import List


class RangeAddRangeSum:
    """Range-add / range-sum structure backed by a lazy segment tree.

    Example:
        st = RangeAddRangeSum([1, 2, 3, 4, 5])
        st.update(1, 3, 2)     # add 2 to indices 1..3
        st.sumRange(0, 2)      # -> 10
    """

    def __init__(self, nums: List[int]) -> None:
        """Build the structure over the initial array.

        Args:
            nums: Initial integer values, 0-indexed.
        """
        # TODO: implement
        pass

    def update(self, left: int, right: int, val: int) -> None:
        """Add ``val`` to every element with index in the inclusive range.

        Args:
            left: Inclusive left index of the range.
            right: Inclusive right index of the range.
            val: Amount to add to each element in the range.
        """
        # TODO: implement
        pass

    def sumRange(self, left: int, right: int) -> int:
        """Return the sum of elements with index in the inclusive range.

        Args:
            left: Inclusive left index of the range.
            right: Inclusive right index of the range.

        Returns:
            The sum of all elements in [left, right].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    st = RangeAddRangeSum([1, 2, 3, 4, 5])
    st.update(1, 3, 2)
    print(st.sumRange(0, 2))  # expected: 10
    st.update(0, 4, 1)
    print(st.sumRange(2, 4))  # expected: 19
