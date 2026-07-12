# Moving Average from Data Stream — Solution

## Optimal Approach

### Reference implementation

```python
class MovingAverage:
    def __init__(self, size):
        self._size = size
        self._q = deque()
        self._sum = 0

    def next(self, val):
        self._q.append(val)
        self._sum += val
        if len(self._q) > self._size:
            self._sum -= self._q.popleft()
        return self._sum / len(self._q)
```
