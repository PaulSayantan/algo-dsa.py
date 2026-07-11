# Rotate Image (90° Clockwise) — Solution

## Brute Force

Allocate a new `n x n` matrix and place each element at its rotated position
`result[j][n-1-i] = matrix[i][j]`, then copy the result back into the input.

```python
def rotate(matrix):
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - 1 - i] = matrix[i][j]
    matrix[:] = result   # copy back so the change is in place from the caller's view
```

- **Time:** `O(n^2)`.
- **Space:** `O(n^2)` — violates the in-place requirement (allocates a second
  grid).

## Optimal Approach (Transpose + Row Reversal)

A 90° clockwise rotation decomposes into two in-place operations:

1. **Transpose** the matrix (swap `matrix[i][j]` with `matrix[j][i]`), iterating
   only the upper triangle so each pair is swapped once.
2. **Reverse each row.**

```python
def rotate(matrix):
    n = len(matrix)

    # Step 1: transpose in place (square matrix -> O(1) space).
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row.
    for row in matrix:
        row.reverse()
```

**Why it is correct.** Transpose sends `(i, j) -> (j, i)`. Reversing each row
sends column `j` to column `n - 1 - j`, i.e. `(j, i) -> (j, n - 1 - i)`.
Composing the two maps sends the original `(i, j)` to `(j, n - 1 - i)`, which is
exactly the definition of a 90° clockwise rotation. Both steps only rearrange
existing cells, so no extra matrix is needed.

**Step by step** on `[[1,2,3],[4,5,6],[7,8,9]]`:

1. Transpose: `[[1,4,7],[2,5,8],[3,6,9]]`.
2. Reverse each row: `[[7,4,1],[8,5,2],[9,6,3]]` — the answer.

- **Time:** `O(n^2)`.
- **Space:** `O(1)` auxiliary.

## Key Insights & Edge Cases

- **Transpose first, then reverse rows** = clockwise. (Reverse rows first, then
  transpose, also works and gives the same result — the order of the two phases
  can be swapped as long as you pick the matching reversal.)
- **Iterate the upper triangle only** (`j` from `i + 1`). Swapping the full grid
  would transpose it and then transpose it back to the original — a no-op bug.
- **1x1 and even/odd n** all work with the same code; there is no special
  center case because the swap loop naturally skips the diagonal.
- **In place matters:** returning a new matrix from `rotate` would fail the
  problem's contract; mutate `matrix` directly.
