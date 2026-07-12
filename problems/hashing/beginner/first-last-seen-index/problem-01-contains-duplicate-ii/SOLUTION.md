# Contains Duplicate II — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last = {}
        for i, x in enumerate(nums):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i
        return False
```

### Complexity

O(n) time, O(n) space (or O(min(n,k)) with a sliding set).
