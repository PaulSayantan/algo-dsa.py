# Solution — Largest Uniform Square

## Brute Force

Try every side length `L` from `1` to `min(n, m)`; for each `L`, scan every
`L x L` window cell-by-cell to compute its spread and check `<= D`.

- **Time:** O(min(n,m) · n · m · L²) in the naive form — astronomically slow for
  `n = m = 500`.
- **Space:** O(1) extra.

Even a smarter per-`L` scan that recomputes each window from scratch is
O(min(n,m) · n · m · L²); we need the window spread in O(1).

## Optimal Approach — 2D Sparse Tables + Binary Search

Two ideas combine:

1. **O(1) window spread.** Build a 2D Sparse Table for `max` and one for `min`.
   For any square window the spread is `maxQuery − minQuery`, both O(1).
2. **Monotonic feasibility.** If *some* `L x L` uniform square exists, then a
   smaller square inside it is also uniform — feasibility is monotone
   decreasing in `L`. So define `feasible(L)` = "does any `L x L` window have
   spread `<= D`?" It is `True` for all `L` up to some threshold and `False`
   above it. **Binary search** for the largest feasible `L`.

### `feasible(L)`

Iterate over every top-left corner `(i, j)` with `0 <= i <= n-L`,
`0 <= j <= m-L`. Compute the window spread with the two tables; return `True`
as soon as one window has spread `<= D`.

- Cost: O((n-L+1)(m-L+1)) = O(n·m) per check.

### Binary search

Search `L` in `[1, min(n, m)]`. Each step calls `feasible(mid)`. Total
O(n·m·log(min(n,m))) after the O(n·m·log n·log m) precompute.

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
    def largest_uniform_square(self, grid, D):
        n, m = len(grid), len(grid[0])
        hi = SparseTable2D(grid, max)
        lo = SparseTable2D(grid, min)

        def feasible(L):
            for i in range(n - L + 1):
                for j in range(m - L + 1):
                    r2, c2 = i + L - 1, j + L - 1
                    if hi.query(i, j, r2, c2) - lo.query(i, j, r2, c2) <= D:
                        return True
            return False

        lo_L, hi_L, best = 1, min(n, m), 1
        while lo_L <= hi_L:
            mid = (lo_L + hi_L) // 2
            if feasible(mid):
                best = mid
                lo_L = mid + 1
            else:
                hi_L = mid - 1
        return best
```

- **Precompute:** O(n·m·log n·log m) (two tables).
- **Search:** O(n·m·log(min(n,m))) — each of `~log(min(n,m))` checks is O(n·m).
- **Space:** O(n·m·log n·log m).

## Key Insights & Edge Cases

- **Monotonicity is what unlocks binary search.** Any square contained in a
  uniform square is itself uniform (its max is no larger, its min no smaller),
  so `feasible` never flips back from `False` to `True` as `L` grows.
- **Answer is always `>= 1`** because a single cell has spread `0 <= D`.
- **`D = 0`** asks for the largest square whose cells are all identical.
- **`D` very large** (`>=` global spread) makes the whole `min(n, m)` square
  feasible → answer `min(n, m)`.
- **Early exit** inside `feasible` (return on the first qualifying window) makes
  the practical running time much better than the worst-case bound.
- Watch integer ranges: values up to `10^9` and `D` up to `2·10^9` fit in
  Python ints natively; in fixed-width languages use 64-bit types for the
  subtraction.
