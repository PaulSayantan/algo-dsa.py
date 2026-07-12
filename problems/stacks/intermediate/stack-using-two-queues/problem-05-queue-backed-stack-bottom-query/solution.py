"""Queue-backed LIFO stack with a getBottom() query (rotate-on-push)."""
from collections import deque  # noqa: F401


class BottomStack:
    def __init__(self) -> None:
        # TODO: single queue, rotate on push so front is top, back is bottom
        pass

    def push(self, x: int) -> None:
        # TODO
        pass

    def pop(self) -> int:
        # TODO
        pass

    def top(self) -> int:
        # TODO
        pass

    def getBottom(self) -> int:
        # TODO: the oldest element is at the back of the queue
        pass

    def empty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    bs = BottomStack()
    bs.push(10)
    bs.push(20)
    bs.push(30)
    print(bs.top())  # expected: 30
    print(bs.getBottom())  # expected: 10
    print(bs.pop())  # expected: 30
    print(bs.getBottom())  # expected: 10
    print(bs.top())  # expected: 20
    print(bs.pop())  # expected: 20
    print(bs.pop())  # expected: 10
    print(bs.empty())  # expected: True
