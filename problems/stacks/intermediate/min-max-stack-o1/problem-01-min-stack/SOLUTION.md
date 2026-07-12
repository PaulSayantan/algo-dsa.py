# Min Stack — Solution

## Optimal Approach

### Reference implementation

```python
class MinStack:
    def __init__(self):
        self._stack = []  # (val, min_so_far)

    def push(self, val):
        cur = val if not self._stack else min(val, self._stack[-1][1])
        self._stack.append((val, cur))

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1][0]

    def getMin(self):
        return self._stack[-1][1]
```
