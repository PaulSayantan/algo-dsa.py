# Solution — Print Matrix Anti-Diagonals

## Brute Force

One "brute" way is to physically rotate/shear the matrix so that diagonals become
rows, then read rows. For each of the `m + n - 1` diagonals you could scan the whole
matrix looking for cells with the matching `i + j`.

- **Time:** `O((m + n) * m * n)` — for each diagonal you rescan every cell.
- **Space:** `O(m * n)` for the output.

This works but wastes time re-scanning cells that belong to other diagonals.

## Optimal Approach (Diagonal / Zig-Zag Traversal)

**Key identity:** every cell on the same anti-diagonal shares the value `i + j`.
There are exactly `m + n - 1` distinct sums, from `0` (top-left) to `m + n - 2`
(bottom-right).

Iterate the diagonal id `d` from `0` to `m + n - 2`. For a fixed `d`, if we pick a
row `i`, the column is forced: `j = d - i`. So we only need to sweep `i` over the
rows and keep the cells where `j = d - i` is a legal column (`0 <= j < n`).

```python
def diagonal_order(mat):
    m, n = len(mat), len(mat[0])
    res = []
    for d in range(m + n - 1):          # each anti-diagonal
        for i in range(m):              # choose the row
            j = d - i                   # column is determined
            if 0 <= j < n:
                res.append(mat[i][j])
    return res
```

**Why it is correct.** Because `j = d - i`, iterating `i` in increasing order emits
the cells of diagonal `d` from top (small `i`) to bottom (large `i`), exactly the
required within-diagonal order. Iterating `d` in increasing order visits diagonals
top-left to bottom-right. Every cell `(i, j)` is emitted exactly once, when
`d == i + j`.

**Step-by-step on `[[1,2,3],[4,5,6],[7,8,9]]`:**

| `d` | valid `(i, j)`            | emitted   |
|-----|--------------------------|-----------|
| 0   | (0,0)                    | 1         |
| 1   | (0,1), (1,0)             | 2, 4      |
| 2   | (0,2), (1,1), (2,0)      | 3, 5, 7   |
| 3   | (1,2), (2,1)             | 6, 8      |
| 4   | (2,2)                    | 9         |

Result: `[1, 2, 4, 3, 5, 7, 6, 8, 9]`.

- **Time:** `O(m * n)` — the inner `if` succeeds a total of `m * n` times across all
  diagonals; the total number of `(d, i)` pairs examined is `O((m + n) * m)`, still
  bounded by `O(m * n)` amortized when you tighten the `i` bounds (see below).
- **Space:** `O(1)` auxiliary beyond the output list.

**Tightening the row bounds (optional).** For diagonal `d`, valid rows satisfy
`0 <= d - i < n`, i.e. `max(0, d - n + 1) <= i <= min(m - 1, d)`. Looping `i` only
over that window makes the work exactly `O(m * n)` with no wasted iterations:

```python
for d in range(m + n - 1):
    i_lo = max(0, d - (n - 1))
    i_hi = min(m - 1, d)
    for i in range(i_lo, i_hi + 1):
        res.append(mat[i][d - i])
```

## Key Insights & Edge Cases

- **The `i + j` invariant is the whole trick.** Once you see it, most "diagonal"
  problems reduce to grouping or walking by this key.
- **Single row / single column** matrices: each diagonal holds exactly one element,
  so the output is just the flattened matrix. The formula handles this with no
  special-casing.
- **Direction within a diagonal:** increasing `i` gives top-to-bottom. If a problem
  wants bottom-to-top on some diagonals, reverse that sub-list — that is precisely
  the zig-zag variant (see Problem 2).
- **Off-by-one:** there are `m + n - 1` diagonals, so `d` ranges over
  `range(m + n - 1)`; a common bug is stopping at `m + n - 2` exclusive incorrectly.
