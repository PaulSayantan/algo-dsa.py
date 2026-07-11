# Solution — Sum of Boundary Elements

## Brute Force

Scan every cell and add it if it lies on the border:

```python
total = 0
for i in range(m):
    for j in range(n):
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            total += matrix[i][j]
```

This is **correct** (the `or` conditions naturally include each border cell exactly
once, so corners are not double-counted), but it visits all `m * n` cells even though
only the perimeter matters.

- **Time:** `O(m * n)`.
- **Space:** `O(1)`.

## Optimal Approach — Boundary / Perimeter Traversal

Add the full top and bottom rows, then add only the **interior** of the left and right
columns (rows `1 .. m-2`) so corner cells are never added twice.

```python
from typing import List

def boundary_sum(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])

    # Single row: the whole row is the boundary.
    if m == 1:
        return sum(matrix[0])
    # Single column: the whole column is the boundary.
    if n == 1:
        return sum(row[0] for row in matrix)

    total = sum(matrix[0]) + sum(matrix[m - 1])   # full top + full bottom row
    for i in range(1, m - 1):                      # interior rows only
        total += matrix[i][0] + matrix[i][n - 1]   # left edge + right edge
    return total
```

### Why it is correct

- `sum(matrix[0]) + sum(matrix[m-1])` covers both full horizontal edges, which already
  include **all four corners**.
- The loop over `range(1, m-1)` deliberately excludes row `0` and row `m-1`, so when we
  add `matrix[i][0]` (left edge) and `matrix[i][n-1]` (right edge) we only touch the
  *middle* of the vertical edges. No corner is added a second time.
- The `m == 1` and `n == 1` guards handle degenerate shapes where the top/bottom rows or
  left/right columns coincide.

### Step-by-step on Example 1

Matrix `[[1,2,3],[4,5,6],[7,8,9]]`, `m = n = 3`.

1. Top row sum: `1+2+3 = 6`. Bottom row sum: `7+8+9 = 24`. Running total `= 30`.
2. Interior rows `i = 1`: add `matrix[1][0] + matrix[1][2] = 4 + 6 = 10`.
3. Total `= 30 + 10 = 40`. Correct.

### Complexity

- **Time:** `O(m + n)` — top and bottom rows are `O(n)`, the interior column loop is
  `O(m)`.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Corner double-count is the whole difficulty.** Summing "first row + last row + first
  column + last column" as four independent sums adds each corner twice; you would then
  have to subtract the four corners. The interior-column loop avoids that correction.
- **Single row (`m == 1`).** First and last row are the same row; return `sum(matrix[0])`.
- **Single column (`n == 1`).** Left and right column coincide; return the column sum.
- **`1 x 1` matrix.** Handled by the `m == 1` branch: returns the single element.
- **Negative values are fine** — this is a plain arithmetic sum, no assumptions about
  sign.
- Alternative correct formula for `m, n > 1`:
  `sum(matrix[0]) + sum(matrix[-1]) + sum(row[0] + row[-1] for row in matrix[1:-1])`.
