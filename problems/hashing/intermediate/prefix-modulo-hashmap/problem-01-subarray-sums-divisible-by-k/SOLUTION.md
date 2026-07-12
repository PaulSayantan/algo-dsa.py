# Subarray Sums Divisible by K — Solution

## Optimal Approach

Equal prefix remainders bound a divisible sum; count equal-remainder pairs.

### Reference implementation

```python
class Solution:
    def subarraysDivByK(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        count = 0
        for x in nums:
            cur = (cur + x) % k
            count += freq[cur]
            freq[cur] += 1
        return count
```

### Complexity

Time O(n), space O(k).

## Key Insights & Edge Cases

Python's % already returns a non-negative remainder for positive k.
