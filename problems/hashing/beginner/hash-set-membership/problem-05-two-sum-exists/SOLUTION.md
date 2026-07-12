# Two-Sum Existence — Solution

## Optimal Approach

Checking `target - x` against the set of values seen *so far* (before inserting x) guarantees the partner sits at an earlier, distinct index — one pass, no sorting.

### Reference implementation

```python
class Solution:
    def twoSumExists(self, nums, target):
        seen = set()
        for x in nums:
            if target - x in seen:
                return True
            seen.add(x)
        return False
```

### Complexity

Time O(n), space O(n).
