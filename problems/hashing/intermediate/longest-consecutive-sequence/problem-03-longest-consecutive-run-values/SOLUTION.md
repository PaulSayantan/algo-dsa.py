# Longest Consecutive Run (Return the Values) — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestConsecutiveRun(self, nums):
        s = set(nums)
        best_start = None
        best_len = 0
        for x in sorted(s):
            if x - 1 not in s:
                length = 1
                y = x + 1
                while y in s:
                    length += 1
                    y += 1
                if length > best_len:
                    best_len = length
                    best_start = x
        if best_start is None:
            return []
        return list(range(best_start, best_start + best_len))
```

### Complexity

O(n) time (sorting the distinct set is O(d log d)), O(n) space.
