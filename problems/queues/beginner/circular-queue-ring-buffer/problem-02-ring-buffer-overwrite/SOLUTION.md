# Ring Buffer with Overwrite — Solution

## Optimal Approach

### Reference implementation

```python
class RingBuffer:
    def __init__(self, capacity):
        self._buf = [None] * capacity
        self._cap = capacity
        self._head = 0
        self._size = 0

    def write(self, x):
        self._buf[(self._head + self._size) % self._cap] = x
        if self._size < self._cap:
            self._size += 1
        else:
            self._head = (self._head + 1) % self._cap

    def snapshot(self):
        return [self._buf[(self._head + i) % self._cap] for i in range(self._size)]

    def size(self):
        return self._size
```
