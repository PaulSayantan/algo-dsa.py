# GCD Stack — Solution

## Optimal Approach

The GCD of all current elements is a prefix-computable statistic, so store it
alongside each value: the GCD-so-far at position `i` is
`gcd(value[i], gcd-so-far[i-1])`. Since it is carried forward, the top pair
always holds the GCD of the whole stack, giving O(1) `gcd()` and a trivial
`pop` that discards the pair (no non-invertible "undo" needed).

### Reference implementation

```python
class GCDStack:
    def __init__(self):
        self._stack = []  # (val, gcd_so_far)

    def push(self, x):
        g = x if not self._stack else math.gcd(x, self._stack[-1][1])
        self._stack.append((x, g))

    def pop(self):
        self._stack.pop()

    def top(self):
        return self._stack[-1][0]

    def gcd(self):
        return self._stack[-1][1]
```
