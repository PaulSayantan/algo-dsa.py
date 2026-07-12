"""Online Stock Span — LeetCode 901 (monotonic stack, design)."""
from typing import List, Tuple


class StockSpanner:
    def __init__(self) -> None:
        # TODO: stack of (price, span) pairs
        pass

    def next(self, price: int) -> int:
        # TODO: pop entries with price <= current, summing their spans
        pass


if __name__ == "__main__":
    ss = StockSpanner()
    print(ss.next(100))  # expected: 1
    print(ss.next(80))  # expected: 1
    print(ss.next(60))  # expected: 1
    print(ss.next(70))  # expected: 2
    print(ss.next(60))  # expected: 1
    print(ss.next(75))  # expected: 4
    print(ss.next(85))  # expected: 6
