# First Repeating Element — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def firstRepeatingIndex(self, nums):
        counts = Counter(nums)
        for i, x in enumerate(nums):
            if counts[x] > 1:
                return i
        return -1
```

### Complexity

O(n) time, O(n) space.
