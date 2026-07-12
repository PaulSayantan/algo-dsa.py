# Longest Consecutive Sequence — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestConsecutive(self, nums):
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:
                length = 1
                y = x + 1
                while y in s:
                    length += 1
                    y += 1
                best = max(best, length)
        return best
```

### Complexity

O(n) time, O(n) space.
