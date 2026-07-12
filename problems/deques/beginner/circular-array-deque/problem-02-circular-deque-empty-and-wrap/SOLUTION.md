# Circular Deque — Empty Handling and Wrap-Around — Solution

## Optimal Approach

### Reference implementation

```python
class MyCircularDeque:
    def __init__(self, k):
        self._cap = k
        self._data = [0] * k
        self._head = 0
        self._count = 0

    def insertFront(self, value):
        if self._count == self._cap:
            return False
        self._head = (self._head - 1) % self._cap
        self._data[self._head] = value
        self._count += 1
        return True

    def insertLast(self, value):
        if self._count == self._cap:
            return False
        tail = (self._head + self._count) % self._cap
        self._data[tail] = value
        self._count += 1
        return True

    def deleteFront(self):
        if self._count == 0:
            return False
        self._head = (self._head + 1) % self._cap
        self._count -= 1
        return True

    def deleteLast(self):
        if self._count == 0:
            return False
        self._count -= 1
        return True

    def getFront(self):
        if self._count == 0:
            return -1
        return self._data[self._head]

    def getRear(self):
        if self._count == 0:
            return -1
        return self._data[(self._head + self._count - 1) % self._cap]

    def isEmpty(self):
        return self._count == 0

    def isFull(self):
        return self._count == self._cap
```
