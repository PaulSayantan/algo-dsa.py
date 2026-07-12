# Intersection of Two Arrays — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def intersection(self, nums1, nums2):
        return sorted(set(nums1) & set(nums2))
```
