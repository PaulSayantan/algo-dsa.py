# Longest Subarray With Equal Counts of Three Categories — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestEqualThree(self, nums):
        c = [0, 0, 0]
        first = {(0, 0): -1}
        best = 0
        for i, x in enumerate(nums):
            c[x] += 1
            key = (c[0] - c[1], c[1] - c[2])
            if key in first:
                best = max(best, i - first[key])
            else:
                first[key] = i
        return best
```

### Complexity

O(n) time, O(n) space.
