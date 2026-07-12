# Binary Subarrays With Sum — Solution

## Optimal Approach

Prefix-sum frequency map; goal=0 counts runs of zeros via C(len+1,2).

### Reference implementation

```python
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        freq = defaultdict(int)
        freq[0] = 1
        cur = 0
        count = 0
        for x in nums:
            cur += x
            count += freq[cur - goal]
            freq[cur] += 1
        return count
```

### Complexity

Time O(n), space O(n).

## Key Insights & Edge Cases

All-zeros with goal 0: 5 zeros give 5+4+3+2+1 = 15 subarrays.
