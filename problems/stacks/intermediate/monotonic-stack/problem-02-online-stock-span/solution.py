"""Online Stock Span — LeetCode 901 (design)."""


class StockSpanner:
    def __init__(self) -> None:
        # TODO: stack of (price, span)
        pass

    def next(self, price: int) -> int:
        # TODO
        pass


if __name__ == "__main__":
    sp = StockSpanner()
    print(sp.next(100))  # expected: 1
    print(sp.next(80))  # expected: 1
    print(sp.next(60))  # expected: 1
    print(sp.next(70))  # expected: 2
    print(sp.next(60))  # expected: 1
    print(sp.next(75))  # expected: 4
    print(sp.next(85))  # expected: 6
