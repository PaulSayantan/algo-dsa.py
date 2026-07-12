# Find the Difference — Solution

## Optimal Approach

`Counter(t) - Counter(s)` keeps only the surplus counts (Counter subtraction drops zero/negative entries), leaving exactly the one extra letter. (XOR of all char codes is an O(1)-space alternative.)

### Reference implementation

```python
class Solution:
    def findTheDifference(self, s, t):
        diff = Counter(t) - Counter(s)
        return next(iter(diff.elements()))
```

### Complexity

Time O(n), space O(k).
