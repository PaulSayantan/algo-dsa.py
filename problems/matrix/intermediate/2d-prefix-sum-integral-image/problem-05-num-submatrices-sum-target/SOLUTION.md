# Solution — Number of Submatrices That Sum to Target

## Brute Force

Enumerate every submatrix by its four corners `(x1, y1, x2, y2)` and sum it.

```python
count = 0
for x1 in range(m):
    for y1 in range(n):
        for x2 in range(x1, m):
            for y2 in range(y1, n):
                if submatrix_sum(x1, y1, x2, y2) == target:
                    count += 1
```

There are O(m^2 * n^2) submatrices. Even with an O(1) integral-image sum per
submatrix this is O(m^2 * n^2), which for `100 x 100` is `10^8` — passable but
on the edge, and naive summation makes it O(m^3 * n^3).

- **Time:** O(m^2 * n^2) with a prefix table (O(m^3 * n^3) without).
- **Space:** O(m * n) for the prefix table.

## Optimal Approach — Row/Column Compression + Hash Map

Combine a 2D/1D prefix sum with the classic **"subarray sum equals K"** hash-map
trick to drop a whole factor of `n` (or `m`).

### The idea

1. Build **row-wise prefix sums** so that the sum of columns `[c1..c2]` within a
   single row `r` is O(1): `rowP[r][c2+1] - rowP[r][c1]`. (This is the 1D slice
   of the integral image; you can equally build the full 2D table.)
2. **Fix the top row `r1` and bottom row `r2`.** Collapse the band of rows
   `r1..r2` into a single 1D array `col`, where `col[c]` is the sum of column
   `c` across rows `r1..r2` — each entry is one O(1) prefix query.
3. Now the question "how many submatrices with these top/bottom rows sum to
   `target`?" becomes "how many **subarrays** of `col` sum to `target`?" — solve
   it in O(n) with a running prefix sum and a hash map counting how many times
   each running sum has occurred. For each position, we look up
   `running - target`.

### Step by step

1. Precompute `rowP[r][c] = sum of matrix[r][0..c-1]`.
2. For every pair of rows `r1 <= r2`:
   - Build `col[c] = rowP[r2][c+1] - rowP[r1][c+1]`? No — build
     `col[c] = (band sum of column c)` via row prefixes accumulated over
     `r1..r2` (see code).
   - Run the 1D "count subarrays == target" scan over `col`, adding to the total.
3. Return the total.

### Why it is correct

Every submatrix is uniquely determined by its top row, bottom row, left column,
and right column. Iterating over all `(r1, r2)` row pairs partitions the
submatrices by their vertical extent, with no double counting. For a fixed row
band, a submatrix corresponds exactly to a contiguous column range, i.e. a
subarray of `col`, and the hash-map scan counts every subarray summing to
`target` — including those with negative values, because it works purely on
running prefix sums.

### Reference implementation

```python
from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])

        # Row-wise prefix sums: rowP[r][c] = sum of matrix[r][0..c-1]
        rowP = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                rowP[r][c + 1] = rowP[r][c] + matrix[r][c]

        total = 0
        for c1 in range(n):
            for c2 in range(c1, n):
                # For each row, the sum of columns c1..c2 is O(1).
                seen = defaultdict(int)
                seen[0] = 1
                running = 0
                for r in range(m):
                    running += rowP[r][c2 + 1] - rowP[r][c1]
                    total += seen[running - target]
                    seen[running] += 1
        return total
```

(This variant fixes a **column pair** and scans down the rows; fixing a row pair
and scanning across columns is symmetric. Choose the pair over the smaller
dimension for speed.)

- **Time:** O(min(m, n)^2 * max(m, n)). For `100 x 100`, about `10^6`.
- **Space:** O(m * n) for the prefix table + O(max(m, n)) for the hash map.

## Key Insights & Edge Cases

- Reducing 2D to 1D by **fixing two boundaries** (row pair or column pair) is the
  single most important pattern layered on top of prefix sums; problem 6 uses the
  same collapse.
- Seed the hash map with `seen[0] = 1` so that a prefix that itself equals
  `target` (a submatrix starting at the first row/column) is counted.
- **Negative numbers and `target = 0`** are the tricky cases; the prefix-sum +
  hash-map method handles them naturally, whereas any sliding-window shortcut
  would be wrong.
- Duplicate running sums must be **counted, not overwritten** — use a counter
  map, not a set.
- Iterate over the smaller dimension's pairs (`min(m, n)^2`) to keep the constant
  factor down.
