# First Unique Stream Tracker — Solution

## Optimal Approach

### Reference implementation

```python
class FirstUniqueStream:
    def __init__(self):
        self._count = {}
        self._dq = deque()  # candidate values, oldest first
        self._unique = 0

    def add(self, value):
        self._count[value] = self._count.get(value, 0) + 1
        c = self._count[value]
        if c == 1:
            self._dq.append(value)
            self._unique += 1
        elif c == 2:
            self._unique -= 1

    def first(self):
        while self._dq and self._count[self._dq[0]] > 1:
            self._dq.popleft()
        return self._dq[0] if self._dq else None

    def numUnique(self):
        return self._unique
```

### Complexity

O(1) amortized per operation; each value is enqueued and dequeued at most once.
