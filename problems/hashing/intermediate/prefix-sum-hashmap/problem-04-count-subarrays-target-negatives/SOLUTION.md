# Count Subarrays Summing to Target (with Negatives) — Solution

## Optimal Approach

Prefix-sum frequency map; negatives are handled naturally.

### Reference implementation

```python
class Solution:
    def countSubarrays(self, nums, target):
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        count = 0
        for x in nums:
            cur += x
            count += freq[cur - target]
            freq[cur] += 1
        return count
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

[1,-1,1,-1] has zero-sum subarrays [1,-1]x2, [-1,1], [1,-1,1,-1].
