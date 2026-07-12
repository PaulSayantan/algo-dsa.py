"""Design Hit Counter — LeetCode 362 (design, sliding 300s window)."""
from collections import deque  # noqa: F401


class HitCounter:
    def __init__(self) -> None:
        # TODO: queue of hit timestamps
        pass

    def hit(self, timestamp: int) -> None:
        # TODO: enqueue the timestamp
        pass

    def getHits(self, timestamp: int) -> int:
        # TODO: dequeue fronts with time <= timestamp - 300, return size
        pass


if __name__ == "__main__":
    hc = HitCounter()
    hc.hit(1)
    hc.hit(100)
    print(hc.getHits(150))  # expected: 2
    hc.hit(200)
    hc.hit(300)
    print(hc.getHits(300))  # expected: 4
    print(hc.getHits(301))  # expected: 3
    print(hc.getHits(500))  # expected: 1
    print(hc.getHits(601))  # expected: 0
