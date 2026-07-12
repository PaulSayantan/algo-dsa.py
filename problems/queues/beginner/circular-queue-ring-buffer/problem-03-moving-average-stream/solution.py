"""Moving Average from Data Stream — LeetCode 346. Fixed window via ring buffer."""


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: fixed-size buffer, head index, live count, and a running sum
        pass

    def next(self, val: int) -> float:
        # TODO: overwrite the head slot; drop the evicted value from the sum,
        #       add val, then divide by the current live count
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0
