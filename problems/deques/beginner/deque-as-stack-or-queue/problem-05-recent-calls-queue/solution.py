"""Number of Recent Calls: deque as a FIFO queue over a sliding time window."""
from collections import deque  # noqa: F401


class RecentCounter:
    def __init__(self) -> None:
        # TODO: hold request times in a deque used as a FIFO queue
        pass

    def ping(self, t: int) -> int:
        # TODO: append t; popleft while front < t - 3000; return len(deque)
        pass


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))  # expected: 1
    print(rc.ping(100))  # expected: 2
    print(rc.ping(3001))  # expected: 3
    print(rc.ping(3002))  # expected: 3
