# Count Pairs With Absolute Difference K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countKDifference(self, nums, k):
        count = Counter()
        res = 0
        for x in nums:
            res += count[x - k] + count[x + k]
            count[x] += 1
        return res
```

### Complexity

O(n) time, O(n) space.
