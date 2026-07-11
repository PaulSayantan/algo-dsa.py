# Solution — Increment Submatrices by One

## Brute Force

For each query, loop over every cell of its submatrix and add 1.

```python
def rangeAddQueries(n, queries):
    mat = [[0] * n for _ in range(n)]
    for r1, c1, r2, c2 in queries:
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                mat[x][y] += 1
    return mat
```

- **Time:** `O(Q * n^2)` in the worst case (each query covers the whole matrix).
  With `Q = 10^4` and `n = 500`, that is `2.5 * 10^9` — too slow.
- **Space:** `O(n^2)` for the output.

## Optimal Approach (2D Difference Array)

Generalize the 1D "+ at start, − just past end" idea to a rectangle. To add `1`
to the submatrix `[r1..r2] x [c1..c2]`, place **four** markers in a difference
matrix `diff` (sized `(n + 1) x (n + 1)` so the `+1` boundaries never overflow):

```
diff[r1][c1]     += 1     # turn the increment on at the top-left corner
diff[r1][c2 + 1] -= 1     # turn it off past the right edge
diff[r2 + 1][c1] -= 1     # turn it off past the bottom edge
diff[r2 + 1][c2 + 1] += 1 # re-add the doubly-subtracted bottom-right overlap
```

Think of it as inclusion–exclusion: the top-left `+1` starts an infinite quadrant
of increments; the two `-1`s cancel the parts extending past the right and bottom
edges; the corner `+1` fixes the region subtracted twice.

Then run a **2D prefix sum** over `diff`. The value at `(i, j)` becomes:

```
mat[i][j] = diff[i][j] + mat[i-1][j] + mat[i][j-1] - mat[i-1][j-1]
```

(treating out-of-range indices as 0). That prefix sum inverts the 2D difference,
recovering how many query-rectangles cover each cell.

```python
def rangeAddQueries(n, queries):
    diff = [[0] * (n + 1) for _ in range(n + 1)]
    for r1, c1, r2, c2 in queries:
        diff[r1][c1]         += 1
        diff[r1][c2 + 1]     -= 1
        diff[r2 + 1][c1]     -= 1
        diff[r2 + 1][c2 + 1] += 1

    mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            up   = mat[i - 1][j] if i > 0 else 0
            left = mat[i][j - 1] if j > 0 else 0
            diag = mat[i - 1][j - 1] if i > 0 and j > 0 else 0
            mat[i][j] = diff[i][j] + up + left - diag
    return mat
```

- **Time:** `O(Q + n^2)` — O(Q) to stamp four corners per query, O(n^2) for the
  prefix sum.
- **Space:** `O(n^2)`.

**Why it is correct:** in 2D difference space, a rectangle increment is exactly
the four-corner stamp above (the standard inclusion–exclusion decomposition of a
rectangle into quadrants). The 2D prefix sum is the inverse operator, so
materializing it counts, for every cell, how many query rectangles include it —
identical to the brute-force totals.

## Key Insights & Edge Cases

- **Four corners, mind the signs.** The pattern is `+ − − +` at
  `(r1,c1)`, `(r1,c2+1)`, `(r2+1,c1)`, `(r2+1,c2+1)`. Swapping a sign or a corner
  is the most common mistake — derive it from inclusion–exclusion each time.
- **Padding by one row and column** (size `n + 1`) makes `c2 + 1` and `r2 + 1`
  always writable, even when the query touches the last row/column.
- **The prefix-sum recurrence** subtracts the diagonal `mat[i-1][j-1]` because it
  was added by both the `up` and `left` terms — the same inclusion–exclusion,
  now in the reconstruction step.
- **Full-matrix query** (`[0, 0, n-1, n-1]`) stamps corners at `(0,0)`,
  `(0,n)`, `(n,0)`, `(n,n)`; only `(0,0)` lands inside the real matrix, and the
  prefix sum correctly floods every cell with 1 (see Example 2).
- **In-place option.** You can do the prefix sum directly on the padded `diff`
  and then slice out the top-left `n x n`, saving one allocation.
