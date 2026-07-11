"""Rank & Select over a static sequence, backed by a Wavelet Tree.

Fill in the Wavelet Tree so that `rank` and `select` run in O(log sigma) per
query, where sigma is the size of the (compressed) value alphabet.
"""

from typing import List


class WaveletSequence:
    """A static sequence supporting rank(c, i) and select(c, j).

    The intended implementation is a Wavelet Tree: recursively split the value
    range [lo, hi] at mid = (lo + hi) // 2, and at each node keep a prefix-sum
    array telling how many of the first k elements at that node fall into the
    left (value <= mid) child.
    """

    def __init__(self, arr: List[int]) -> None:
        """Preprocess `arr` in O(n log sigma).

        Args:
            arr: The static input sequence. Values may be arbitrary integers;
                you may coordinate-compress them internally, but rank/select
                arguments `c` refer to the ORIGINAL values.
        """
        # TODO: implement
        pass

    def rank(self, c: int, i: int) -> int:
        """Count occurrences of value `c` in the prefix arr[0..i).

        Args:
            c: The value to count.
            i: Exclusive right bound of the prefix, 0 <= i <= n.

        Returns:
            The number of indices p with 0 <= p < i and arr[p] == c.

        Example:
            >>> ws = WaveletSequence([4, 2, 4, 1, 4, 3, 2])
            >>> ws.rank(4, 5)
            3
        """
        # TODO: implement
        pass

    def select(self, c: int, j: int) -> int:
        """Return the 0-based index of the j-th (1-based) occurrence of `c`.

        Args:
            c: The value whose occurrence we want.
            j: 1-based occurrence number (j >= 1).

        Returns:
            The index of the j-th occurrence of `c`, or -1 if there are fewer
            than j occurrences.

        Example:
            >>> ws = WaveletSequence([4, 2, 4, 1, 4, 3, 2])
            >>> ws.select(4, 3)
            4
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    ws = WaveletSequence([4, 2, 4, 1, 4, 3, 2])
    print(ws.rank(4, 5))     # expected: 3
    print(ws.select(4, 3))   # expected: 4
    print(ws.select(2, 2))   # expected: 6
    print(ws.select(5, 1))   # expected: -1  (value 5 not present)
