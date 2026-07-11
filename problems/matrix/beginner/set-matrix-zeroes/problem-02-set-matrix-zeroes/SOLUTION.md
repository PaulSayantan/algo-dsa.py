# Solution — Set Matrix Zeroes

## Brute Force

Two safe brute-force strategies exist; the *naive* in-place scan does **not**
work.

**Broken naive attempt:** scanning the matrix and immediately zeroing rows/cols
as you find zeros. The freshly written zeros are re-read as if they were
original zeros, so the zeroing cascades and destroys the matrix. Do not do this.

**Correct brute force with extra space:** remember which rows and columns
contain a zero, then apply.

```python
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    rows, cols = set(), set()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(m):
        for j in range(n):
            if i in rows or j in cols:
                matrix[i][j] = 0
```

- **Time:** `O(m·n)`.
- **Space:** `O(m + n)` for the two sets.

## Optimal Approach (First Row/Column as Flags)

**Idea:** we still need one flag per row and one per column, but we already own
`m + n` cells that can hold those flags — the matrix's own first row and first
column. The only wrinkle is that cell `(0,0)` would have to store *both* the
"row 0 has a zero" and "column 0 has a zero" flags, so we split those two out
into standalone booleans.

### Step by step

1. **Record the border separately.** Scan the first row; set
   `first_row_zero = True` if any cell there is `0`. Scan the first column; set
   `first_col_zero = True` similarly. These two booleans are our only extra
   space.
2. **Mark using the border.** For every interior cell `(i, j)` with `i >= 1` and
   `j >= 1`, if `matrix[i][j] == 0`, write the flags into the border:
   `matrix[i][0] = 0` (mark row `i`) and `matrix[0][j] = 0` (mark column `j`).
3. **Zero the interior from the flags.** For every interior cell `(i, j)`, set
   it to `0` if its row flag `matrix[i][0] == 0` **or** its column flag
   `matrix[0][j] == 0`.
4. **Zero the first row** if `first_row_zero` is `True`.
5. **Zero the first column** if `first_col_zero` is `True`.

```python
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
```

### Why it is correct

- **Ordering is everything.** We compute `first_row_zero` / `first_col_zero`
  *before* the marking loop, because the marking loop will overwrite border
  cells and we would otherwise lose the original border information.
- **The interior is written last, from flags.** Steps 2 and 3 only read the
  border flags, never a freshly zeroed interior cell, so the cascade bug from
  the naive approach cannot happen.
- **The border is applied at the very end.** If we zeroed row 0 / column 0
  before finishing the interior, we would corrupt the flags that the interior
  still depends on. Doing it last means every interior decision has already been
  made.

### Complexity

- **Time:** `O(m·n)` — a constant number of passes over the grid.
- **Space:** `O(1)` extra — just the two boolean scalars.

## Key Insights & Edge Cases

- **Why `(0,0)` needs two booleans:** cell `(0,0)` is simultaneously the flag
  for row 0 and column 0. One cell cannot faithfully carry two independent
  flags, so we lift them into `first_row_zero` and `first_col_zero`.
- **Single row / single column:** `m == 1` or `n == 1` collapses the entire grid
  into the "border," which is exactly why we handle the border with dedicated
  booleans. Example 3 (`[[1,2,3]]`) has no zeros so nothing changes.
- **A zero already on the border:** correctly captured by the `first_row_zero` /
  `first_col_zero` scan in step 1, and the border is zeroed in steps 4–5.
- **Don't mutate the return value:** the function returns `None`; all changes
  are in place.
