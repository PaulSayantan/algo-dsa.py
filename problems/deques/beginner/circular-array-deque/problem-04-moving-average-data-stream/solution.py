"""Moving Average from Data Stream — LeetCode 346.

Return the moving average of the last ``size`` values of a stream. Back the
window with a fixed-capacity ring buffer plus a running sum, so each ``next``
call is O(1) rather than rescanning the window.
"""
from typing import List  # noqa: F401


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: ring buffer of length size, a head index, a count, a running sum
        pass

    def next(self, val: int) -> float:
        # TODO: overwrite the oldest slot when full, adjusting the running sum
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0

    ma1 = MovingAverage(1)
    print(ma1.next(4))  # expected: 4.0
    print(ma1.next(9))  # expected: 9.0
