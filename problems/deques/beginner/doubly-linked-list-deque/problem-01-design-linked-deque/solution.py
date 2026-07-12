"""Design a deque backed by a doubly linked list.

pushFront / pushBack / popFront / popBack are all O(1) at either end using two
sentinel nodes. pop* return the removed value, or -1 when the deque is empty.
"""


class _DNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class LinkedDeque:
    def __init__(self) -> None:
        # TODO: two sentinel nodes (head, tail) linked to each other + a size
        pass

    def pushFront(self, val: int) -> None:
        # TODO: splice a new node in right after the head sentinel
        pass

    def pushBack(self, val: int) -> None:
        # TODO: splice a new node in right before the tail sentinel
        pass

    def popFront(self) -> int:
        # TODO: unlink head.next; return its value (or -1 if empty)
        pass

    def popBack(self) -> int:
        # TODO: unlink tail.prev; return its value (or -1 if empty)
        pass

    def isEmpty(self) -> bool:
        # TODO
        pass


if __name__ == "__main__":
    dq = LinkedDeque()
    print(dq.isEmpty())  # expected: True
    dq.pushBack(1)
    dq.pushBack(2)
    dq.pushFront(0)
    print(dq.popFront())  # expected: 0
    print(dq.popBack())  # expected: 2
    print(dq.popFront())  # expected: 1
    print(dq.isEmpty())  # expected: True
    print(dq.popBack())  # expected: -1
