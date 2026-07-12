# Max Points on a Line — Solution

## Optimal Approach

Per anchor, bucket every other point by reduced slope; the biggest bucket + anchor wins.

### Reference implementation

```python
class Solution:
    def maxPoints(self, points):
        n = len(points)
        if n <= 2:
            return n
        best = 1
        for i in range(n):
            slopes = defaultdict(int)
            xi, yi = points[i]
            for j in range(n):
                if j == i:
                    continue
                dx = points[j][0] - xi
                dy = points[j][1] - yi
                g = math.gcd(dx, dy)
                if g:
                    dx //= g
                    dy //= g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
                best = max(best, slopes[(dx, dy)] + 1)
        return best
```

### Complexity

Time O(n^2), space O(n).

## Key Insights & Edge Cases

Normalize sign so (1,1) and (-1,-1) map to one key; never use float slopes.
