# Solution — Submatrix Minimum Query

## Brute Force

For each query, scan every cell of the rectangle and track the running minimum.

- **Time:** O(q · n · m) — up to `2·10^5 · 500 · 500 = 5·10^10` cell visits in
  the worst case, far too slow.
- **Space:** O(1) extra.

A 2D prefix array does **not** help here: prefix sums rely on subtraction to
"remove" the region outside the rectangle, but `min` has no inverse, so you
cannot subtract a min back out.

## Optimal Approach — 2D Sparse Table

`min` is **idempotent**: `min(x, x) = x`. That means a range may be covered by
overlapping blocks without corrupting the answer, which is exactly what a sparse
table exploits.

### Precompute

Define `sp[i][j][r][c]` = the minimum over the block of height `2^i` and width
`2^j` whose top-left corner is `(r, c)`.

Build it in two nested doublings:

1. **Base:** `sp[0][0] = grid` (a `1 x 1` block is just the cell).
2. **Grow width** (fix height `2^0`): for `j = 1 .. log m`,
   `sp[0][j][r][c] = min(sp[0][j-1][r][c], sp[0][j-1][r][c + 2^(j-1)])`.
3. **Grow height** (for every width power `j`): for `i = 1 .. log n`,
   `sp[i][j][r][c] = min(sp[i-1][j][r][c], sp[i-1][j][r + 2^(i-1)][c])`.

### Query `(r1, c1, r2, c2)`

Let `kr = floor(log2(r2 - r1 + 1))` and `kc = floor(log2(c2 - c1 + 1))`.
Cover the rectangle with four `2^kr x 2^kc` blocks anchored at the four corners:

```
rr = r2 - 2^kr + 1
cc = c2 - 2^kc + 1
answer = min( sp[kr][kc][r1][c1], sp[kr][kc][r1][cc],
              sp[kr][kc][rr][c1], sp[kr][kc][rr][cc] )
```

The four blocks together cover exactly the rectangle; any overlap is absorbed
by idempotency, so the result is correct.

### Reference implementation

```python
from typing import List, Callable


class SparseTable2D:
    def __init__(self, mat: List[List[int]], func: Callable[[int, int], int]):
        self.f = func
        self.n, self.m = len(mat), len(mat[0])
        self.LR = self.n.bit_length()   # rows: powers 0 .. LR-1
        self.LC = self.m.bit_length()   # cols: powers 0 .. LC-1
        self.sp = [[None] * self.LC for _ in range(self.LR)]
        self.sp[0][0] = [row[:] for row in mat]
        # widen (height 2^0)
        for j in range(1, self.LC):
            prev, cur = self.sp[0][j - 1], [[0] * self.m for _ in range(self.n)]
            span = 1 << (j - 1)
            for r in range(self.n):
                for c in range(self.m - (1 << j) + 1):
                    cur[r][c] = self.f(prev[r][c], prev[r][c + span])
            self.sp[0][j] = cur
        # heighten (every width power)
        for i in range(1, self.LR):
            span = 1 << (i - 1)
            for j in range(self.LC):
                prev, cur = self.sp[i - 1][j], [[0] * self.m for _ in range(self.n)]
                for r in range(self.n - (1 << i) + 1):
                    for c in range(self.m):
                        cur[r][c] = self.f(prev[r][c], prev[r + span][c])
                self.sp[i][j] = cur

    def query(self, r1: int, c1: int, r2: int, c2: int) -> int:
        kr = (r2 - r1 + 1).bit_length() - 1
        kc = (c2 - c1 + 1).bit_length() - 1
        rr, cc = r2 - (1 << kr) + 1, c2 - (1 << kc) + 1
        a = self.sp[kr][kc][r1][c1]
        b = self.sp[kr][kc][r1][cc]
        c = self.sp[kr][kc][rr][c1]
        d = self.sp[kr][kc][rr][cc]
        return self.f(self.f(a, b), self.f(c, d))


class Solution:
    def submatrix_minimums(self, grid, queries):
        st = SparseTable2D(grid, min)
        return [st.query(r1, c1, r2, c2) for r1, c1, r2, c2 in queries]
```

- **Precompute time:** O(n·m·log n·log m).
- **Query time:** O(1) each, O(q) total.
- **Space:** O(n·m·log n·log m).

## Key Insights & Edge Cases

- **Idempotency is mandatory.** This works for `min`/`max`/`gcd`/AND/OR but is
  wrong for `sum` (overlaps would be double-counted).
- **Log floor via bit tricks.** `x.bit_length() - 1 == floor(log2(x))` for
  `x >= 1`; a query side length is always `>= 1`, so this is safe.
- **Single cell / single row / single column** are handled uniformly: when a
  side length is `1`, `k = 0` and the four corner blocks collapse onto the same
  `1 x 1` block.
- **Negative values** are fine — the operation never assumes non-negativity.
- **Memory budget.** For `n = m = 500`, `log` is ~9 in each dimension, so the
  table holds roughly `500·500·9·9 ≈ 2·10^7` ints — acceptable, but store only
  the widths/heights that actually fit if memory is tight.
