# Longest Subarray Divisible by K — Solution

## Optimal Approach

Store the first index of each remainder; the longest equal-remainder gap wins.

### Reference implementation

```python
class Solution:
    def longestDivByK(self, nums, k):
        first = {0: -1}
        cur = 0
        best = 0
        for i, x in enumerate(nums):
            cur = (cur + x) % k
            if cur in first:
                best = max(best, i - first[cur])
            else:
                first[cur] = i
        return best
```

### Complexity

Time O(n), space O(k).

## Key Insights & Edge Cases

[2,7,6,1,4,5]%3 prefixes: 0,2,0,0,1,2,1 → longest equal-remainder gap is 4.
