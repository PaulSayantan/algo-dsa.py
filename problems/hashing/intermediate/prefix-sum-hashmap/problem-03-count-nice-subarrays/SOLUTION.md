# Count Number of Nice Subarrays — Solution

## Optimal Approach

Prefix count of odd numbers with a frequency map; count += freq[odd - k].

### Reference implementation

```python
class Solution:
    def numberOfSubarrays(self, nums, k):
        freq = defaultdict(int)
        freq[0] = 1
        odd = 0
        count = 0
        for x in nums:
            odd += x & 1
            count += freq[odd - k]
            freq[odd] += 1
        return count
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

Reduce to a 0/1 sum problem by taking each element mod 2.
