"""Moving Average from Data Stream — LeetCode 346 (design)."""
from collections import deque  # noqa: F401


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: fixed-size queue + running sum
        pass

    def next(self, val: int) -> float:
        # TODO
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0
