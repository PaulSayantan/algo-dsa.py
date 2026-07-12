# Maximum Distance Between Equal Values — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def maxEqualDistance(self, nums):
        first = {}
        best = 0
        for i, x in enumerate(nums):
            if x in first:
                best = max(best, i - first[x])
            else:
                first[x] = i
        return best
```

### Complexity

O(n) time, O(n) space. Only the first index of each value matters.
