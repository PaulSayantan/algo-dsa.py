# Partially-Retroactive Stack — Solution

## Optimal Approach

### Reference implementation

```python
class RetroStack:
    def __init__(self):
        self._ops = []  # (time, seq, kind, value)
        self._seq = 0

    def insertPush(self, t, x):
        self._ops.append((t, self._seq, 'push', x))
        self._seq += 1

    def insertPop(self, t):
        self._ops.append((t, self._seq, 'pop', None))
        self._seq += 1

    def top(self):
        stack = []
        for _, _, kind, value in sorted(self._ops):
            if kind == 'push':
                stack.append(value)
            elif stack:
                stack.pop()
        return stack[-1] if stack else -1
```
