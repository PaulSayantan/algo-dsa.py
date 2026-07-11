"""Range Update Range Sum (two-BIT / B1-B2 Fenwick Tree trick).

Fill in the body using TWO Binary Indexed Trees (Fenwick Trees) so that both
rangeUpdate(l, r, delta) and rangeSum(l, r) run in O(log n).
"""

from typing import List, Union


class RangeBIT:
    """Range-add, range-sum over a 1-indexed array of length n (initially 0).

    Args:
        n: Number of elements (positions 1..n).

    Example:
        >>> bit = RangeBIT(5)
        >>> bit.rangeUpdate(1, 3, 2)
        >>> bit.rangeSum(1, 5)
        6
    """

    def __init__(self, n: int) -> None:
        # TODO: implement (allocate two Fenwick Trees B1 and B2 of size n)
        pass

    def rangeUpdate(self, l: int, r: int, delta: int) -> None:
        """Add `delta` to every element in the inclusive range [l, r].

        Args:
            l: 1-based inclusive left bound.
            r: 1-based inclusive right bound (r >= l).
            delta: Amount to add to each element in the range.
        """
        # TODO: implement
        pass

    def rangeSum(self, l: int, r: int) -> int:
        """Return the sum of elements in the inclusive range [l, r].

        Args:
            l: 1-based inclusive left bound.
            r: 1-based inclusive right bound (r >= l).

        Returns:
            Sum of the current values at positions l..r.
        """
        # TODO: implement
        pass


def process(n: int, ops: List[List[Union[str, int]]]) -> List[int]:
    """Apply the operations in order and collect the rangeSum answers.

    Args:
        n: Size of the array.
        ops: Each op is ["rangeUpdate", l, r, delta] or ["rangeSum", l, r].

    Returns:
        The list of results, one per "rangeSum" operation, in order.

    Example:
        >>> process(3, [["rangeUpdate", 1, 3, 5], ["rangeSum", 1, 3]])
        [15]
    """
    # TODO: implement
    pass


if __name__ == "__main__":
    ops1 = [
        ["rangeUpdate", 1, 3, 2],
        ["rangeSum", 1, 5],
        ["rangeUpdate", 2, 5, 3],
        ["rangeSum", 2, 4],
        ["rangeSum", 1, 1],
    ]
    print(process(5, ops1))  # expected: [6, 13, 2]

    ops2 = [
        ["rangeUpdate", 1, 3, 5],
        ["rangeUpdate", 2, 2, -4],
        ["rangeSum", 1, 3],
        ["rangeSum", 2, 2],
    ]
    print(process(3, ops2))  # expected: [11, 1]
