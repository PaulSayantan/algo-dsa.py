# 4Sum II — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        sums = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sums[a + b] += 1
        count = 0
        for c in nums3:
            for d in nums4:
                count += sums[-(c + d)]
        return count
```

### Complexity

O(n^2) time, O(n^2) space to hash the pairwise sums of the first two arrays.
