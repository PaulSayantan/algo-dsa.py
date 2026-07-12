# Design a Stack (Array-Backed) — Solution

## Optimal Approach

### Reference implementation

```python
class MyStack:
    def __init__(self):
        self._data = []

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0
```
