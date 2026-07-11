# Solution — Anti-clockwise Spiral Traversal

## Brute Force

Simulate movement with a `visited` grid. Start at `(0, 0)` heading **down**;
whenever the next step is off-grid or already visited, turn counter-clockwise
(down -> right -> up -> left). Collect `m * n` cells.

- **Time:** `O(m * n)`.
- **Space:** `O(m * n)` for the `visited` matrix.

Correct, but the boundary method removes the auxiliary grid.

## Optimal Approach (Spiral Traversal, reversed)

This is the clockwise spiral reflected across the main diagonal. Keep the four
boundaries `top`, `bottom`, `left`, `right`, but reverse both the order of the
four passes and their sweep directions:

1. Top -> bottom along column `left`, then `left += 1`.
2. Left -> right along row `bottom`, then `bottom -= 1`.
3. Bottom -> top along column `right` (only if `left <= right`), then `right -= 1`.
4. Right -> left along row `top` (only if `top <= bottom`), then `top += 1`.

Loop while `top <= bottom` and `left <= right`.

```python
def anticlockwise_spiral_order(matrix):
    if not matrix or not matrix[0]:
        return []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []
    while top <= bottom and left <= right:
        for row in range(top, bottom + 1):        # left col, top -> bottom
            result.append(matrix[row][left])
        left += 1
        for col in range(left, right + 1):        # bottom row, left -> right
            result.append(matrix[bottom][col])
        bottom -= 1
        if left <= right:                         # right col, bottom -> top
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][right])
            right -= 1
        if top <= bottom:                         # top row, right -> left
            for col in range(right, left - 1, -1):
                result.append(matrix[top][col])
            top += 1
    return result
```

**Correctness sketch:** the same peeling argument as the clockwise version
applies — each outer iteration consumes exactly the current outer ring, and the
boundary updates guarantee inner rings are visited on later iterations. The
guards on passes 2–4 stop a row/column being emitted twice once a dimension is
exhausted.

- **Time:** `O(m * n)`.
- **Space:** `O(1)` extra beyond the output.

## Key Insights & Edge Cases

- **Same skeleton, mirrored moves.** If you already have the clockwise routine,
  the anti-clockwise one is a mechanical transformation: swap the roles of rows
  and columns in the direction cycle.
- **Order of the guards is subtle.** The first two passes (left column, bottom
  row) always run once the `while` condition holds; the last two passes (right
  column, top row) each need a guard — `left <= right` before the right-column
  pass and `top <= bottom` before the top-row pass. Miss a guard and thin
  matrices duplicate a line (e.g. the center cell of a 3x3 gets emitted twice).
- **Single column** `[[1], [2], [3]]`: the first pass emits `1, 2, 3`; then
  `left` exceeds `right` and the loop ends — result `[1, 2, 3]`.
- **Single row** `[[1, 2, 3]]`: first pass emits `1` (column `left`), then the
  bottom-row pass emits `2, 3`. Result `[1, 2, 3]`.
- Collected count always equals `m * n`.
