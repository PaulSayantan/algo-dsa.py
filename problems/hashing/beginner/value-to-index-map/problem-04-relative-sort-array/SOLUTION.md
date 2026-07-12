# Relative Sort Array — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def relativeSortArray(self, arr1, arr2):
        rank = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (rank.get(x, len(arr2)), x))
```

### Complexity

O(m + n log n) time with the rank map; O(m) space for the map.
