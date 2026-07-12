# Max Stack — Solution

## Optimal Approach

### Reference implementation

```python
class MaxStack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def peekMax(self):
        return max(self._data)

    def popMax(self):
        m = max(self._data)
        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] == m:
                del self._data[i]
                return m
```
