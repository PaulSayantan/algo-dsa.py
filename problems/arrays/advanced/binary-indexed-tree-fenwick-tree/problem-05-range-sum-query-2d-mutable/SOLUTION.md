# Range Sum Query 2D - Mutable — Solution

## Brute Force

Keep the raw matrix. `update` is O(1). `sumRegion` loops over the sub-rectangle and adds
every cell, which is O(m · n) per query.

- **Time:** O(1) per update, O(m · n) per query — up to 200·200 = 4·10⁴ per query, times
  5000 queries ≈ 2·10⁸, borderline and wasteful.
- **Space:** O(m · n).

A 2D prefix-sum table gives O(1) queries but O(m · n) per update (rebuilding the affected
suffix), so again one operation is expensive.

## Optimal Approach (2D Binary Indexed Tree / Fenwick Tree)

Generalize the 1D Fenwick Tree to two dimensions: `tree[i][j]` aggregates a 2D block, and we
walk **both** coordinates by their low bits. A point update loops `i` up by `i & (-i)` and,
for each such `i`, loops `j` up by `j & (-j)`. A prefix query over the rectangle
`[1..r] x [1..c]` loops both coordinates *down* by their low bits.

**2D prefix sum.** Define `prefix(r, c)` = sum of all cells in rows `1..r` and columns
`1..c` (1-based). Then a general rectangle sum uses **inclusion-exclusion**:

```
sumRegion(r1, c1, r2, c2)
  = prefix(r2, c2) - prefix(r1-1, c2) - prefix(r2, c1-1) + prefix(r1-1, c1-1)
```

(with all four indices shifted +1 to convert 0-based inputs to the 1-based tree).

**Point update.** As in 1D, the tree stores deltas. To set `matrix[r][c] = val`, add
`delta = val - vals[r][c]` at that cell and refresh the cache.

**Why it is correct.** Each dimension independently satisfies the 1D Fenwick invariant, so
the nested walks touch exactly the O(log m · log n) tree cells whose 2D responsibility block
covers `(r, c)` (for update) or decompose the prefix rectangle into disjoint blocks (for
query). The four-term inclusion-exclusion isolates the requested rectangle because the sum
is an invertible group operation.

**Reference implementation:**

```python
class NumMatrix:
    def __init__(self, matrix):
        self.m = len(matrix)
        self.n = len(matrix[0]) if self.m else 0
        self.vals = [[0] * self.n for _ in range(self.m)]
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])

    def _add(self, r, c, delta):        # r, c are 1-based
        i = r
        while i <= self.m:
            j = c
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def _prefix(self, r, c):            # sum over rows 1..r, cols 1..c
        s = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                s += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return s

    def update(self, row, col, val):
        delta = val - self.vals[row][col]
        self.vals[row][col] = val
        self._add(row + 1, col + 1, delta)

    def sumRegion(self, row1, col1, row2, col2):
        return (self._prefix(row2 + 1, col2 + 1)
                - self._prefix(row1, col2 + 1)
                - self._prefix(row2 + 1, col1)
                + self._prefix(row1, col1))
```

- **Time:** O(m · n · log m · log n) to build via point updates (or O(m · n) with a linear
  build per row/column); O(log m · log n) per `update` and per `sumRegion`.
- **Space:** O(m · n) for the 2D tree plus O(m · n) for the cached values.

## Key Insights & Edge Cases

- **Nested low-bit walks.** The 2D tree is literally a Fenwick Tree whose cells are Fenwick
  Trees; update walks *up* in both dimensions, query walks *down* in both.
- **Inclusion-exclusion off-by-ones.** In the four-term formula the "minus" terms use
  `row1` / `col1` (i.e. `row1 - 1 + 1`), and only the main term and the corner term add;
  getting a sign or an index wrong is the classic 2D-BIT bug. Verify against
  `prefix(r1, c2+1)` corresponding to rows `1..r1` (0-based `0..r1-1`), which correctly
  excludes the target rectangle's rows.
- **Delta updates.** The tree holds sums, so `update` must add `val - vals[row][col]` and
  keep the `vals` cache in sync — never overwrite a tree cell directly.
- **Empty matrix guard.** Handle `m == 0` or `n == 0` before allocating (constraints here
  guarantee `m, n >= 1`, but defensive code avoids index errors on reuse).
- **Constant factor.** With `m, n <= 200`, `log m · log n <= 8 · 8 = 64` cell touches per
  operation — comfortably fast for 5000 mixed queries.
