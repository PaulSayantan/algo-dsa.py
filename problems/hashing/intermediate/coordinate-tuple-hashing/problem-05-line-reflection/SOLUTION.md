# Line Reflection — Solution

## Optimal Approach

Sum = minX+maxX; check (sum-x, y) membership for every point.

### Reference implementation

```python
class Solution:
    def isReflected(self, points):
        pts = set((x, y) for x, y in points)
        xs = [x for x, _ in pts]
        s = min(xs) + max(xs)
        for x, y in pts:
            if (s - x, y) not in pts:
                return False
        return True
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

Using min+max avoids fractions — compare 2x against the constant sum.
