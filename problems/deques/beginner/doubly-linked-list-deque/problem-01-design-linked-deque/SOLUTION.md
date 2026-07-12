# Design a Doubly-Linked Deque — Solution

## Optimal Approach

### Reference implementation

```python
class _DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class LinkedDeque:
    def __init__(self):
        self._head = _DNode(None)  # sentinel
        self._tail = _DNode(None)  # sentinel
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def pushFront(self, val):
        first = self._head.next
        node = _DNode(val)
        node.prev = self._head
        node.next = first
        self._head.next = node
        first.prev = node
        self._size += 1

    def pushBack(self, val):
        last = self._tail.prev
        node = _DNode(val)
        node.next = self._tail
        node.prev = last
        self._tail.prev = node
        last.next = node
        self._size += 1

    def popFront(self):
        if self._size == 0:
            return -1
        node = self._head.next
        self._head.next = node.next
        node.next.prev = self._head
        self._size -= 1
        return node.val

    def popBack(self):
        if self._size == 0:
            return -1
        node = self._tail.prev
        self._tail.prev = node.prev
        node.prev.next = self._tail
        self._size -= 1
        return node.val

    def isEmpty(self):
        return self._size == 0
```
