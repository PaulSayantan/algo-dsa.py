# Minimum Area Rectangle — Solution

## Optimal Approach

Each opposite-corner pair defines the other two corners; look them up in the set.

### Reference implementation

```python
class Solution:
    def minAreaRect(self, points):
        seen = set()
        best = 0
        pts = [(x, y) for x, y in points]
        for x, y in pts:
            seen.add((x, y))
        for i in range(len(pts)):
            x1, y1 = pts[i]
            for j in range(len(pts)):
                x2, y2 = pts[j]
                if x1 < x2 and y1 < y2:
                    if (x1, y2) in seen and (x2, y1) in seen:
                        area = (x2 - x1) * (y2 - y1)
                        if best == 0 or area < best:
                            best = area
        return best
```

### Complexity

Time O(n^2), space O(n).

## Key Insights & Edge Cases

The 2x1 rectangle (area 2) beats the 2x2 (area 4) in the second case.
