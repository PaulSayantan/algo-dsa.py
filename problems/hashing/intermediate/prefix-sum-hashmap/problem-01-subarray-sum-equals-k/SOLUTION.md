# Subarray Sum Equals K — Solution

## Optimal Approach

Count previous prefix sums equal to `cur - k`; store frequencies of each prefix sum as you scan.

### Reference implementation

```python
class Solution:
    def subarraySum(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        count = 0
        for x in nums:
            cur += x
            count += freq[cur - k]
            freq[cur] += 1
        return count
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

Seed freq[0]=1; count BEFORE inserting the current prefix.
