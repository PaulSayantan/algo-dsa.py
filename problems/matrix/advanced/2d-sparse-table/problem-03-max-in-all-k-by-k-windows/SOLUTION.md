# Solution — Maximum in Every k×k Window

## Brute Force

For each of the `(n-k+1)·(m-k+1)` windows, scan all `k²` cells for the max.

- **Time:** O(n·m·k²). For `n = m = 500` and `k = 250` this is ~`10^10`
  operations.
- **Space:** O(1) extra (besides the output).

## Optimal Approach — 2D Sparse Table

Every window is a `k x k` **square submatrix**, and `max` is idempotent, so a
2D Sparse Table for `max` answers each window in O(1).

A neat simplification: because every query has the **same** side length `k`, the
block exponents are constant, `kr = kc = floor(log2(k))`. The window
`[i, i+k-1] x [j, j+k-1]` is covered by the four `2^kr x 2^kr` blocks anchored at
its corners, so we can even precompute a single "max over `2^kr x 2^kr` block"
grid and read it four times per window.

### Steps

1. Build `sp[i][j][r][c]` = max over the `2^i x 2^j` block at `(r, c)`.
2. Let `p = floor(log2(k))` so `2^p <= k`.
3. For each valid `(i, j)`, query the window `(i, j)-(i+k-1, j+k-1)`:
   ```
   rr = i + k - 2^p        cc = j + k - 2^p
   result[i][j] = max( sp[p][p][i][j],  sp[p][p][i][cc],
                       sp[p][p][rr][j], sp[p][p][rr][cc] )
   ```

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
    def max_in_k_windows(self, grid, k):
        n, m = len(grid), len(grid[0])
        st = SparseTable2D(grid, max)
        return [[st.query(i, j, i + k - 1, j + k - 1)
                 for j in range(m - k + 1)]
                for i in range(n - k + 1)]
```

- **Precompute:** O(n·m·log n·log m).
- **All windows:** O((n-k+1)·(m-k+1)) = O(n·m) queries, each O(1).
- **Space:** O(n·m·log n·log m).

## Key Insights & Edge Cases

- **Fixed side length** means every query shares `kr = kc = floor(log2(k))`;
  only one `(kr, kc)` layer of the table is ever read.
- **`k = 1`** returns the grid unchanged (each window is a single cell).
- **`k = min(n, m)`** may yield a single-row or single-column output; the corner
  formula still works because the four blocks collapse appropriately.
- **`k` not a power of two** is the whole point of overlapping blocks: e.g. for
  `k = 3`, `2^p = 2` and the two blocks per axis overlap by one, which is fine
  for `max`.
- If you only ever need this one `k`, a monotonic-deque sliding window computes
  all maxima in O(n·m) without the log factors — reach for the sparse table when
  you also need arbitrary rectangle queries.
