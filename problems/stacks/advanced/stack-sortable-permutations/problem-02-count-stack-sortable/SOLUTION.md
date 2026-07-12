# Count Stack-Sortable Permutations — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def countStackSortable(self, n):
        catalan = [0] * (n + 1)
        catalan[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]
        return catalan[n]
```
