# Count Maximal Consecutive Runs — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countConsecutiveRuns(self, nums):
        s = set(nums)
        runs = 0
        for x in s:
            if x - 1 not in s:
                runs += 1
        return runs
```

### Complexity

O(n) time, O(n) space.
