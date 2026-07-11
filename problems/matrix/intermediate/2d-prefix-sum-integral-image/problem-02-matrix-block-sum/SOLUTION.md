# Solution — Matrix Block Sum

## Brute Force

For every output cell `(i, j)`, iterate over the up-to-`(2k+1) x (2k+1)` block
around it, clamping indices to the grid, and accumulate the sum.

```python
for i in range(m):
    for j in range(n):
        s = 0
        for r in range(max(0, i - k), min(m - 1, i + k) + 1):
            for c in range(max(0, j - k), min(n - 1, j + k) + 1):
                s += mat[r][c]
        answer[i][j] = s
```

- **Time:** O(m * n * k^2). With `m = n = k = 100` that is `10^8` — borderline
  and clearly wasteful because neighboring blocks overlap heavily.
- **Space:** O(m * n) for the output.

## Optimal Approach — 2D Prefix Sum (Integral Image)

The block for `(i, j)` is just a rectangle whose corners we clamp to the grid:

```
r1 = max(0, i - k)      r2 = min(m - 1, i + k)
c1 = max(0, j - k)      c2 = min(n - 1, j + k)
```

If we have a padded prefix table `P` of size `(m+1) x (n+1)`, each block sum is
one O(1) inclusion-exclusion query:

```
answer[i][j] = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

### Step by step

1. Build `P` where `P[i][j]` is the sum of the top-left `i x j` subrectangle:
   `P[i][j] = mat[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]`.
2. For each `(i, j)`, compute the clamped corners `r1, c1, r2, c2`.
3. Answer the rectangle sum with the query formula above.

### Why it is correct

Clamping the corners is exactly the "positions inside the matrix" rule from the
statement: any part of the ideal `(2k+1) x (2k+1)` window that falls outside the
grid is dropped, which is the same as shrinking the rectangle to the grid
boundary. The prefix-sum query then returns the exact sum of that clamped
rectangle.

### Reference implementation

```python
class Solution:
    def matrixBlockSum(self, mat, k):
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = (mat[i - 1][j - 1] + P[i - 1][j]
                           + P[i][j - 1] - P[i - 1][j - 1])

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m - 1, i + k), min(n - 1, j + k)
                ans[i][j] = (P[r2 + 1][c2 + 1] - P[r1][c2 + 1]
                             - P[r2 + 1][c1] + P[r1][c1])
        return ans
```

- **Time:** O(m * n) to build + O(m * n) to fill the answer = O(m * n).
- **Space:** O(m * n) for the prefix table (plus the required output).

## Key Insights & Edge Cases

- The problem reduces to "answer m*n rectangle-sum queries", the canonical use
  of an integral image.
- **Clamping** must use `min(m-1, i+k)` / `min(n-1, j+k)` for the far corners and
  `max(0, ...)` for the near corners — mixing these up is the usual bug.
- Large `k` (e.g. `k >= max(m, n)`): every block becomes the whole matrix, so
  every cell equals the grand total. The clamping handles this with no special
  case.
- `k` can equal 0 in the general definition (block is a single cell); the code
  above still works, returning `mat` unchanged.
