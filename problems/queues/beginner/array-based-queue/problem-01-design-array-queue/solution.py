"""Design a FIFO queue backed by a list (enqueue/dequeue/front/empty)."""
from typing import Any  # noqa: F401


class ArrayQueue:
    def __init__(self) -> None:
        # TODO: keep the elements in a list; the front is index 0
        pass

    def enqueue(self, x: int) -> None:
        # TODO: add x at the rear (end of the list)
        pass

    def dequeue(self) -> int:
        # TODO: remove and return the front element
        pass

    def front(self) -> int:
        # TODO: peek at the front element
        pass

    def empty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    q = ArrayQueue()
    print(q.empty())  # expected: True
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.front())  # expected: 1
    print(q.dequeue())  # expected: 1
    print(q.front())  # expected: 2
    print(q.empty())  # expected: False
    print(q.dequeue())  # expected: 2
    print(q.dequeue())  # expected: 3
    print(q.empty())  # expected: True
