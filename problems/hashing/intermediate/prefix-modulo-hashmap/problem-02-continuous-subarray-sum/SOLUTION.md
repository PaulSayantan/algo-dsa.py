# Continuous Subarray Sum — Solution

## Optimal Approach

Store the first index of each remainder; require the gap to be >= 2.

### Reference implementation

```python
class Solution:
    def checkSubarraySum(self, nums, k):
        first = {0: -1}
        cur = 0
        for i, x in enumerate(nums):
            cur = (cur + x) % k
            if cur in first:
                if i - first[cur] >= 2:
                    return True
            else:
                first[cur] = i
        return False
```

### Complexity

Time O(n), space O(k).

## Key Insights & Edge Cases

[1,0] with k=2: remainders 1 then 1 but only length 1 apart → False.
