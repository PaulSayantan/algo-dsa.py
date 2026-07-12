"""Count recent requests within the last 3000 ms using an array-backed queue."""
from typing import List  # noqa: F401


class RecentCounter:
    def __init__(self) -> None:
        # TODO: keep request times in a list; the oldest sits at index 0
        pass

    def ping(self, t: int) -> int:
        # TODO: enqueue t at the rear, drop times < t - 3000 from the front,
        # then return how many remain
        pass


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))  # expected: 1
    print(rc.ping(100))  # expected: 2
    print(rc.ping(3001))  # expected: 3
    print(rc.ping(3002))  # expected: 3
    print(rc.ping(7000))  # expected: 1
