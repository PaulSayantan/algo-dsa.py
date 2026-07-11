# Rotate Image (90° Counterclockwise) — Solution

## Brute Force

Allocate a new `n x n` matrix, place each element at its rotated position
`result[n-1-j][i] = matrix[i][j]`, then copy the result back.

```python
def rotateCounterclockwise(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[n - 1 - j][i] = matrix[i][j]
    matrix[:] = result
```

- **Time:** `O(n^2)`.
- **Space:** `O(n^2)` — violates the in-place requirement.

## Optimal Approach (Transpose + Column Reversal)

A 90° counterclockwise rotation decomposes into two in-place operations. It is
the mirror image of the clockwise case: instead of reversing each row, we
reverse each **column** (equivalently, reverse the order of the rows).

1. **Transpose** the matrix (swap `matrix[i][j]` with `matrix[j][i]`), iterating
   only the upper triangle.
2. **Reverse the order of the rows** (`matrix.reverse()`), which reverses every
   column in place.

```python
def rotateCounterclockwise(matrix):
    n = len(matrix)

    # Step 1: transpose in place.
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse the row order (reverses each column).
    matrix.reverse()
```

**Why it is correct.** Transpose sends `(i, j) -> (j, i)`. Reversing the row
order sends row `j` to row `n - 1 - j`, i.e. `(j, i) -> (n - 1 - j, i)`.
Composing the two maps sends the original `(i, j)` to `(n - 1 - j, i)`, which is
exactly the definition of a 90° counterclockwise rotation. Only existing cells
are rearranged, so no extra matrix is needed.

**Step by step** on `[[1,2,3],[4,5,6],[7,8,9]]`:

1. Transpose: `[[1,4,7],[2,5,8],[3,6,9]]`.
2. Reverse row order: `[[3,6,9],[2,5,8],[1,4,7]]` — the answer.

- **Time:** `O(n^2)`.
- **Space:** `O(1)` auxiliary.

## Key Insights & Edge Cases

- **Clockwise vs. counterclockwise** differ only in the second step:
  - Clockwise = transpose + reverse each **row**.
  - Counterclockwise = transpose + reverse the **row order** (reverse each
    column).
- `matrix.reverse()` reverses the outer list (the rows) in place in `O(n)` list
  operations and does not allocate a new grid.
- **Upper-triangle-only swap** is still essential; swapping the whole grid would
  cancel the transpose.
- **1x1** input is returned unchanged.
- Four counterclockwise rotations return the original matrix, a handy sanity
  check when testing.
