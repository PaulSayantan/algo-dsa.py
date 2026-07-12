# Design Circular Deque — Solution

## Optimal Approach

Use a doubly linked list with two sentinel nodes (`head`, `tail`) so both ends
splice in O(1) with no null checks, and track `size` against the fixed capacity
`k`. `insert*` refuse when `size == k`; `delete*` and the getters refuse (return
`False` / `-1`) when `size == 0`.

### Reference implementation

```python
class _DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyCircularDeque:
    def __init__(self, k):
        self._cap = k
        self._size = 0
        self._head = _DNode(None)  # sentinel
        self._tail = _DNode(None)  # sentinel
        self._head.next = self._tail
        self._tail.prev = self._head

    def insertFront(self, value):
        if self._size == self._cap:
            return False
        first = self._head.next
        node = _DNode(value)
        node.prev = self._head
        node.next = first
        self._head.next = node
        first.prev = node
        self._size += 1
        return True

    def insertLast(self, value):
        if self._size == self._cap:
            return False
        last = self._tail.prev
        node = _DNode(value)
        node.next = self._tail
        node.prev = last
        self._tail.prev = node
        last.next = node
        self._size += 1
        return True

    def deleteFront(self):
        if self._size == 0:
            return False
        node = self._head.next
        self._head.next = node.next
        node.next.prev = self._head
        self._size -= 1
        return True

    def deleteLast(self):
        if self._size == 0:
            return False
        node = self._tail.prev
        self._tail.prev = node.prev
        node.prev.next = self._tail
        self._size -= 1
        return True

    def getFront(self):
        if self._size == 0:
            return -1
        return self._head.next.val

    def getRear(self):
        if self._size == 0:
            return -1
        return self._tail.prev.val

    def isEmpty(self):
        return self._size == 0

    def isFull(self):
        return self._size == self._cap
```
