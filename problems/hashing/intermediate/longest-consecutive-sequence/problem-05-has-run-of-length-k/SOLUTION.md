# Consecutive Run of Length At Least K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def hasConsecutiveRun(self, nums, k):
        if k <= 0:
            return True
        s = set(nums)
        for x in s:
            if x - 1 not in s:
                length = 1
                y = x + 1
                while y in s:
                    length += 1
                    y += 1
                if length >= k:
                    return True
        return False
```

### Complexity

O(n) time, O(n) space.
