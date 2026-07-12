# First Unique Number — Solution

## Optimal Approach

### Reference implementation

```python
class FirstUnique:
    def __init__(self, nums):
        self._count = {}
        self._dq = deque()  # candidate values, oldest first
        for v in nums:
            self.add(v)

    def showFirstUnique(self):
        while self._dq and self._count[self._dq[0]] > 1:
            self._dq.popleft()
        return self._dq[0] if self._dq else -1

    def add(self, value):
        self._count[value] = self._count.get(value, 0) + 1
        if self._count[value] == 1:
            self._dq.append(value)
```

### Complexity

O(1) amortized per operation.
