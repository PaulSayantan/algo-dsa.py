# Longest Subarray With Equal Counts of Two Values — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestEqualCount(self, nums, a, b):
        first = {0: -1}
        balance = 0
        best = 0
        for i, x in enumerate(nums):
            if x == a:
                balance += 1
            elif x == b:
                balance -= 1
            if balance in first:
                best = max(best, i - first[balance])
            else:
                first[balance] = i
        return best
```

### Complexity

O(n) time, O(n) space.
