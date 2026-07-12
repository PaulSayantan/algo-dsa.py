# Count Subarrays Divisible by K — Solution

## Optimal Approach

Same as LeetCode 974; count C(cnt,2) over equal remainders (incl. the seed 0).

### Reference implementation

```python
class Solution:
    def countDivisible(self, nums, k):
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

[2,4,6] all divisible: remainders 0,0,0,0 → C(4,2)=6.
