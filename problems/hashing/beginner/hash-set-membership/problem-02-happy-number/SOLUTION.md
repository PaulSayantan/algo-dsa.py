# Happy Number — Solution

## Optimal Approach

The sequence of sum-of-digit-squares values is deterministic, so it either hits 1 or revisits a previous value. A set of visited values detects the revisit and stops the loop.

### Reference implementation

```python
class Solution:
    def isHappy(self, n):
        def step(x):
            total = 0
            while x > 0:
                x, d = divmod(x, 10)
                total += d * d
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = step(n)
        return n == 1
```

### Complexity

Time O(log n) per transform step over a bounded number of steps; space O(k) for the visited set.
