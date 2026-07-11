# Solution — Range Sum Query 2D - Immutable

## Brute Force

For each `sumRegion` query, loop over every cell in the requested rectangle and
add them up.

```python
def sumRegion(self, r1, c1, r2, c2):
    total = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            total += self.matrix[i][j]
    return total
```

- **Time:** O(m * n) per query, O(q * m * n) for `q` queries.
- **Space:** O(1) extra.

With up to `10^4` queries on a `200 x 200` grid this is `4 * 10^8` operations —
too slow, and it wastes the fact that the matrix never changes.

## Optimal Approach — 2D Prefix Sum (Integral Image)

Build a padded prefix table `P` of size `(m+1) x (n+1)` **once** in the
constructor, where

```
P[i][j] = sum of matrix[r][c] for all 0 <= r < i and 0 <= c < j
```

Row 0 and column 0 of `P` are all zeros. This padding removes every boundary
special case.

### Build (each cell in O(1))

```
P[i][j] = matrix[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
```

We add the sum of the rectangle above (`P[i-1][j]`) and the rectangle to the
left (`P[i][j-1]`). Those two overlap in the top-left block `P[i-1][j-1]`, which
we counted twice, so we subtract it once.

### Query (O(1) via inclusion-exclusion)

For rows `r1..r2` and columns `c1..c2` (inclusive):

```
sum = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

`P[r2+1][c2+1]` is the whole rectangle from the origin to the bottom-right
corner of the target. We subtract the horizontal strip above the target
(`P[r1][c2+1]`) and the vertical strip to its left (`P[r2+1][c1]`). The
top-left corner block `P[r1][c1]` was removed twice, so we add it back once.

### Why it is correct

Each `P[i][j]` is defined as a genuine prefix sum. The build recurrence is exact
inclusion-exclusion over the three previously-computed rectangles, and the query
formula is the same inclusion-exclusion applied to isolate an arbitrary
rectangle. Because addition is associative and has an inverse (subtraction), the
overlaps cancel exactly.

### Reference implementation

```python
class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.P[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.P[i - 1][j]
                    + self.P[i][j - 1]
                    - self.P[i - 1][j - 1]
                )

    def sumRegion(self, r1, c1, r2, c2):
        P = self.P
        return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]
```

- **Build time:** O(m * n). **Query time:** O(1). **Space:** O(m * n).

## Key Insights & Edge Cases

- **Padding by one row and column** is the trick that keeps the build and query
  formulas branch-free; without it you must special-case `r1 == 0` / `c1 == 0`.
- The `+1` offsets are the most common bug: the query uses `r2+1`, `c2+1` for the
  far corner but `r1`, `c1` (no offset) for the near corner.
- **Single-cell query** (`r1 == r2`, `c1 == c2`) must return exactly
  `matrix[r1][c1]`; the formula handles this automatically.
- Negative values are fine — nothing in the derivation assumes non-negativity.
- Watch for integer overflow in languages with fixed-width ints:
  `200 * 200 * 10^4 = 4 * 10^8` fits in 64-bit but not 32-bit. Python is safe.
