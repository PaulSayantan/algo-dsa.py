# Rotate Image — Solution

## Brute Force

Allocate a fresh `n x n` matrix and copy each element to its rotated position:
for a clockwise rotation, element `(i, j)` lands at `(j, n-1-i)`.

```python
n = len(matrix)
rotated = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        rotated[j][n - 1 - i] = matrix[i][j]
matrix[:] = rotated
```

- **Time:** O(n²).
- **Space:** O(n²) — the extra matrix violates the in-place requirement.

## Optimal Approach — Transpose + Reverse Each Row (2-D reversal trick)

A 90° clockwise rotation equals a **transpose** (reflect over the main diagonal)
followed by a **horizontal reflection** (reverse every row). Both are done in
place, and reversing each row is literally the same two-pointer reverse that
powers 1-D array rotation.

```python
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix)

    # Step 1: transpose in place (swap across the main diagonal).
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: reverse each row (the reversal trick, applied row by row).
    for row in matrix:
        lo, hi = 0, n - 1
        while lo < hi:
            row[lo], row[hi] = row[hi], row[lo]
            lo += 1
            hi -= 1
```

### Why it is correct

- **Transpose** sends element `(i, j)` to `(j, i)`.
- **Reverse each row** then sends `(j, i)` to `(j, n-1-i)`.

Composing the two maps `(i, j) -> (j, n-1-i)`, which is exactly the clockwise
90° rotation formula. Because transpose only swaps pairs across the diagonal
(iterating `j` from `i+1` avoids swapping each pair twice), and row reversal is
a standard in-place reverse, no element is lost or double-moved.

Worked example, `[[1,2,3],[4,5,6],[7,8,9]]`:

```
transpose:            reverse each row:
1 4 7                 7 4 1
2 5 8       -->        8 5 2
3 6 9                 9 6 3
```

which matches the expected clockwise rotation.

### Complexity

- **Time:** O(n²) — each of the n² cells is touched a constant number of times.
- **Space:** O(1) — all swaps are in place.

## Key Insights & Edge Cases

- **Inner loop starts at `j = i + 1`.** Starting at `j = 0` would swap every pair
  twice and undo the transpose, leaving the matrix unchanged.
- **Row reversal is the 1-D reversal trick.** Rotating a matrix reuses the exact
  primitive from Rotate Array — recognizing this connection is the point of the
  problem.
- **Counter-clockwise variant:** reverse each row first *then* transpose, or
  transpose then reverse each *column* — the two building blocks recombine for
  the opposite direction.
- **`n == 1`:** transpose does nothing (`range(i+1, n)` is empty) and the single
  row reverses to itself — correct.
- **Even vs. odd `n`:** no special handling; the diagonal element in odd-sized
  matrices is simply never swapped, which is correct since it stays on the axis
  of the transpose and at the center of its row.
