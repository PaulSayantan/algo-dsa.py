"""Sliding-window moving average backed by a linked-list queue + running sum."""


class _Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: window capacity, head/tail pointers, a count, and a running sum
        pass

    def next(self, val: int) -> float:
        # TODO: enqueue val (add to sum); if count exceeds size, dequeue head
        # (subtract from sum); return sum / count
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0
    ma1 = MovingAverage(1)
    print(ma1.next(4))  # expected: 4.0
    print(ma1.next(8))  # expected: 8.0
    ma2 = MovingAverage(2)
    print(ma2.next(2))  # expected: 2.0
    print(ma2.next(6))  # expected: 4.0
    print(ma2.next(10))  # expected: 8.0
