# Number of Good Pairs — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def numIdenticalPairs(self, nums):
        seen = defaultdict(int)
        count = 0
        for x in nums:
            count += seen[x]
            seen[x] += 1
        return count
```

### Complexity

O(n) time, O(n) space. A value seen c times contributes C(c,2) pairs.
