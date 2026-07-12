"""Number of Recent Calls — LeetCode 933 (design)."""
from collections import deque  # noqa: F401


class RecentCounter:
    def __init__(self) -> None:
        # TODO: queue of timestamps
        pass

    def ping(self, t: int) -> int:
        # TODO
        pass


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))  # expected: 1
    print(rc.ping(100))  # expected: 2
    print(rc.ping(3001))  # expected: 3
    print(rc.ping(3002))  # expected: 3
