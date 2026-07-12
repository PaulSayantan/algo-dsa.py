# Sum of the Longest Consecutive Run — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def sumOfLongestRun(self, nums):
        s = set(nums)
        best_len = 0
        best_sum = 0
        for x in sorted(s):
            if x - 1 not in s:
                length = 1
                y = x + 1
                while y in s:
                    length += 1
                    y += 1
                if length > best_len:
                    best_len = length
                    best_sum = sum(range(x, x + length))
        return best_sum
```

### Complexity

O(n) time, O(n) space.
