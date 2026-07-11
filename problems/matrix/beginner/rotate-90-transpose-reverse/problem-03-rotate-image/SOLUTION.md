# Rotate Image — Solution

## Brute Force

Allocate a new `n × n` matrix and copy each element to its rotated position
using the closed-form map for a 90° clockwise rotation: the element at
`(i, j)` goes to `(j, n-1-i)`.

```python
def rotate(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]
    matrix[:] = rotated   # copy back to satisfy "in place" API
```

**Time:** `O(n²)`. **Space:** `O(n²)` — violates the intended `O(1)` extra
memory requirement because it builds a full second matrix.

## Optimal Approach (Rotate 90° via transpose + reverse)

Two in-place passes achieve the rotation with only swaps:

1. **Transpose** — swap `matrix[i][j]` with `matrix[j][i]` for `j > i`.
2. **Reverse each row.**

```python
def rotate(matrix):
    n = len(matrix)
    # Pass 1: transpose (swap across main diagonal)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Pass 2: reverse each row
    for row in matrix:
        row.reverse()
```

**Why it is correct:** Transpose maps `(i, j) → (j, i)`. Reversing row `j`
maps column `i` to column `n-1-i`, so the element that transpose placed at
`(j, i)` lands at `(j, n-1-i)`. The composed map is `(i, j) → (j, n-1-i)`,
which is precisely the coordinate transform of a 90° clockwise rotation. Each
pass is a bijection over the cells, so nothing is overwritten prematurely.

**Step by step** on `[[1,2,3],[4,5,6],[7,8,9]]`:

1. Transpose swaps `(0,1)↔(1,0)`, `(0,2)↔(2,0)`, `(1,2)↔(2,1)`:
   `[[1,4,7],[2,5,8],[3,6,9]]`.
2. Reverse each row:
   `[7,4,1]`, `[8,5,2]`, `[9,6,3]` → `[[7,4,1],[8,5,2],[9,6,3]]`. Correct.

**Time:** `O(n²)` — each of the two passes touches every cell once.
**Space:** `O(1)` extra — only a temporary swap variable.

### Alternative: four-way ring swap

You can also rotate by cycling four cells at a time around each concentric ring:
`top → right → bottom → left`. It is also `O(n²)` / `O(1)` but has fiddly index
bounds. Transpose + reverse is easier to write correctly and is the recommended
approach here.

## Key Insights & Edge Cases

- **`j` starts at `i + 1`** in the transpose loop. Starting at `0` swaps every
  pair twice and leaves the matrix unchanged.
- **Clockwise = transpose then reverse rows.** For counter-clockwise, reverse
  the rows *first* or reverse the column order instead (see problem 4).
- **In place** means no second `n × n` matrix — reversing rows with
  `row.reverse()` mutates the existing lists.
- `n == 1`: both passes are no-ops, which is correct — a single cell is
  unchanged by rotation.
- Because the matrix is square, the transpose can be done in place; this trick
  does **not** extend to non-square matrices (see problem 1).
