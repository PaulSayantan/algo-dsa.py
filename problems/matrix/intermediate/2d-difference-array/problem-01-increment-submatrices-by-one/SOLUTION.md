# Solution — Increment Submatrices by One

## Brute Force

For each query, loop over every cell of its rectangle and add `1`.

```python
for row1, col1, row2, col2 in queries:
    for x in range(row1, row2 + 1):
        for y in range(col1, col2 + 1):
            mat[x][y] += 1
```

- **Time:** `O(q * n^2)` in the worst case (a full-grid rectangle repeated `q`
  times). With `q = 10^4` and `n = 500` that is `2.5 * 10^9` operations — too
  slow.
- **Space:** `O(n^2)` for the grid.

## Optimal Approach (2D Difference Array)

Instead of touching every cell, record each rectangle as **four corner edits**
in a difference matrix `diff`, then reconstruct the grid with one 2D prefix-sum
sweep.

### Why four corners work

Define `diff` so that the value of `mat[i][j]` equals the 2D prefix sum of
`diff` over all `(x, y)` with `x <= i` and `y <= j`. A `+v` placed at
`diff[r1][c1]` therefore floods the entire lower-right quadrant anchored at
`(r1, c1)`. To confine the flood to the rectangle `(r1,c1)`–`(r2,c2)` we cancel
the overflow past its bottom and right edges using inclusion–exclusion:

```
diff[r1  ][c1  ] += 1   # start the flood
diff[r2+1][c1  ] -= 1   # stop it below the rectangle
diff[r1  ][c2+1] -= 1   # stop it right of the rectangle
diff[r2+1][c2+1] += 1   # add back the doubly-subtracted corner
```

To keep the `r2+1` / `c2+1` indices in range we size `diff` as
`(n + 1) x (n + 1)` and simply ignore the extra row/column at the end.

### Reconstruction

A 2D prefix sum turns the four corner deltas into the actual increments:

```
diff[i][j] += diff[i-1][j] + diff[i][j-1] - diff[i-1][j-1]
```

The subtraction removes the region double-counted by the top and left
neighbours.

### Reference implementation

```python
class Solution:
    def rangeAddQueries(self, n, queries):
        diff = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:      # O(1) per query
            diff[r1][c1]     += 1
            diff[r2 + 1][c1] -= 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        # 2D prefix sum to recover the grid
        for i in range(n):
            for j in range(n):
                top  = diff[i - 1][j] if i else 0
                left = diff[i][j - 1] if j else 0
                corner = diff[i - 1][j - 1] if (i and j) else 0
                diff[i][j] += top + left - corner

        return [row[:n] for row in diff[:n]]
```

- **Time:** `O(q + n^2)` — constant work per query plus one grid-sized sweep.
- **Space:** `O(n^2)` for the difference/answer matrix.

## Key Insights & Edge Cases

- **Pad by one row and column** (`n + 1` each) so the `r2+1` and `c2+1` writes
  never go out of bounds; those padding cells are discarded at the end.
- The four-corner pattern is **inclusion–exclusion**: `+`, `-`, `-`, `+`. Getting
  a sign or index wrong is the classic bug — memorize the top-left `+`,
  bottom-left `-`, top-right `-`, bottom-right `+` layout.
- Works only when all updates happen **before** you read the grid. If point
  queries were interleaved with updates you would need a Fenwick/segment tree
  instead.
- A single-cell rectangle (`r1 == r2 and c1 == c2`) still uses all four corners
  and works correctly.
- Reconstruction can be done **in place** on `diff`; no separate output matrix
  is required.
