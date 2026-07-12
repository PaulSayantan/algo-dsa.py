# Count Zero-Sum Subarrays — Solution

## Optimal Approach

A repeated prefix sum ⇒ a zero-sum range; count equal-prefix pairs.

### Reference implementation

```python
class Solution:
    def countZeroSum(self, nums):
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        count = 0
        for x in nums:
            cur += x
            count += freq[cur]
            freq[cur] += 1
        return count
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

[0,0,0]: prefix sums 0,0,0,0 → C(4,2)=6 zero-sum subarrays.
