# Min-Max Stack — Solution

## Optimal Approach

Alongside every pushed value, store the minimum and maximum seen from the bottom
of the stack up to (and including) that element. Because both are prefix
statistics, the top triple always holds the current min and max, so `getMin`
and `getMax` are O(1) reads and `pop` simply discards the triple.

### Reference implementation

```python
class MinMaxStack:
    def __init__(self):
        self._stack = []  # (val, min_so_far, max_so_far)

    def push(self, x):
        if not self._stack:
            self._stack.append((x, x, x))
        else:
            _, lo, hi = self._stack[-1]
            self._stack.append((x, min(x, lo), max(x, hi)))

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1][0]

    def getMin(self):
        return self._stack[-1][1]

    def getMax(self):
        return self._stack[-1][2]
```
