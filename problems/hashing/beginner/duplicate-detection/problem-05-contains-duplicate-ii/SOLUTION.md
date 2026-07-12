# Contains Duplicate II — Solution

## Optimal Approach

A hash map from value to its latest index lets each element check the gap to its previous occurrence in O(1). Storing only the most recent index is sufficient because that is the closest candidate.

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

Time O(n), space O(n).
