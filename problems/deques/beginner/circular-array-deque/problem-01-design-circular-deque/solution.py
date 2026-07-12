"""Design Circular Deque — LeetCode 641.

Implement a double-ended queue on a fixed-capacity circular array. All
operations must be O(1). insert*/delete* return a bool (success); getFront /
getRear return -1 when the deque is empty.
"""
from typing import List  # noqa: F401


class MyCircularDeque:
    def __init__(self, k: int) -> None:
        # TODO: fixed buffer of size k, a head index, and an element count
        pass

    def insertFront(self, value: int) -> bool:
        # TODO
        pass

    def insertLast(self, value: int) -> bool:
        # TODO
        pass

    def deleteFront(self) -> bool:
        # TODO
        pass

    def deleteLast(self) -> bool:
        # TODO
        pass

    def getFront(self) -> int:
        # TODO
        pass

    def getRear(self) -> int:
        # TODO
        pass

    def isEmpty(self) -> bool:
        # TODO
        pass

    def isFull(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    dq = MyCircularDeque(3)
    print(dq.insertLast(1))  # expected: True
    print(dq.insertLast(2))  # expected: True
    print(dq.insertFront(3))  # expected: True
    print(dq.insertFront(4))  # expected: False
    print(dq.getRear())  # expected: 2
    print(dq.isFull())  # expected: True
    print(dq.deleteLast())  # expected: True
    print(dq.insertFront(4))  # expected: True
    print(dq.getFront())  # expected: 4
    print(dq.isEmpty())  # expected: False
