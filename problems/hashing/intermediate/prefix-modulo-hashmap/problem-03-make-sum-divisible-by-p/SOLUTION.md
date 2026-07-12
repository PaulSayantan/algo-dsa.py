# Make Sum Divisible by P — Solution

## Optimal Approach

Map each prefix remainder to its latest index; look up (cur-need)%p.

### Reference implementation

```python
class Solution:
    def minSubarray(self, nums, p):
        total = sum(nums) % p
        if total == 0:
            return 0
        n = len(nums)
        first = {0: -1}
        cur = 0
        best = n
        for i, x in enumerate(nums):
            cur = (cur + x) % p
            need = (cur - total) % p
            if need in first:
                best = min(best, i - first[need])
            first[cur] = i
        return best if best < n else -1
```

### Complexity

Time O(n), space O(p).

## Key Insights & Edge Cases

[6,3,5,2] total=16, 16%9=7; shortest subarray with sum%9==7 is [5,2] length 2.
