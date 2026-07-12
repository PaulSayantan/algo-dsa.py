# First and Last Occurrence via Hash Map — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def firstLast(self, nums, target):
        first = {}
        last = {}
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
        if target not in first:
            return [-1, -1]
        return [first[target], last[target]]
```

### Complexity

O(n) time, O(n) space.
