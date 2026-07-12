# Moving Average from Data Stream — Solution

## Optimal Approach

Hold the current window in a singly linked list queue and maintain a running
`sum`. On each `next(val)`, enqueue `val` at the tail and add it to `sum`. If the
queue now holds more than `size` values, dequeue the oldest value from the head
and subtract it from `sum`. The moving average is `sum` divided by the current
number of queued values.

Both the enqueue and the (single) eviction are O(1), so `next` is O(1) per call
and uses O(size) space.

### Reference implementation

```python
class _Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MovingAverage:
    def __init__(self, size):
        self._cap = size
        self._head = None
        self._tail = None
        self._count = 0
        self._sum = 0

    def next(self, val):
        node = _Node(val)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._count += 1
        self._sum += val
        if self._count > self._cap:
            old = self._head
            self._head = old.next
            if self._head is None:
                self._tail = None
            self._count -= 1
            self._sum -= old.val
        return self._sum / self._count
```
