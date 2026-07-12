"""Design Hit Counter — LeetCode 362 (design, two-stack FIFO window)."""


class HitCounter:
    def __init__(self) -> None:
        # TODO: keep hit timestamps in a two-stack FIFO queue
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
    hc.hit(2)
    hc.hit(3)
    print(hc.getHits(4))  # expected: 3
    hc.hit(300)
    print(hc.getHits(300))  # expected: 4
    print(hc.getHits(301))  # expected: 3
    hc.hit(301)
    print(hc.getHits(600))  # expected: 1
    print(hc.getHits(601))  # expected: 0
