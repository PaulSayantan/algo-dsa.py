# Implement Stack using Queues — Solution

## Optimal Approach

Keep a single FIFO queue backed by a singly linked list. The trick is to make
`push` do the reordering: after enqueuing the new value at the tail, rotate the
queue by dequeuing and re-enqueuing the `size - 1` elements that were already
there. That brings the just-pushed value to the head, so the queue's front
always holds the stack's top.

With the invariant "head == stack top" maintained by `push`, both `pop` and
`top` are O(1) reads of the head. `push` is O(n) because of the rotation, which
is the standard single-queue trade-off for this problem.

### Reference implementation

```python
class _Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyStack:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def _enqueue(self, x):
        node = _Node(x)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def _dequeue(self):
        node = self._head
        self._head = node.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return node.val

    def push(self, x):
        self._enqueue(x)
        for _ in range(self._size - 1):
            self._enqueue(self._dequeue())

    def pop(self):
        return self._dequeue()

    def top(self):
        return self._head.val

    def empty(self):
        return self._size == 0
```
