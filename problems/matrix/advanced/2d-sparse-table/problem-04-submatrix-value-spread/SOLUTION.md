# Solution — Submatrix Value Spread

## Brute Force

For each query, scan the rectangle tracking both the running max and min, then
subtract.

- **Time:** O(q · n · m) — up to `5·10^10` cell visits at the limits, too slow.
- **Space:** O(1) extra.

## Optimal Approach — Two 2D Sparse Tables

`spread = max − min`. Both `max` and `min` are idempotent, so we build **two**
independent 2D Sparse Tables over the same matrix — one merging with `max`, one
with `min`. Each query does one O(1) lookup in each table and subtracts:

```
spread(r1,c1,r2,c2) = maxTable.query(r1,c1,r2,c2)
                    - minTable.query(r1,c1,r2,c2)
```

The two tables are completely independent; sharing the same query geometry
(same `kr`, `kc`, same four corners) keeps the code symmetric.

### Reference implementation

```python
from typing import List, Callable


class SparseTable2D:
    def __init__(self, mat: List[List[int]], func: Callable[[int, int], int]):
        self.f = func
        self.n, self.m = len(mat), len(mat[0])
        self.LR, self.LC = self.n.bit_length(), self.m.bit_length()
        self.sp = [[None] * self.LC for _ in range(self.LR)]
        self.sp[0][0] = [row[:] for row in mat]
        for j in range(1, self.LC):
            prev, cur = self.sp[0][j - 1], [[0] * self.m for _ in range(self.n)]
            span = 1 << (j - 1)
            for r in range(self.n):
                for c in range(self.m - (1 << j) + 1):
                    cur[r][c] = self.f(prev[r][c], prev[r][c + span])
            self.sp[0][j] = cur
        for i in range(1, self.LR):
            span = 1 << (i - 1)
            for j in range(self.LC):
                prev, cur = self.sp[i - 1][j], [[0] * self.m for _ in range(self.n)]
                for r in range(self.n - (1 << i) + 1):
                    for c in range(self.m):
                        cur[r][c] = self.f(prev[r][c], prev[r + span][c])
                self.sp[i][j] = cur

    def query(self, r1, c1, r2, c2):
        kr = (r2 - r1 + 1).bit_length() - 1
        kc = (c2 - c1 + 1).bit_length() - 1
        rr, cc = r2 - (1 << kr) + 1, c2 - (1 << kc) + 1
        f = self.f
        return f(f(self.sp[kr][kc][r1][c1], self.sp[kr][kc][r1][cc]),
                 f(self.sp[kr][kc][rr][c1], self.sp[kr][kc][rr][cc]))


class Solution:
    def submatrix_spreads(self, grid, queries):
        hi = SparseTable2D(grid, max)
        lo = SparseTable2D(grid, min)
        return [hi.query(r1, c1, r2, c2) - lo.query(r1, c1, r2, c2)
                for r1, c1, r2, c2 in queries]
```

- **Precompute:** O(n·m·log n·log m) for each of the two tables.
- **Query:** O(1) each (two lookups + subtraction).
- **Space:** O(n·m·log n·log m) — doubled for two tables.

## Key Insights & Edge Cases

- **Two tables, not one.** You cannot derive `min` from a `max` table (or vice
  versa) for arbitrary rectangles, so maintain both.
- **Uniform rectangle** (all equal values) → spread `0`; single cell → spread
  `0`.
- **Negative values** are fine; the subtraction of two same-signed-or-mixed
  values is still the correct nonnegative spread since `max >= min` always.
- **Memory-tight variants** can build both tables from a single doubling loop
  that stores pairs `(mn, mx)` per block, halving Python object overhead.
- This "combine several idempotent statistics" trick generalizes: any tuple of
  idempotent aggregates (max, min, gcd, and, or) can ride along on the same
  block structure.
