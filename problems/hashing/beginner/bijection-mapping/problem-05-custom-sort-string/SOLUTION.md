# Custom Sort String — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def customSortString(self, order, s):
        rank = {c: i for i, c in enumerate(order)}
        return "".join(sorted(s, key=lambda c: rank.get(c, len(order))))
```
