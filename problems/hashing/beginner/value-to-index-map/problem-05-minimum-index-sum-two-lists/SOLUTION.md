# Minimum Index Sum of Two Lists — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def findRestaurant(self, list1, list2):
        idx = {name: i for i, name in enumerate(list1)}
        best = math.inf
        result = []
        for j, name in enumerate(list2):
            if name in idx:
                total = idx[name] + j
                if total < best:
                    best = total
                    result = [name]
                elif total == best:
                    result.append(name)
        return sorted(result)
```

### Complexity

O(m + n) time, O(m) space for the name -> index map.
