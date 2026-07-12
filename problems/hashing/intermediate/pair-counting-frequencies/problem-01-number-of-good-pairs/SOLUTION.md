# Number of Good Pairs — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def numIdenticalPairs(self, nums):
        count = Counter(nums)
        return sum(c * (c - 1) // 2 for c in count.values())
```

### Complexity

O(n) time, O(n) space.
