"""Design a fixed-capacity circular deque backed by a doubly linked list.

Two sentinel nodes make insert/delete at either end O(1); a size counter plus
the capacity ``k`` gives O(1) isEmpty / isFull. Bounded inserts return False
when full, deletes return False when empty, and the getters return -1 when
empty.
"""


class _DNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int) -> None:
        # TODO: capacity k, size 0, two sentinels (head, tail) linked together
        pass

    def insertFront(self, value: int) -> bool:
        # TODO: if full return False; else splice after head sentinel
        pass

    def insertLast(self, value: int) -> bool:
        # TODO: if full return False; else splice before tail sentinel
        pass

    def deleteFront(self) -> bool:
        # TODO: if empty return False; else unlink head.next
        pass

    def deleteLast(self) -> bool:
        # TODO: if empty return False; else unlink tail.prev
        pass

    def getFront(self) -> int:
        # TODO: value of head.next, or -1 if empty
        pass

    def getRear(self) -> int:
        # TODO: value of tail.prev, or -1 if empty
        pass

    def isEmpty(self) -> bool:
        # TODO
        pass

    def isFull(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    dq = MyCircularDeque(3)
    print(dq.isEmpty())  # expected: True
    print(dq.getFront())  # expected: -1
    print(dq.insertLast(1))  # expected: True
    print(dq.insertLast(2))  # expected: True
    print(dq.insertFront(3))  # expected: True
    print(dq.insertFront(4))  # expected: False
    print(dq.getRear())  # expected: 2
    print(dq.isFull())  # expected: True
    print(dq.deleteLast())  # expected: True
    print(dq.insertFront(4))  # expected: True
    print(dq.getFront())  # expected: 4
    print(dq.getRear())  # expected: 1
    print(dq.isEmpty())  # expected: False
