"""Max Stack backed by a queue: LIFO via rotate-on-push, plus peekMax()."""
from collections import deque  # noqa: F401


class MaxStack:
    def __init__(self) -> None:
        # TODO: single queue, rotate on push so the top is at the front
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

    def peekMax(self) -> int:
        # TODO: linear scan for the maximum
        pass


if __name__ == "__main__":
    ms = MaxStack()
    ms.push(5)
    ms.push(1)
    ms.push(5)
    print(ms.top())  # expected: 5
    print(ms.peekMax())  # expected: 5
    print(ms.pop())  # expected: 5
    print(ms.peekMax())  # expected: 5
    print(ms.pop())  # expected: 1
    print(ms.peekMax())  # expected: 5
    print(ms.top())  # expected: 5
