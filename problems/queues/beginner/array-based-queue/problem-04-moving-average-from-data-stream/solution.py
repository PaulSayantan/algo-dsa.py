"""Sliding-window moving average over a stream using an array-backed queue."""
from typing import List  # noqa: F401


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: remember the window size and keep the values in a list
        pass

    def next(self, val: int) -> float:
        # TODO: enqueue val at the rear; if the list exceeds size, dequeue the
        # oldest from the front (index 0); return sum(window) / len(window)
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0
    print(ma.next(9))  # expected: 5.666666666666667
