# Intersection of Two Arrays II — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        result = []
        for x in nums2:
            if c1[x] > 0:
                result.append(x)
                c1[x] -= 1
        return sorted(result)
```
