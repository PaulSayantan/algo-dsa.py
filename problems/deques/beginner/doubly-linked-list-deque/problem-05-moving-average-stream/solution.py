"""Moving average over a sliding window, backed by a doubly-linked-list deque.

The deque holds at most ``size`` most-recent values. Each ``next`` pushes the
new value at the back and, if the window overflowed, pops the oldest at the
front; a running sum kept in step makes every ``next`` O(1).
"""


class _DNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None


class LinkedDeque:
    def __init__(self) -> None:
        self._head = _DNode(None)  # sentinel
        self._tail = _DNode(None)  # sentinel
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def pushBack(self, val):
        last = self._tail.prev
        node = _DNode(val)
        node.next = self._tail
        node.prev = last
        self._tail.prev = node
        last.next = node
        self._size += 1

    def popFront(self):
        node = self._head.next
        self._head.next = node.next
        node.next.prev = self._head
        self._size -= 1
        return node.val

    def size(self) -> int:
        return self._size


class MovingAverage:
    def __init__(self, size: int) -> None:
        # TODO: store window size, a LinkedDeque, and a running sum
        pass

    def next(self, val: int) -> float:
        # TODO: pushBack val (+= sum); if over size, popFront (-= sum);
        #       return sum / current length
        pass


if __name__ == "__main__":
    ma = MovingAverage(3)
    print(ma.next(1))  # expected: 1.0
    print(ma.next(10))  # expected: 5.5
    print(ma.next(3))  # expected: 4.666666666666667
    print(ma.next(5))  # expected: 6.0

    ma2 = MovingAverage(2)
    print(ma2.next(4))  # expected: 4.0
    print(ma2.next(8))  # expected: 6.0
    print(ma2.next(2))  # expected: 5.0
