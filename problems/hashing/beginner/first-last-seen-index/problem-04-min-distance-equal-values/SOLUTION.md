# Minimum Distance Between Equal Values — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def minEqualDistance(self, nums):
        last = {}
        best = -1
        for i, x in enumerate(nums):
            if x in last:
                d = i - last[x]
                if best == -1 or d < best:
                    best = d
            last[x] = i
        return best
```

### Complexity

O(n) time, O(n) space.
