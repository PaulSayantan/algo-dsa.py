"""Range Updates and Sums (CSES 1735).

Fill in the segment-tree-with-lazy-propagation logic. Two lazy tags coexist here:
a pending assignment and a pending add. Keep the method signatures unchanged.
"""
from typing import List


class RangeUpdatesAndSums:
    """Range-add + range-assign + range-sum via a lazy segment tree.

    Example:
        st = RangeUpdatesAndSums([1, 2, 3, 4, 5])
        st.assign(0, 2, 4)
        st.sum(0, 4)          # -> 21
        st.add(1, 3, 2)
        st.sum(0, 4)          # -> 27
    """

    def __init__(self, nums: List[int]) -> None:
        """Build the structure over the initial array.

        Args:
            nums: Initial integer values, 0-indexed.
        """
        # TODO: implement
        pass

    def add(self, left: int, right: int, x: int) -> None:
        """Increase every element with index in [left, right] by ``x``.

        Args:
            left: Inclusive left index.
            right: Inclusive right index.
            x: Amount to add to each element in the range.
        """
        # TODO: implement
        pass

    def assign(self, left: int, right: int, x: int) -> None:
        """Set every element with index in [left, right] to ``x``.

        Args:
            left: Inclusive left index.
            right: Inclusive right index.
            x: Value to overwrite each element in the range with.
        """
        # TODO: implement
        pass

    def sum(self, left: int, right: int) -> int:
        """Return the sum of elements with index in [left, right].

        Args:
            left: Inclusive left index.
            right: Inclusive right index.

        Returns:
            The sum of all elements in [left, right].
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    st = RangeUpdatesAndSums([1, 2, 3, 4, 5])
    st.assign(0, 2, 4)
    print(st.sum(0, 4))   # expected: 21
    st.add(1, 3, 2)
    print(st.sum(0, 4))   # expected: 27

    st2 = RangeUpdatesAndSums([5, 5, 5])
    st2.add(0, 2, 3)
    st2.assign(1, 2, 0)
    print(st2.sum(0, 2))  # expected: 8
    print(st2.sum(1, 1))  # expected: 0
