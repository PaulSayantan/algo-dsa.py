# Contiguous Array — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findMaxLength(self, nums):
        first = {0: -1}
        balance = 0
        best = 0
        for i, x in enumerate(nums):
            balance += 1 if x == 1 else -1
            if balance in first:
                best = max(best, i - first[balance])
            else:
                first[balance] = i
        return best
```

### Complexity

O(n) time, O(n) space.
