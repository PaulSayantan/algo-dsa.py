# Max Non-Overlapping Subarrays With Sum Target — Solution

## Optimal Approach

Track seen prefixes; on a match increment count and reset (non-overlap).

### Reference implementation

```python
class Solution:
    def maxNonOverlapping(self, nums, target):
        seen = {0}
        cur = 0
        count = 0
        for x in nums:
            cur += x
            if cur - target in seen:
                count += 1
                seen = {0}
                cur = 0
            else:
                seen.add(cur)
        return count
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

Resetting the seen set after a cut enforces non-overlap greedily.
