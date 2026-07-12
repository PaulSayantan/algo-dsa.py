# Design Count-Min Sketch — Solution

## Optimal Approach

With `w = 50`, `2654435761 mod 50 = 11`, `40503 mod 50 = 3`, so `col_r(x) = (11*x + 3*(r+1)) mod 50`.

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

update / estimate are O(d); space is O(d*w).

## Key Insights & Edge Cases

Columns: 5 -> (8,11,14) over rows 0..2; 7 -> (30,33,36); 9 -> (2,5,8). No two of these share a cell in the same row, so each item's counters hold exactly its own count: estimate(5)=3, estimate(7)=2, estimate(9)=0. If a collision existed the min would still be >= the true count (one-sided over-estimation).
