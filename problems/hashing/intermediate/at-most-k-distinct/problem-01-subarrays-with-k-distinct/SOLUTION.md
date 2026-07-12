# Subarrays with K Different Integers — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def at_most(m):
            count = defaultdict(int)
            left = 0
            res = 0
            for right, x in enumerate(nums):
                count[x] += 1
                while len(count) > m:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                res += right - left + 1
            return res
        return at_most(k) - at_most(k - 1)
```

### Complexity

O(n) time, O(k) space.
