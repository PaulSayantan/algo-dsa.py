# Count Number of Pairs With Absolute Difference K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countKDifference(self, nums, k):
        seen = defaultdict(int)
        count = 0
        for x in nums:
            count += seen[x - k] + seen[x + k]
            seen[x] += 1
        return count
```

### Complexity

O(n) time, O(n) space. Counting earlier matches avoids double counting.
