# Solution — Count Submatrices With All Ones

## Brute Force

Enumerate every rectangle by its top row, bottom row, left column, and right
column, then verify it is all `1`s.

- Enumerating corners is O(m²n²) rectangles; verifying each naively adds another
  O(mn), giving O(m³n³). With a 2D prefix sum the all-ones test is O(1), so the
  total is **O(m²n²)**.
- For `m, n <= 150`, `m²n²` ≈ 5 * 10^8 — slow but sometimes accepted; there is a
  much cleaner O(m²n) / O(mn) route.

```python
def brute(mat):
    m, n = len(mat), len(mat[0])
    # prefix[i][j] = sum of mat[0..i-1][0..j-1]
    pre = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m):
        for j in range(n):
            pre[i+1][j+1] = mat[i][j] + pre[i][j+1] + pre[i+1][j] - pre[i][j]
    def ones(r1, c1, r2, c2):
        return pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1]
    count = 0
    for r1 in range(m):
        for r2 in range(r1, m):
            for c1 in range(n):
                for c2 in range(c1, n):
                    area = (r2-r1+1)*(c2-c1+1)
                    if ones(r1, c1, r2, c2) == area:
                        count += 1
    return count
```

## Optimal Approach (Histogram Heights + Monotonic Stack Sum)

**Reduce to counting per bottom row.** As in largest-all-zero-submatrix, build

```
height[j] = number of consecutive 1s ending at the current row in column j
```

(reset to 0 on a `0`). Every all-`1` rectangle has a unique bottom row, so it
suffices to count, for each row, the rectangles whose **bottom edge lies on that
row** using `height[]`, then sum over rows.

**Counting rectangles ending at each column with a monotonic stack.** For the
current row, define `f[j]` = the number of all-`1` rectangles whose bottom-right
corner is `(current row, j)`. Such a rectangle picks a left column `l <= j`; its
height is limited by `min(height[l..j])`, and it may choose any of those
`min(height[l..j])` heights. So:

- Let `p` be the nearest column to the left of `j` with `height[p] < height[j]`
  (or `-1`). For columns in `(p, j]` the limiting height is `height[j]`, each
  contributing `height[j]` rectangles for that right edge → `(j - p) * height[j]`.
- For columns at or before `p`, the count is exactly the same as what already
  ended at column `p` (the taller bar `j` doesn't change those), i.e. `f[p]`.

Therefore:

```
f[j] = (j - p) * height[j] + f[p]      (f[p] = 0 when p == -1)
```

A monotonic increasing stack finds `p` in amortized O(1). Summing `f[j]` over all
columns and all rows gives the answer.

```python
def numSubmat(mat):
    m, n = len(mat), len(mat[0])
    height = [0] * n
    total = 0
    for i in range(m):
        for j in range(n):
            height[j] = height[j] + 1 if mat[i][j] == 1 else 0
        stack = []          # indices with strictly increasing heights
        f = [0] * n
        for j in range(n):
            # pop bars taller-or-equal so the top is the nearest strictly shorter
            while stack and height[stack[-1]] >= height[j]:
                stack.pop()
            if stack:
                p = stack[-1]
                f[j] = (j - p) * height[j] + f[p]
            else:
                f[j] = (j + 1) * height[j]
            stack.append(j)
            total += f[j]
    return total
```

**Why it is correct.** `f[j]` counts every all-`1` rectangle with bottom-right
corner exactly `(i, j)`: choosing a left edge and a height. Splitting at `p`
(nearest strictly shorter bar to the left) partitions those choices into "left
edge inside `(p, j]`, height up to `height[j]`" — that's `(j - p) * height[j]` —
and "left edge at or before `p`", which is identical to the rectangles counted
by `f[p]` since bar `j` is at least as tall and imposes no new limit. Summing
`f[j]` over all `(i, j)` counts each all-`1` rectangle once, at its unique
bottom-right corner.

### Worked trace on Example 3

```
mat = [[1, 1, 1, 1, 1, 1]]
```

Single row → `height = [1,1,1,1,1,1]`. Since heights are equal, each `f[j]`
reduces to `f[j] = (j + 1) * 1` because the stack keeps popping equal bars,
leaving no strictly-shorter predecessor:

```
f = [1, 2, 3, 4, 5, 6]   sum = 21
```

Matching the expected **21** (= 6+5+4+3+2+1 subarrays of a length-6 run).

- **Time:** O(m·n) — each column is pushed/popped once per row.
- **Space:** O(n) for `height`, `f`, and the stack.

## Key Insights & Edge Cases

- **Count, don't maximize.** The height-build phase is identical to the largest-
  submatrix problems; the difference is the stack carries a running *sum* `f[j]`
  instead of a running max area.
- **Use `>=` when popping** so the nearest *strictly* shorter bar becomes `p`.
  This correctly folds equal-height runs into `f[p]` and prevents double
  counting.
- **The `f[p]` carry** is the crux: it reuses previously counted rectangles whose
  left edge lies further left, in O(1).
- **A row of zeros** contributes `height[j] = 0` everywhere → adds 0.
- **Overflow:** counts can be large (up to ~ (mn)² / 4); use 64-bit integers in
  languages without arbitrary precision (Python is fine).
- An alternative O(m²n) approach fixes the top row, extends downward tracking a
  per-column consecutive width, and sums row minima — simpler to derive but a
  factor slower than the O(mn) stack method above.
