# Design a Queue (Array-Backed) — Solution

## Optimal Approach

### Reference implementation

```python
class ArrayQueue:
    def __init__(self):
        self._data = []

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.pop(0)

    def front(self):
        return self._data[0]

    def empty(self):
        return len(self._data) == 0
```
