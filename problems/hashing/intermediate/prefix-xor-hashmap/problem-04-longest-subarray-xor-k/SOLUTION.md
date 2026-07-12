# Longest Subarray With XOR Equal to K — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestSubarrayXorK(self, nums, k):
        first = {0: -1}
        cur = 0
        best = 0
        for i, x in enumerate(nums):
            cur ^= x
            target = cur ^ k
            if target in first:
                best = max(best, i - first[target])
            if cur not in first:
                first[cur] = i
        return best
```

### Complexity

O(n) time, O(n) space.
