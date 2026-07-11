# Solution — Max Sum of Rectangle No Larger Than K

## Brute Force

Enumerate all four corners, compute each rectangle sum, and keep the best value
that does not exceed `k`.

```python
best = -inf
for x1 in range(m):
    for y1 in range(n):
        for x2 in range(x1, m):
            for y2 in range(y1, n):
                s = rect_sum(x1, y1, x2, y2)
                if s <= k:
                    best = max(best, s)
```

- **Time:** O(m^2 * n^2) with an integral image for O(1) sums (O(m^3 * n^3)
  without). For `100 x 100` the O(m^2 n^2) version is `10^8` — works but slow,
  and does not exploit the `<= k` structure.
- **Space:** O(m * n) for the prefix table.

## Optimal Approach — Column-Pair Compression + Sorted-Set Search

This layers a 1D "max subarray sum <= k" search on top of prefix sums.

### Reduce 2D to 1D

Fix a **left column `c1`** and a **right column `c2`**. Using row-wise prefix
sums, compute for each row `r` the value
`rowSum[r] = sum of matrix[r][c1..c2]` in O(1). Now the best rectangle whose
horizontal extent is exactly `[c1, c2]` corresponds to the **maximum-sum
contiguous subarray of `rowSum` that is `<= k`**.

### 1D "max subarray sum <= k"

We cannot use Kadane directly because of the `<= k` cap and possible negatives.
Instead, walk a running prefix sum `S` down the rows and maintain a **sorted
set** of previously seen prefix sums `S_prev`. For the subarray ending at the
current row to have sum `<= k`, we need
`S - S_prev <= k`, i.e. `S_prev >= S - k`. So we search the sorted set for the
**smallest** `S_prev >= S - k` (a `lower_bound` / `bisect_left`); if it exists,
`S - S_prev` is a candidate. Then insert `S` into the set.

### Step by step

1. Precompute row-wise prefix sums `rowP` so any horizontal band sum is O(1).
2. For each column pair `(c1, c2)`:
   - Reset a sorted container `seen = {0}` (the empty prefix).
   - `S = 0`.
   - For each row `r`: add `rowSum[r]` to `S`; find the smallest `x` in `seen`
     with `x >= S - k`; if found, update `best = max(best, S - x)`; insert `S`.
   - Early-exit if `best == k` (cannot do better than the cap).
3. Return `best`.

### Why it is correct

Fixing `(c1, c2)` partitions rectangles by their horizontal extent. For that
band, a rectangle is a contiguous row range `[r1, r2]` with sum
`S(r2) - S(r1-1)`, where `S` is the running prefix over `rowSum`. Requiring
`S(r2) - S(r1-1) <= k` and maximizing it is exactly "for the current prefix
`S(r2)`, find the closest earlier prefix not below `S(r2) - k`". The sorted set
answers this in O(log m). Seeding with `0` accounts for rectangles that start at
the first row.

### Reference implementation

```python
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        m, n = len(matrix), len(matrix[0])

        # Fix the pair over the smaller dimension for speed.
        # Here we fix column pairs and scan rows; transpose first if n > m.
        rowP = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                rowP[r][c + 1] = rowP[r][c] + matrix[r][c]

        best = float("-inf")
        for c1 in range(n):
            for c2 in range(c1, n):
                seen = [0]
                S = 0
                for r in range(m):
                    S += rowP[r][c2 + 1] - rowP[r][c1]
                    idx = bisect_left(seen, S - k)
                    if idx < len(seen):
                        best = max(best, S - seen[idx])
                    insort(seen, S)
                if best == k:
                    return k
        return best
```

- **Time:** O(min(m, n)^2 * max(m, n) * log(max(m, n))). For `100 x 100`, about
  `100^2 * 100 * 7 ~ 7 * 10^6`.
- **Space:** O(m * n) for the prefix table + O(max(m, n)) for the sorted set.

## Key Insights & Edge Cases

- The `<= k` constraint with **negative numbers** kills plain Kadane; the
  sorted-set `lower_bound` search is what enforces the cap while still
  maximizing.
- Seed the sorted set with `0` so single-band rectangles that start at the top
  row are considered; forgetting this misses valid answers.
- Search for the smallest prefix `>= S - k` (not `> S - k`); using the wrong
  boundary can miss rectangles whose sum is exactly `k`.
- **Early termination** when `best == k` is a big practical speedup — no
  rectangle can beat the cap.
- **Transpose** the matrix when `n > m` so the O(dimension^2) factor is over the
  smaller side; this is the follow-up's point.
- Python has no built-in balanced BST; `bisect.insort` into a list is
  O(len) per insert. For the given limits that is fine; for larger inputs use a
  `SortedList` (from `sortedcontainers`) to keep inserts at O(log n).
