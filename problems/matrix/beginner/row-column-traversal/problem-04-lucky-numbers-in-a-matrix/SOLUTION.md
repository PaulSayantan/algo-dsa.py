# Solution — Lucky Numbers in a Matrix

## Brute Force

For every cell, check whether it is the minimum of its row *and* the maximum of its
column by scanning the whole row and the whole column each time.

```python
def luckyNumbers(self, matrix):
    m, n = len(matrix), len(matrix[0])
    result = []
    for i in range(m):
        for j in range(n):
            v = matrix[i][j]
            is_row_min = all(v <= matrix[i][k] for k in range(n))
            is_col_max = all(v >= matrix[k][j] for k in range(m))
            if is_row_min and is_col_max:
                result.append(v)
    return result
```

- **Time:** O(m * n * (m + n)) — each of `m * n` cells triggers an O(m + n) rescan.
- **Space:** O(1) beyond the output.

## Optimal Approach (Row/Column Traversal)

Precompute the two summaries in two clean traversals, then intersect them.

1. **Row pass:** for each row, take its minimum. Collect these into a set
   `row_mins`.
2. **Column pass:** for each column, take its maximum. Collect these into a set
   `col_maxes`.
3. Any number appearing in both sets is lucky.

```python
def luckyNumbers(self, matrix):
    row_mins = {min(row) for row in matrix}          # one min per row
    m, n = len(matrix), len(matrix[0])
    col_maxes = {max(matrix[i][j] for i in range(m)) # one max per column
                 for j in range(n)}
    return list(row_mins & col_maxes)
```

**Why it is correct:** A value is lucky exactly when it equals the minimum of its own
row and the maximum of its own column. `row_mins` holds every row minimum and
`col_maxes` holds every column maximum, so their intersection is precisely the set of
lucky numbers. Because all entries are distinct, membership is unambiguous — no two
cells share a value, so a matched value pins down a single cell.

There can be **at most one** lucky number in the whole matrix. If two cells `(r1, c1)`
and `(r2, c2)` were both lucky, comparing `matrix[r1][c1]`, `matrix[r1][c2]`,
`matrix[r2][c2]`, `matrix[r2][c1]` yields a contradiction — so the result list has
length 0 or 1.

**Step by step** on `[[7,8],[1,2]]`:

1. Row minimums: `min(7,8)=7`, `min(1,2)=1` -> `row_mins = {7, 1}`.
2. Column maximums: col 0 `max(7,1)=7`, col 1 `max(8,2)=8` -> `col_maxes = {7, 8}`.
3. Intersection `{7, 1} & {7, 8} = {7}` -> return `[7]`.

- **Time:** O(m * n) — the row pass and the column pass each touch every cell once.
- **Space:** O(m + n) for the two summary sets.

## Key Insights & Edge Cases

- Turning an O(m * n * (m + n)) brute force into O(m * n) is the whole point: compute
  per-row and per-column summaries *once* instead of rescanning per cell.
- The problem guarantees distinct values, which makes the set intersection exact. With
  duplicates you would instead have to verify the actual `(row, col)` position.
- A `1 x 1` matrix is trivially lucky: its lone element is both the row min and the
  column max.
- Order of the output does not matter, so returning `list(set intersection)` is fine.
