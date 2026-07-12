# Count Pairs Summing to Target — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countPairs(self, nums, target):
        seen = defaultdict(int)
        count = 0
        for x in nums:
            count += seen[target - x]
            seen[x] += 1
        return count
```

### Complexity

O(n) time, O(n) space.
