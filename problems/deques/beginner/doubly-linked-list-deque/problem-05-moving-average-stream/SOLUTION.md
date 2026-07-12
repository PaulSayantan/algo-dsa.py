# Moving Average from Data Stream — Solution

## Optimal Approach

Keep the sliding window inside a doubly-linked-list deque and track a running
`sum`. On each `next(val)`: `pushBack(val)` and add it to `sum`; if the deque now
holds more than `size` values, `popFront()` the oldest and subtract it from
`sum`. The answer is `sum / deque.size()`. Both-end O(1) deque operations keep
`next` at O(1) with no re-summing.

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

    def size(self):
        return self._size


class MovingAverage:
    def __init__(self, size):
        self._cap = size
        self._dq = LinkedDeque()
        self._sum = 0

    def next(self, val):
        self._dq.pushBack(val)
        self._sum += val
        if self._dq.size() > self._cap:
            self._sum -= self._dq.popFront()
        return self._sum / self._dq.size()
```
