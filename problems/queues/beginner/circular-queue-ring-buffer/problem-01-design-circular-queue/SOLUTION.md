# Design Circular Queue — Solution

## Optimal Approach

### Reference implementation

```python
class MyCircularQueue:
    def __init__(self, k):
        self._q = [0] * k
        self._cap = k
        self._head = 0
        self._count = 0

    def enQueue(self, value):
        if self.isFull():
            return False
        self._q[(self._head + self._count) % self._cap] = value
        self._count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self._head = (self._head + 1) % self._cap
        self._count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self._q[self._head]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self._q[(self._head + self._count - 1) % self._cap]

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == self._cap
```
