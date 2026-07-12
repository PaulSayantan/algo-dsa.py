# Design Circular Queue — Solution

## Optimal Approach

Back the queue with a fixed array plus a `head` index and an element `count`. The
front lives at `head`; the rear lives at `(head + count - 1) % cap`. Enqueue
writes at the next tail slot `(head + count) % cap`; dequeue just advances `head`
modulo the capacity, so freed slots are transparently reused as the indices wrap.

### Reference implementation

```python
class MyCircularQueue:
    def __init__(self, k):
        self._cap = k
        self._data = [0] * k
        self._head = 0
        self._count = 0

    def enQueue(self, value):
        if self._count == self._cap:
            return False
        tail = (self._head + self._count) % self._cap
        self._data[tail] = value
        self._count += 1
        return True

    def deQueue(self):
        if self._count == 0:
            return False
        self._head = (self._head + 1) % self._cap
        self._count -= 1
        return True

    def Front(self):
        if self._count == 0:
            return -1
        return self._data[self._head]

    def Rear(self):
        if self._count == 0:
            return -1
        return self._data[(self._head + self._count - 1) % self._cap]

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == self._cap
```
