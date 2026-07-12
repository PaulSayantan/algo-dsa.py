# Find the Difference of Two Arrays — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        return [sorted(s1 - s2), sorted(s2 - s1)]
```
