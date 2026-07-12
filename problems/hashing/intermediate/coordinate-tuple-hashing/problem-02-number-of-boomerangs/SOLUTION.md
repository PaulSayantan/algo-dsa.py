# Number of Boomerangs — Solution

## Optimal Approach

Use integer squared distances as keys; sum c*(c-1) over each anchor's buckets.

### Reference implementation

```python
class Solution:
    def numberOfBoomerangs(self, points):
        total = 0
        for x1, y1 in points:
            dist = defaultdict(int)
            for x2, y2 in points:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2
                dist[d] += 1
            for c in dist.values():
                total += c * (c - 1)
        return total
```

### Complexity

Time O(n^2), space O(n).

## Key Insights & Edge Cases

Squared distance keeps keys integral and exact — never take a square root.
