# Longest Subarray With Sum K (Negatives) — Solution

## Optimal Approach

Same as LeetCode 325; the earliest index maximizes the qualifying length.

### Reference implementation

```python
class Solution:
    def longestSubarraySumK(self, nums, k):
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

With negatives a window is invalid; the prefix map is required.
