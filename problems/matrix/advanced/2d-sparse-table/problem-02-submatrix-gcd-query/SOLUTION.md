# Solution — Submatrix GCD Query

## Brute Force

For each query, fold `gcd` over every cell of the rectangle.

- **Time:** O(q · n · m · log V), where `V` is the max value (each `gcd` step is
  `O(log V)`). With `q = 2·10^5` and `n = m = 400`, this is far too slow.
- **Space:** O(1) extra.

## Optimal Approach — 2D Sparse Table

`gcd` is **idempotent** (`gcd(x, x) = x`), **associative**, and **commutative**,
so overlapping blocks may be combined without changing the result — the exact
property a sparse table needs. The construction is identical to the min case;
only the merge function changes.

### Precompute

`sp[i][j][r][c]` = gcd over the `2^i x 2^j` block anchored at `(r, c)`.

1. `sp[0][0] = grid`.
2. Widen: `sp[0][j][r][c] = gcd(sp[0][j-1][r][c], sp[0][j-1][r][c + 2^(j-1)])`.
3. Heighten: `sp[i][j][r][c] = gcd(sp[i-1][j][r][c], sp[i-1][j][r + 2^(i-1)][c])`.

### Query

Identical corner formula as the min problem, using `kr`/`kc` = floor log2 of the
side lengths and folding the four corner blocks with `gcd`:

```
answer = gcd( gcd(sp[kr][kc][r1][c1], sp[kr][kc][r1][cc]),
              gcd(sp[kr][kc][rr][c1], sp[kr][kc][rr][cc]) )
```

### Reference implementation

```python
from math import gcd
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
    def submatrix_gcds(self, grid, queries):
        st = SparseTable2D(grid, gcd)
        return [st.query(r1, c1, r2, c2) for r1, c1, r2, c2 in queries]
```

- **Precompute:** O(n·m·log n·log m) merges, each `O(log V)`.
- **Query:** O(1) merges (three `gcd` calls) → effectively `O(log V)` per query.
- **Space:** O(n·m·log n·log m).

## Key Insights & Edge Cases

- **Why gcd works but sum does not.** `gcd` is idempotent, so double-covering a
  cell is harmless. `sum` is not, so a sparse table would over-count overlaps.
- **`gcd` with equal inputs** returns that input, which is why the overlapping
  four-block cover is valid.
- **All values equal `v`** → every query returns `v`. **Any pair that is
  coprime** in a rectangle forces that rectangle's gcd to `1`.
- **Single cell** returns the cell itself (`k = 0` in both dimensions).
- Use `math.gcd`; it runs in `O(log(min(a, b)))` and handles large values
  cleanly.
