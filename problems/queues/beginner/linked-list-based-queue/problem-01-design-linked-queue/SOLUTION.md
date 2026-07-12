# Design a Linked-List Queue — Solution

## Optimal Approach

### Reference implementation

```python
class _Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedQueue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, x):
        node = _Node(x)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self):
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.val

    def front(self):
        return self._head.val

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0
```
