# Longest Zero-Sum Subarray — Solution

## Optimal Approach

Special case of sum==k with k=0; earliest occurrence of each prefix sum.

### Reference implementation

```python
class Solution:
    def longestZeroSum(self, nums):
        first = {0: -1}
        cur = 0
        best = 0
        for i, x in enumerate(nums):
            cur += x
            if cur in first:
                best = max(best, i - first[cur])
            else:
                first[cur] = i
        return best
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

[15,-2,2,-8,1] sums to 8-... actually -2+2-8+1+7=0 over indices 1..5 → length 5.
