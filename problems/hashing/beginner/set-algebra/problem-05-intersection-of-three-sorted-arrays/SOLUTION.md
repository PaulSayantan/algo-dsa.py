# Intersection of Three Sorted Arrays — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        return sorted(set(arr1) & set(arr2) & set(arr3))
```
