"""Moving Average from a data stream: deque as a fixed-length FIFO window."""
from collections import deque  # noqa: F401


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: store size, a deque window, and a running sum
        pass

    def next(self, val: int) -> float:
        # TODO: append val; if window exceeds size, popleft oldest; return sum / len
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0
