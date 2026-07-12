# Count Subarrays With At Most K Distinct Integers — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def atMostKDistinct(self, nums, k):
        count = defaultdict(int)
        left = 0
        res = 0
        for right, x in enumerate(nums):
            count[x] += 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            res += right - left + 1
        return res
```

### Complexity

O(n) time, O(k) space.
