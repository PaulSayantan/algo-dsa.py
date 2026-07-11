"""Range k-th smallest (order statistic) queries, backed by a Wavelet Tree.

Fill in the Wavelet Tree so that kthSmallest(l, r, k) runs in O(log sigma).
"""

from typing import List


class RangeKthSmallest:
    """Static array supporting kthSmallest(l, r, k).

    Intended implementation: a Wavelet Tree over the value range. At each node,
    pref[k] counts how many of the node's first k elements go left (value <= mid).
    A window [l, r) maps to the left child as [pref[l], pref[r]) and to the right
    child as [l - pref[l], r - pref[r]).
    """

    def __init__(self, arr: List[int]) -> None:
        """Preprocess `arr` in O(n log sigma).

        Args:
            arr: The static input sequence (arbitrary integers).
        """
        # TODO: implement
        pass

    def kth_smallest(self, l: int, r: int, k: int) -> int:
        """Return the k-th smallest value (1-based) in arr[l..r).

        Args:
            l: Inclusive left bound (0 <= l < r <= n).
            r: Exclusive right bound.
            k: 1-based rank; 1 <= k <= r - l.

        Returns:
            The value that would sit at position k of the sorted subarray.

        Example:
            >>> rk = RangeKthSmallest([1, 5, 2, 6, 3, 7, 4])
            >>> rk.kth_smallest(1, 5, 3)
            5
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    rk = RangeKthSmallest([1, 5, 2, 6, 3, 7, 4])
    print(rk.kth_smallest(1, 5, 3))  # expected: 5
    print(rk.kth_smallest(0, 7, 2))  # expected: 2
    print(rk.kth_smallest(2, 3, 1))  # expected: 2
