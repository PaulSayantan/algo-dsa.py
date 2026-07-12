# Number of Recent Calls — Solution

## Optimal Approach

Keep a FIFO queue of timestamps backed by a singly linked list. Each `ping(t)`
enqueues `t` at the tail, then dequeues from the head every timestamp older than
`t - 3000` (i.e. strictly less than `t - 3000`). Because timestamps arrive in
increasing order, the head is always the oldest, so at most a prefix is dropped.
The queue's size after cleanup is the number of requests in `[t - 3000, t]`.

Each timestamp is enqueued once and dequeued at most once, so every `ping` is
amortized O(1).

### Reference implementation

```python
class _Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class RecentCounter:
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

    def ping(self, t):
        self._enqueue(t)
        while self._head is not None and self._head.val < t - 3000:
            self._dequeue()
        return self._size
```
