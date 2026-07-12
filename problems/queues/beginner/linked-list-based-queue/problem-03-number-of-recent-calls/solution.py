"""Count recent requests in a 3000ms window using a linked-list queue."""


class _Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class RecentCounter:
    def __init__(self) -> None:
        # TODO: head pointer, tail pointer, and a size counter
        pass

    def ping(self, t: int) -> int:
        # TODO: enqueue t at the tail, dequeue from the head while head < t - 3000,
        # then return the queue size
        pass


if __name__ == "__main__":
    rc = RecentCounter()
    print(rc.ping(1))  # expected: 1
    print(rc.ping(100))  # expected: 2
    print(rc.ping(3001))  # expected: 3
    print(rc.ping(3002))  # expected: 3
    rc2 = RecentCounter()
    print(rc2.ping(642))  # expected: 1
    print(rc2.ping(1849))  # expected: 2
    print(rc2.ping(4921))  # expected: 1
    print(rc2.ping(5814))  # expected: 2
