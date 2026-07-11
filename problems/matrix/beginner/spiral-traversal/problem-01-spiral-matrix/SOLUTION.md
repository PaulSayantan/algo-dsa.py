# Solution — Spiral Matrix

## Brute Force

A "simulation with a visited grid" approach also works and is a reasonable first
idea: keep a boolean `visited` matrix, start at `(0, 0)` heading right, and step
forward; whenever the next cell is out of bounds or already visited, turn
clockwise (right -> down -> left -> up). Stop after collecting `m * n` cells.

- **Time:** `O(m * n)` — each cell is processed once.
- **Space:** `O(m * n)` for the `visited` grid (on top of the output).

This is correct but uses extra memory that the boundary method avoids.

## Optimal Approach (Spiral Traversal)

Maintain four boundaries that describe the un-visited sub-rectangle:

- `top` — first un-visited row (starts at `0`)
- `bottom` — last un-visited row (starts at `m - 1`)
- `left` — first un-visited column (starts at `0`)
- `right` — last un-visited column (starts at `n - 1`)

Each iteration of the outer loop peels off one ring in four directed passes,
shrinking the appropriate boundary after each pass:

1. Left -> right along row `top`, then `top += 1`.
2. Top -> bottom along column `right`, then `right -= 1`.
3. Right -> left along row `bottom` (only if `top <= bottom`), then `bottom -= 1`.
4. Bottom -> top along column `left` (only if `left <= right`), then `left += 1`.

Continue while `top <= bottom` **and** `left <= right`.

**Why the extra guards matter:** for non-square matrices, after the first two
passes it is possible that `top > bottom` (all rows consumed) or
`left > right` (all columns consumed). Without the `if` checks on passes 3 and 4
you would re-emit a row or column. The guards make the method correct for thin
`1 x n` and `m x 1` matrices too.

```python
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []
    while top <= bottom and left <= right:
        for col in range(left, right + 1):        # top row, left -> right
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):        # right col, top -> bottom
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:                         # bottom row, right -> left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:                         # left col, bottom -> top
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result
```

- **Time:** `O(m * n)` — each cell appended exactly once.
- **Space:** `O(1)` extra beyond the output list.

## Key Insights & Edge Cases

- **Fixed direction cycle.** Directions never change order: right, down, left,
  up. Only the boundaries move.
- **The two guards are essential**, not decorative. Test with a single row
  `[[1, 2, 3, 4]]` (should give `[1, 2, 3, 4]`) and a single column
  `[[1], [2], [3]]` (should give `[1, 2, 3]`). Both hit the guard branches.
- **Single element** `[[7]]`: the top-row pass emits `7`, then `top` exceeds
  `bottom` and the loop ends.
- **Off-by-one care** in the reverse ranges: `range(right, left - 1, -1)` and
  `range(bottom, top - 1, -1)` must include the endpoint columns/rows.
- Total elements collected always equals `m * n`; you can assert this while
  debugging.
