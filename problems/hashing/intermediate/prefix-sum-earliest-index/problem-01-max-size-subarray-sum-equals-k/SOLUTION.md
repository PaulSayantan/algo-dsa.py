# Maximum Size Subarray Sum Equals k — Solution

## Optimal Approach

Record the first index of each prefix sum; measure the longest gap.

### Reference implementation

```python
class Solution:
    def maxSubArrayLen(self, nums, k):
        first = {0: -1}
        cur = 0
        best = 0
        for i, x in enumerate(nums):
            cur += x
            if cur - k in first:
                best = max(best, i - first[cur - k])
            if cur not in first:
                first[cur] = i
        return best
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

Only insert a prefix sum if unseen — the earliest index maximizes length.
