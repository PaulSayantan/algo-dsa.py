"""Queue with max_value — amortized O(1) max (design)."""
from collections import deque  # noqa: F401


class MaxQueue:
    def __init__(self) -> None:
        # TODO: data queue + monotonic helper deque
        pass

    def push_back(self, x: int) -> None:
        # TODO
        pass

    def pop_front(self) -> int:
        # TODO
        pass

    def max_value(self) -> int:
        # TODO
        pass


if __name__ == "__main__":
    mq = MaxQueue()
    mq.push_back(1)
    mq.push_back(3)
    mq.push_back(2)
    print(mq.max_value())  # expected: 3
    print(mq.pop_front())  # expected: 1
    print(mq.max_value())  # expected: 3
    print(mq.pop_front())  # expected: 3
    print(mq.max_value())  # expected: 2
