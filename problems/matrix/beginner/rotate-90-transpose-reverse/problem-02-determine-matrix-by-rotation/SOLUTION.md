# Determine Whether Matrix Can Be Obtained By Rotation — Solution

## Brute Force

Generate all four rotations of `mat` by any means (for example, using index
formulas to build a brand-new matrix for each of the 90°, 180°, and 270°
orientations) and compare each to `target`.

- Build rotation-1 with `r1[j][n-1-i] = mat[i][j]`, rotation-2 from rotation-1,
  and so on.
- Compare each fresh matrix to `target`.

**Time:** `O(n²)` — four rotations, each `O(n²)`, is still `O(n²)`.
**Space:** `O(n²)` for the extra matrices you allocate.

## Optimal Approach (Rotate 90° via transpose + reverse)

Only four orientations exist, so rotate `mat` **in place** up to three times and
compare after each turn. Each clockwise turn is transpose-then-reverse-each-row.

```python
def findRotation(mat, target):
    def rotate(m):                      # 90 deg clockwise, in place
        n = len(m)
        for i in range(n):              # transpose
            for j in range(i + 1, n):
                m[i][j], m[j][i] = m[j][i], m[i][j]
        for row in m:                   # reverse each row
            row.reverse()

    for _ in range(4):                  # 0, 1, 2, 3 quarter-turns
        if mat == target:
            return True
        rotate(mat)
    return False
```

**Why it is correct:** Any rotation by a multiple of 90° is one of exactly four
orientations. By checking `mat == target` before the first rotation and after
each of the next three, we test all four candidates. Transpose-then-reverse-row
is a proven 90° clockwise rotation (see the folder README), so the sequence of
in-place rotations visits every orientation exactly once.

**Step by step** on Example 1, `mat = [[0,1],[1,0]]`, `target = [[1,0],[0,1]]`:

1. Turn 0: `mat = [[0,1],[1,0]]` ≠ target. Rotate.
2. Transpose swaps `(0,1)` with `(1,0)` (both `1`) → unchanged `[[0,1],[1,0]]`.
   Reverse each row → `[[1,0],[0,1]]`.
3. Turn 1: `mat = [[1,0],[0,1]]` == target → return `True`.

**Time:** `O(n²)` — a constant number (4) of `O(n²)` operations.
**Space:** `O(1)` extra; the rotation is in place.

## Key Insights & Edge Cases

- **Check the 0-turn case.** `mat` might already equal `target`; compare before
  rotating, not only after.
- **Only four orientations exist**, so a fourth rotation would repeat the
  original — never loop more than four times.
- **In-place transpose needs `j` to start at `i + 1`** so the diagonal is not
  double-swapped.
- `n == 1`: a `1 × 1` matrix is unchanged by rotation, so the answer is just
  `mat == target`.
- A quick pruning check — equal count of 1s — is optional; the four comparisons
  are already cheap for `n <= 10`.
