# Solution — Boundary Traversal (Clockwise)

## Brute Force

Walk **every** cell `(i, j)` and keep it only if it lies on the border, i.e.
`i == 0 or i == m - 1 or j == 0 or j == n - 1`. This correctly identifies boundary
cells, but a naive row-major scan does **not** produce clockwise order — you would have
to bucket the cells and stitch the four sides together afterward, which is fiddly and
error-prone.

- **Time:** `O(m * n)` — every interior cell is examined even though it is discarded.
- **Space:** `O(1)` beyond the output.

The waste is obvious: for a `1000 x 1000` matrix we touch ~1,000,000 cells to return
only ~4,000 of them.

## Optimal Approach — Boundary / Perimeter Traversal

Track four edge indices and perform four directed sweeps. Only boundary cells are ever
visited.

```python
from typing import List

def boundary_traversal(matrix: List[List[int]]) -> List[int]:
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m - 1, 0, n - 1
    result: List[int] = []

    # 1) top row, left -> right
    for j in range(left, right + 1):
        result.append(matrix[top][j])

    # 2) right column, top+1 -> bottom
    for i in range(top + 1, bottom + 1):
        result.append(matrix[i][right])

    # 3) bottom row, right-1 -> left  (only if more than one row)
    if top != bottom:
        for j in range(right - 1, left - 1, -1):
            result.append(matrix[bottom][j])

    # 4) left column, bottom-1 -> top+1  (only if more than one column)
    if left != right:
        for i in range(bottom - 1, top, -1):
            result.append(matrix[i][left])

    return result
```

### Why it is correct

- The **top row** sweep covers `matrix[0][0 .. n-1]`, including both top corners.
- The **right column** sweep starts at `top + 1` so the top-right corner is not repeated;
  it covers down to the bottom-right corner.
- The **bottom row** sweep runs right-to-left from `right - 1` (bottom-right already
  emitted) down to `left`, capturing the bottom-left corner. Guarded by `top != bottom`
  so a single-row matrix does not re-emit the row.
- The **left column** sweep runs from `bottom - 1` up to `top + 1`, emitting the interior
  of the left edge. Both corners on this edge were already handled. Guarded by
  `left != right` so a single-column matrix does not re-emit the column.

Together the four sweeps visit each boundary cell exactly once and preserve clockwise
order by construction.

### Step-by-step on Example 1

Matrix `[[1,2,3],[4,5,6],[7,8,9]]`, so `top=0, bottom=2, left=0, right=2`.

1. Top row: `1, 2, 3`.
2. Right column (`i = 1, 2`): `6, 9`.
3. `top != bottom`, bottom row (`j = 1, 0`): `8, 7`.
4. `left != right`, left column (`i = 1`): `4`.

Result: `[1, 2, 3, 6, 9, 8, 7, 4]`. Correct.

### Complexity

- **Time:** `O(m + n)` — exactly `2*(m + n) - 4` cells for `m, n > 1`, or `n` / `m`
  for a single row / column.
- **Space:** `O(1)` beyond the output list.

## Key Insights & Edge Cases

- **Corners are the trap.** The `+1` offsets on sweeps 2–4 exist purely to avoid
  double-counting the four corners.
- **Single row (`m == 1`).** Sweep 1 emits the row; the `top != bottom` guard skips
  sweep 3, and sweep 4's range `range(bottom-1, top, -1)` = `range(-1, 0, -1)` is empty.
  Result is just the row.
- **Single column (`n == 1`).** Sweep 1 emits `matrix[0][0]`, sweep 2 emits the rest of
  the column, and the `left != right` guard skips sweep 4. No element repeats.
- **Single cell (`1 x 1`).** Only sweep 1 runs, emitting the lone element.
- **Empty matrix.** Guard with `if not matrix or not matrix[0]: return []`.
- Using `top != bottom` and `left != right` (rather than `m > 1` / `n > 1`) makes the
  same code reusable for peeling **inner** rings in a spiral, where the effective bounds
  shrink.
