# Longest Subarray With At Most K Distinct Integers — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def longestKDistinct(self, nums, k):
        if k == 0:
            return 0
        count = defaultdict(int)
        left = 0
        best = 0
        for right, x in enumerate(nums):
            count[x] += 1
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            best = max(best, right - left + 1)
        return best
```

### Complexity

O(n) time, O(k) space.
