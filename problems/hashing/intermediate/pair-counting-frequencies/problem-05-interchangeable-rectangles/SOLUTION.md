# Number of Pairs of Interchangeable Rectangles — Solution

## Optimal Approach

### Reference implementation

```python
class Solution:
    def interchangeableRectangles(self, rectangles):
        count = Counter()
        res = 0
        for w, h in rectangles:
            g = math.gcd(w, h)
            key = (w // g, h // g)
            res += count[key]
            count[key] += 1
        return res
```

### Complexity

O(n) time, O(n) space.
