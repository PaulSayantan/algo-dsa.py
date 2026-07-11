"""Online Stock Span — LeetCode 901.

Empty solution template. Fill in the body yourself.
"""


class StockSpanner:
    """Streaming calculator for the daily stock-price span.

    The span for the current day is the count of consecutive days ending today
    (walking backwards) whose price was less than or equal to today's price.

    Example:
        >>> spanner = StockSpanner()
        >>> [spanner.next(p) for p in [100, 80, 60, 70, 60, 75, 85]]
        [1, 1, 1, 2, 1, 4, 6]
    """

    def __init__(self) -> None:
        """Initialize any internal state needed to track prices."""
        # TODO: implement
        pass

    def next(self, price: int) -> int:
        """Record today's price and return its span.

        Args:
            price: Today's stock price.

        Returns:
            The span: the number of consecutive days ending today (inclusive)
            whose price was <= ``price``.
        """
        # TODO: implement
        pass


if __name__ == "__main__":
    spanner = StockSpanner()
    results = [spanner.next(p) for p in [100, 80, 60, 70, 60, 75, 85]]
    print(results)  # expected: [1, 1, 1, 2, 1, 4, 6]
