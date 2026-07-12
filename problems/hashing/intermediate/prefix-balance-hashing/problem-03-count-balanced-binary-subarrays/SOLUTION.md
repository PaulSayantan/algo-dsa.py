# Count Balanced Binary Subarrays — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countBalancedSubarrays(self, nums):
        freq = defaultdict(int)
        freq[0] = 1
        balance = 0
        count = 0
        for x in nums:
            balance += 1 if x == 1 else -1
            count += freq[balance]
            freq[balance] += 1
        return count
```

### Complexity

O(n) time, O(n) space.
