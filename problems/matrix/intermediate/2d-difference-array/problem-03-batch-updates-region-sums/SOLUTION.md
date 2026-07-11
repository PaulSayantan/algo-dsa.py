# Solution — Batch Updates and Region Sums

## Brute Force

Apply each update cell-by-cell, then answer each query by scanning its
rectangle.

```python
for r1, c1, r2, c2, v in updates:
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            mat[x][y] += v

ans = []
for r1, c1, r2, c2 in queries:
    s = 0
    for x in range(r1, r2 + 1):
        for y in range(c1, c2 + 1):
            s += mat[x][y]
    ans.append(s)
```

- **Time:** `O((U + Q) * m * n)` in the worst case — with `U, Q` up to `10^5`
  and `m*n` up to `10^6`, hopelessly slow.
- **Space:** `O(m*n)`.

## Optimal Approach (2D Difference Array, then 2D Prefix Sum)

Two independent classic tricks compose perfectly here because the problem is
**offline** (all updates precede all queries):

### Phase 1 — apply updates with a 2D difference array

Record every rectangle range-add in `O(1)` using four corner deltas on a
`(m+1) x (n+1)` diff matrix:

```
diff[r1  ][c1  ] += v
diff[r2+1][c1  ] -= v
diff[r1  ][c2+1] -= v
diff[r2+1][c2+1] += v
```

Then a 2D prefix sum over `diff` reconstructs the final matrix `mat`.

### Phase 2 — answer queries with a 2D prefix-sum table

Build a `(m+1) x (n+1)` table `P` where `P[i][j]` is the sum of `mat` over rows
`< i` and columns `< j`:

```
P[i+1][j+1] = mat[i][j] + P[i][j+1] + P[i+1][j] - P[i][j]
```

Any rectangle sum `(r1,c1)`–`(r2,c2)` is then answered in `O(1)` by
inclusion–exclusion:

```
sum = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

Note the elegant symmetry: Phase 1 is the *inverse* operation of Phase 2 — the
difference array "spreads" corner deltas into a matrix, and the prefix sum
"collapses" a matrix back into cumulative corners.

### Reference implementation

```python
def batch_updates_region_sums(m, n, updates, queries):
    diff = [[0] * (n + 1) for _ in range(m + 1)]
    for r1, c1, r2, c2, v in updates:          # O(1) per update
        diff[r1][c1]         += v
        diff[r2 + 1][c1]     -= v
        diff[r1][c2 + 1]     -= v
        diff[r2 + 1][c2 + 1] += v

    # reconstruct mat via 2D prefix sum over diff
    mat = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            top    = diff[i - 1][j] if i else 0
            left   = diff[i][j - 1] if j else 0
            corner = diff[i - 1][j - 1] if (i and j) else 0
            diff[i][j] += top + left - corner
            mat[i][j] = diff[i][j]

    # build 2D prefix-sum table P (1-indexed padding)
    P = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            P[i + 1][j + 1] = mat[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]

    ans = []
    for r1, c1, r2, c2 in queries:             # O(1) per query
        ans.append(P[r2 + 1][c2 + 1] - P[r1][c2 + 1]
                   - P[r2 + 1][c1] + P[r1][c1])
    return ans
```

- **Time:** `O(U + m*n + Q)` — updates and queries are each `O(1)`, plus two
  grid sweeps.
- **Space:** `O(m*n)` for the diff matrix and the prefix-sum table.

## Key Insights & Edge Cases

- This only works because it is **offline**. If queries were interleaved with
  updates, you'd need a 2D Fenwick (BIT) or segment tree supporting both
  operations in `O(log m * log n)`.
- **Negative `v`** is fine; the difference array is purely additive.
- Use padded (`+1`) dimensions in *both* phases so the `r2+1`/`c2+1` writes and
  the prefix-sum lookups never go out of bounds.
- **Empty batches:** zero updates leaves the matrix all zeros; zero queries
  returns an empty list.
- Sums can be large (up to `~10^6 cells * 10^4` per cell after many updates), so
  in languages with fixed-width integers use 64-bit; Python integers are
  unbounded.
- Do not confuse the two tables: the difference array is written at
  `(r2+1, c2+1)` corners (**inverse**), whereas the prefix-sum query reads at
  `(r2+1, c2+1)` corners (**forward**).
