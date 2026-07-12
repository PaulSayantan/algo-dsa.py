# Missing Number — Solution

## Optimal Approach

Because the values are known to be the distinct set {0..n} minus one, a membership set lets a single 0..n scan find the absent index. (The n(n+1)/2 sum formula is an O(1)-space alternative.)

### Reference implementation

```python
class Solution:
    def missingNumber(self, nums):
        present = set(nums)
        for i in range(len(nums) + 1):
            if i not in present:
                return i
        return -1
```

### Complexity

Time O(n), space O(n).
