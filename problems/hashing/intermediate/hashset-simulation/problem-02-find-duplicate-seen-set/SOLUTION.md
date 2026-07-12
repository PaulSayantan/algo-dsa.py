# Find the Duplicate Number (Seen Set) — Solution

## Optimal Approach

Membership test as you scan; first hit is the duplicate.

### Reference implementation

```python
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        return -1
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

The first value seen twice in scan order is returned.
