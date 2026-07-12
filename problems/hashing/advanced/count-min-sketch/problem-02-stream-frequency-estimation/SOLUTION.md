# Frequency Estimation over a Stream — Solution

## Optimal Approach

Same sketch; a single pass over the stream, O(d) per event.

### Reference implementation

```python
class CountMinSketch:
    def __init__(self, depth=3, width=50):
        self.depth = depth
        self.width = width
        self.table = [[0] * width for _ in range(depth)]

    def _col(self, x, row):
        return (x * 2654435761 + (row + 1) * 40503) % self.width

    def update(self, x, count=1):
        for r in range(self.depth):
            self.table[r][self._col(x, r)] += count

    def estimate(self, x):
        return min(self.table[r][self._col(x, r)] for r in range(self.depth))
```

### Complexity

O(d) per stream event; O(d*w) space regardless of stream length.

## Key Insights & Edge Cases

Stream counts are 5x3, 7x2, 9x1. 11 -> columns (24,27,30); none of those cells were touched by 5 (8,11,14), 7 (30,33,36), or 9 (2,5,8) in the matching row, so estimate(11)=0. The sketch's size is fixed no matter how long the stream is — that's the whole point.
