# Set Mismatch — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findErrorNums(self, nums):
        counts = Counter(nums)
        n = len(nums)
        dup = missing = -1
        for x in range(1, n + 1):
            c = counts[x]
            if c == 2:
                dup = x
            elif c == 0:
                missing = x
        return [dup, missing]
```
