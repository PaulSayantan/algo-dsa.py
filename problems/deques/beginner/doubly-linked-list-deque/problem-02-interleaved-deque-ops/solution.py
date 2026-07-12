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
    dq.pushFront(10)
    dq.pushFront(20)
    dq.pushBack(30)
    print(dq.popBack())  # expected: 30
    print(dq.popFront())  # expected: 20
    dq.pushBack(40)
    print(dq.popFront())  # expected: 10
    print(dq.popFront())  # expected: 40
    print(dq.isEmpty())  # expected: True
