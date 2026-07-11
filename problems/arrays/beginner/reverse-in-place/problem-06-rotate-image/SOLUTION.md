# Rotate Image — Solution

## Brute Force

Allocate a fresh `n x n` matrix and place each element at its rotated destination: the
element at `(i, j)` in a 90-degree clockwise rotation lands at `(j, n - 1 - i)`.

```python
n = len(matrix)
rotated = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated[j][n - 1 - i] = matrix[i][j]
matrix[:] = rotated
```

- **Time:** O(n^2) — every cell visited once.
- **Space:** O(n^2) — the extra matrix, which the problem explicitly forbids.

## Optimal Approach (Reverse In-Place)

A 90-degree clockwise rotation equals **transpose, then reverse each row**. The
row-reversal step is exactly the reverse-in-place two-pointer swap.

```python
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Step 1: transpose (reflect across the main diagonal).
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row in place.
    for row in matrix:
        left, right = 0, n - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
```

**Why it is correct:** Transposing sends element `(i, j)` to `(j, i)`. Reversing each
row then sends `(j, i)` to `(j, n - 1 - i)`. Composed, `(i, j) -> (j, n - 1 - i)`,
which is precisely the mapping for a 90-degree clockwise rotation.

Worked example, `[[1,2,3],[4,5,6],[7,8,9]]`:
- Transpose -> `[[1,4,7],[2,5,8],[3,6,9]]`
- Reverse each row -> `[[7,4,1],[8,5,2],[9,6,3]]`  ✓

- **Time:** O(n^2) — the transpose touches each cell once and the row reversals do too.
- **Space:** O(1) — all swaps happen inside the original matrix.

## Key Insights & Edge Cases

- **Transpose loop starts at `j = i + 1`.** Iterating over the strict upper triangle
  swaps each off-diagonal pair exactly once; starting at `j = 0` would swap every pair
  twice and undo the transpose. Diagonal elements stay fixed.
- **Reverse-each-row is the reverse-in-place kernel** — the same two-pointer swap from
  the "Reverse String" problem, applied per row.
- **Counter-clockwise variant:** reverse each row first *then* transpose, or transpose
  then reverse each column — a handy thing to know for the mirrored question.
- **`n == 1`:** transpose and reversal are both no-ops; the single cell is unchanged.
