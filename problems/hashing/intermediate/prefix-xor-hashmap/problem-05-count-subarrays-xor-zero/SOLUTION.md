# Count Subarrays With XOR Equal to Zero — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countZeroXorSubarrays(self, nums):
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        count = 0
        for x in nums:
            cur ^= x
            count += freq[cur]
            freq[cur] += 1
        return count
```

### Complexity

O(n) time, O(n) space.
