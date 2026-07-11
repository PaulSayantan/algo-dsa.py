# Rotate Matrix Counter-Clockwise — Solution

## Brute Force

Allocate a new `n × n` matrix and place each element at its counter-clockwise
target using the closed-form map: the element at `(i, j)` goes to
`(n-1-j, i)`.

```python
def rotateCounterClockwise(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[n - 1 - j][i] = matrix[i][j]
    matrix[:] = rotated
```

**Time:** `O(n²)`. **Space:** `O(n²)` — builds a second matrix, so it does not
meet the `O(1)` extra-memory goal.

## Optimal Approach (Rotate 90° via transpose + reverse)

Counter-clockwise is the mirror of clockwise. Keep the same transpose pass but
change the reverse: **reverse the order of the rows** rather than reversing each
row.

```python
def rotateCounterClockwise(matrix):
    n = len(matrix)
    # Pass 1: transpose (swap across main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Pass 2: reverse the order of the rows (top <-> bottom)
    matrix.reverse()
```

**Why it is correct:** Transpose maps `(i, j) → (j, i)`. Reversing the row order
sends row `j` to row `n-1-j`, so the element transpose put at `(j, i)` ends at
`(n-1-j, i)`. The composed map `(i, j) → (n-1-j, i)` is exactly a 90°
counter-clockwise rotation. Both passes are bijections, so no cell is lost.

**Alternative order — reverse each row first, then transpose** — also produces a
counter-clockwise rotation:

```python
for row in matrix:
    row.reverse()          # reverse each row first
for i in range(n):         # then transpose
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

**Step by step** on `[[1,2,3],[4,5,6],[7,8,9]]` (transpose then reverse rows):

1. Transpose → `[[1,4,7],[2,5,8],[3,6,9]]`.
2. Reverse row order → `[[3,6,9],[2,5,8],[1,4,7]]`. Correct.

**Time:** `O(n²)`. **Space:** `O(1)` extra — `matrix.reverse()` reorders the
row references without allocating a new grid.

## Key Insights & Edge Cases

- **The only difference from the clockwise rotation is the reverse step.**
  Clockwise reverses *each row*; counter-clockwise reverses the *row order*.
- **Two turns = 180°.** Rotating counter-clockwise twice equals rotating
  clockwise twice: both reverse the row order and reverse each row.
- **`matrix.reverse()` is `O(n)`, not `O(n²)`** — it swaps row references, which
  keeps the whole routine at `O(1)` auxiliary space.
- **`j` starts at `i + 1`** in the transpose to avoid double-swapping.
- `n == 1`: no-op, correctly leaving the single cell unchanged.
