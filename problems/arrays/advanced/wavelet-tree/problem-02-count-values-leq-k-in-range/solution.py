"""Range 'count of values <= x' queries, backed by a Wavelet Tree.

Fill in the Wavelet Tree so that rangeCountLeq(l, r, x) runs in O(log sigma).
"""

from typing import List


class RangeCounter:
    """Static array supporting rangeCountLeq(l, r, x).

    Intended implementation: a Wavelet Tree over the value range. Each node
    stores pref[k] = number of the node's first k elements that go to the left
    (value <= mid) child. Routing a window [l, r) down one level is O(1).
    """

    def __init__(self, arr: List[int]) -> None:
        """Preprocess `arr` in O(n log sigma).

        Args:
            arr: The static input sequence (arbitrary integers).
        """
        # TODO: implement
        pass

    def range_count_leq(self, l: int, r: int, x: int) -> int:
        """Count elements of arr[l..r) that are <= x.

        Args:
            l: Inclusive left bound (0 <= l < r <= n).
            r: Exclusive right bound.
            x: Upper value threshold (inclusive).

        Returns:
            The number of indices p with l <= p < r and arr[p] <= x.

        Example:
            >>> rc = RangeCounter([2, 5, 1, 4, 3])
            >>> rc.range_count_leq(1, 4, 3)
            1
        """
        # TODO: implement
        pass

    def range_count_between(self, l: int, r: int, a: int, b: int) -> int:
        """Count elements of arr[l..r) whose value lies in [a, b].

        Args:
            l: Inclusive left bound.
            r: Exclusive right bound.
            a: Inclusive lower value bound.
            b: Inclusive upper value bound.

        Returns:
            Count of p in [l, r) with a <= arr[p] <= b. Should reuse
            range_count_leq: result = leq(l, r, b) - leq(l, r, a - 1).

        Example:
            >>> rc = RangeCounter([2, 5, 1, 4, 3])
            >>> rc.range_count_between(0, 5, 2, 4)
            3
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rc = RangeCounter([2, 5, 1, 4, 3])
    print(rc.range_count_leq(1, 4, 3))       # expected: 1
    print(rc.range_count_leq(0, 5, 4))       # expected: 4
    print(rc.range_count_leq(0, 2, 10))      # expected: 2
    print(rc.range_count_between(0, 5, 2, 4))  # expected: 3  ({2,4,3})
