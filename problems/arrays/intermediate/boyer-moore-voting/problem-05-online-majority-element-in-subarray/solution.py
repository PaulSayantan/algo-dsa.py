from typing import List


class MajorityChecker:
    def __init__(self, arr: List[int]) -> None:
        """Initialize the structure over ``arr``.

        Suggested design: build a segment tree whose nodes each store the
        Boyer–Moore (candidate, count) summary of their range (the vote merges
        associatively in O(1)), and build a map from value -> sorted list of the
        indices where it occurs so a candidate's frequency in any subarray can
        be verified by binary search.

        Args:
            arr: The backing array of integers.
        """
        # TODO: implement
        pass

    def query(self, left: int, right: int, threshold: int) -> int:
        """Return the value occurring >= ``threshold`` times in arr[left..right].

        It is guaranteed that ``2 * threshold > right - left + 1``, so any
        qualifying value is the strict majority of the subarray and is unique.
        Merge segment-tree nodes over [left, right] to obtain the sole majority
        candidate, then confirm its real count in the subarray reaches
        ``threshold``; return the value if so, otherwise -1.

        Args:
            left: Inclusive left index of the subarray.
            right: Inclusive right index of the subarray.
            threshold: Minimum required occurrence count.

        Returns:
            The qualifying element, or -1 if none exists.

        Example:
            >>> mc = MajorityChecker([1, 1, 2, 2, 1, 1])
            >>> mc.query(0, 5, 4)
            1
            >>> mc.query(0, 3, 3)
            -1
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    mc = MajorityChecker([1, 1, 2, 2, 1, 1])

    print(mc.query(0, 5, 4))    # expected: 1
    print(mc.query(0, 3, 3))    # expected: -1
    print(mc.query(2, 3, 2))    # expected: 2
