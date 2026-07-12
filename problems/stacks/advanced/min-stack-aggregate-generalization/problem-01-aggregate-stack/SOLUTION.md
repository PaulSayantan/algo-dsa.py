# Stack with O(1) Min, Max, and GCD — Solution

## Optimal Approach

### Reference implementation

```python
class AggregateStack:
    def __init__(self):
        self._stack = []  # (value, min, max, gcd)

    def push(self, x):
        if not self._stack:
            self._stack.append((x, x, x, x))
        else:
            _, mn, mx, g = self._stack[-1]
            self._stack.append((x, min(mn, x), max(mx, x), math.gcd(g, x)))

    def pop(self):
        self._stack.pop()

    def getMin(self):
        return self._stack[-1][1]

    def getMax(self):
        return self._stack[-1][2]

    def getGcd(self):
        return self._stack[-1][3]
```
