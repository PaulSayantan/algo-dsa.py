"""Range Assign and Range Minimum Query.

Fill in the segment-tree-with-lazy-propagation logic. The public API is fixed by
the problem statement; do not change the method signatures.
"""
from typing import List


class RangeAssignRangeMin:
    """Range-assign / range-min structure backed by a lazy segment tree.

    Example:
        st = RangeAssignRangeMin([5, 3, 8, 1, 9])
        st.assign(1, 3, 4)      # set indices 1..3 to 4
        st.minRange(0, 2)       # -> 4
    """

    def __init__(self, nums: List[int]) -> None:
        """Build the structure over the initial array.

        Args:
            nums: Initial integer values, 0-indexed.
        """
        # TODO: implement
        pass

    def assign(self, left: int, right: int, val: int) -> None:
        """Set every element with index in the inclusive range to ``val``.

        Args:
            left: Inclusive left index of the range.
            right: Inclusive right index of the range.
            val: Value to overwrite each element in the range with.
        """
        # TODO: implement
        pass

    def minRange(self, left: int, right: int) -> int:
        """Return the minimum element with index in the inclusive range.

        Args:
            left: Inclusive left index of the range.
            right: Inclusive right index of the range.

        Returns:
            The minimum of all elements in [left, right].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    st = RangeAssignRangeMin([5, 3, 8, 1, 9])
    print(st.minRange(0, 4))  # expected: 1
    st.assign(1, 3, 4)
    print(st.minRange(0, 2))  # expected: 4
    print(st.minRange(3, 4))  # expected: 4
