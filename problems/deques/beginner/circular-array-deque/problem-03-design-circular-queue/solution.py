"""Design Circular Queue — LeetCode 622.

Implement a FIFO queue on a fixed-capacity circular array. All operations must
be O(1). enQueue/deQueue return a bool (success); Front / Rear return -1 when
the queue is empty.
"""
from typing import List  # noqa: F401


class MyCircularQueue:
    def __init__(self, k: int) -> None:
        # TODO: fixed buffer of size k, a head index, and an element count
        pass

    def enQueue(self, value: int) -> bool:
        # TODO: write at (head + count) % capacity if not full
        pass

    def deQueue(self) -> bool:
        # TODO: advance head with % capacity if not empty
        pass

    def Front(self) -> int:
        # TODO
        pass

    def Rear(self) -> int:
        # TODO
        pass

    def isEmpty(self) -> bool:
        # TODO
        pass

    def isFull(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    q = MyCircularQueue(3)
    print(q.enQueue(1))  # expected: True
    print(q.enQueue(2))  # expected: True
    print(q.enQueue(3))  # expected: True
    print(q.enQueue(4))  # expected: False
    print(q.Rear())  # expected: 3
    print(q.isFull())  # expected: True
    print(q.deQueue())  # expected: True
    print(q.enQueue(4))  # expected: True
    print(q.Rear())  # expected: 4
    print(q.Front())  # expected: 2
    print(q.isEmpty())  # expected: False
