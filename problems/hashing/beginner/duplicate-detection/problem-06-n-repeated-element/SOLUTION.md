# N-Repeated Element in Size 2N Array — Solution

## Optimal Approach

Only one value repeats, so the first value that is already in the set must be it — no need to count all the way to n. Early-exit keeps it a partial pass.

### Reference implementation

```python
class Solution:
    def repeatedNTimes(self, nums):
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        return -1
```

### Complexity

Time O(n), space O(n).
