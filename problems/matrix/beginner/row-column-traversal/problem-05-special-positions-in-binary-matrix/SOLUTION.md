# Solution — Special Positions in a Binary Matrix

## Brute Force

For every cell that holds a 1, scan its entire row and its entire column to confirm no
other 1 exists.

```python
def numSpecial(self, mat):
    m, n = len(mat), len(mat[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                row_ones = sum(mat[i])                       # scan row i
                col_ones = sum(mat[k][j] for k in range(m))  # scan column j
                if row_ones == 1 and col_ones == 1:
                    count += 1
    return count
```

- **Time:** O(m * n * (m + n)) — each 1 triggers an O(m + n) rescan.
- **Space:** O(1) beyond the input.

## Optimal Approach (Row/Column Traversal)

Precompute all row sums and all column sums in one traversal, then decide each cell in
a second traversal using those cached sums — no repeated rescans.

1. **Aggregate pass:** walk every cell once, adding its value to `row_sum[i]` and to
   `col_sum[j]`.
2. **Decision pass:** walk every cell again; a position is special exactly when
   `mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1`.

```python
def numSpecial(self, mat):
    m, n = len(mat), len(mat[0])
    row_sum = [0] * m
    col_sum = [0] * n
    for i in range(m):              # aggregate pass
        for j in range(n):
            row_sum[i] += mat[i][j]
            col_sum[j] += mat[i][j]

    count = 0
    for i in range(m):              # decision pass
        for j in range(n):
            if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                count += 1
    return count
```

**Why it is correct:** Since entries are 0 or 1, `row_sum[i]` is the count of 1s in row
`i` and `col_sum[j]` is the count of 1s in column `j`. A cell is special iff it is a 1
that is the *only* 1 in its row and the *only* 1 in its column — precisely the condition
`mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1`. Caching the sums makes each
per-cell test O(1).

**Step by step** on `[[1,0,0],[0,0,1],[1,0,0]]`:

1. Aggregate: `row_sum = [1, 1, 1]`, `col_sum = [2, 0, 1]`.
2. Decision: the 1 at `(0,0)` has `col_sum[0] == 2` (reject); the 1 at `(1,2)` has
   `row_sum[1] == 1` and `col_sum[2] == 1` (accept); the 1 at `(2,0)` has
   `col_sum[0] == 2` (reject).
3. Count `= 1`.

- **Time:** O(m * n) — two full traversals.
- **Space:** O(m + n) for the two sum arrays.

## Key Insights & Edge Cases

- The binary constraint lets a plain **sum** double as a **count of 1s**; recognizing
  this converts an O(m * n * (m + n)) brute force into O(m * n).
- Both conditions must hold: a 1 that is unique in its row but shares its column is not
  special (and vice versa). Test row sum *and* column sum.
- Cells holding 0 are never special; short-circuit on `mat[i][j] == 1` first.
- The identity matrix is the maximal case: every diagonal 1 is special, giving `min(m,
  n)` special positions.
- An all-zero matrix has no special positions; the loops naturally return 0.
