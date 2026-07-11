"""LeetCode 901 - Online Stock Span.

Stream daily prices and report, for each, the number of consecutive preceding
days (including today) with price <= today's price. A monotonic stack makes each
call O(1) amortized.
"""


class StockSpanner:
    """Compute stock price spans online using a monotonic stack.

    Example:
        >>> ss = StockSpanner()
        >>> [ss.next(p) for p in [100, 80, 60, 70, 60, 75, 85]]
        [1, 1, 1, 2, 1, 4, 6]
    """

    def __init__(self) -> None:
        """Initialize the spanner's internal state."""
        # TODO: implement (e.g. a stack of (price, span) pairs)
        pass

    def next(self, price: int) -> int:
        """Record today's price and return its span.

        Args:
            price: Today's stock price.

        Returns:
            The number of consecutive days up to and including today for which the
            price was less than or equal to ``price``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    ss = StockSpanner()
    print([ss.next(p) for p in [100, 80, 60, 70, 60, 75, 85]])
    # expected: [1, 1, 1, 2, 1, 4, 6]

    ss2 = StockSpanner()
    print([ss2.next(p) for p in [31, 41, 48]])
    # expected: [1, 2, 3]
