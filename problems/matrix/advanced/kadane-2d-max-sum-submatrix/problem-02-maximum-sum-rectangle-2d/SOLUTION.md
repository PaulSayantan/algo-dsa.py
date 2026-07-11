# Solution — Maximum Sum Rectangle in a 2D Matrix

## Brute Force

Enumerate every rectangle by choosing `(top, bottom)` row pair and
`(left, right)` column pair, then sum the enclosed cells.

- With a 2D prefix-sum table you can get each rectangle's sum in `O(1)`, so the
  enumeration is `O(n² · m²)`.
- Without the prefix table, summing each rectangle naively is `O(n³ · m³)`.

Either way the space is `O(n · m)` for the prefix table (or `O(1)` for the
fully naive version). For `n = m = 300`, `n² · m²` is about `8.1 × 10⁹` —
too slow.

## Optimal Approach — Kadane 2D

Collapse the 2D problem into repeated 1D problems.

**Step by step:**

1. **Fix the top row** `top` from `0` to `n-1`.
2. Initialize a compressed array `colSum` of length `m` to all zeros.
3. **Sweep the bottom row** `bottom` from `top` down to `n-1`. Each time
   `bottom` advances, add that row into the accumulator:
   `colSum[c] += matrix[bottom][c]` for every column `c`. Now `colSum[c]`
   holds the sum of the vertical strip `matrix[top..bottom][c]`.
4. **Run 1D Kadane** on `colSum`. The maximum contiguous subarray sum of
   `colSum` equals the best rectangle whose vertical extent is exactly
   `[top, bottom]`.
5. Track the global maximum across all `(top, bottom)` pairs.

```python
def maxSumRectangle(matrix):
    n, m = len(matrix), len(matrix[0])
    best = float("-inf")
    for top in range(n):
        col = [0] * m
        for bottom in range(top, n):
            for c in range(m):
                col[c] += matrix[bottom][c]   # compress the row band
            # --- 1D Kadane on col ---
            cur = col[0]
            local = col[0]
            for j in range(1, m):
                cur = max(col[j], cur + col[j])
                local = max(local, cur)
            best = max(best, local)
    return best
```

**Why it is correct.** Every rectangle is uniquely determined by a row band
`[top, bottom]` and a column band `[left, right]`. The outer two loops iterate
over *every* possible row band. For a fixed row band, the sum of the rectangle
with column band `[left, right]` is exactly
`colSum[left] + ... + colSum[right]` — a contiguous subarray of `colSum`. So
maximizing over column bands is precisely the 1D maximum-subarray problem on
`colSum`, which Kadane solves optimally. Taking the max over all row bands
therefore visits every rectangle's sum, guaranteeing the global optimum.

- **Time:** `O(n² · m)` — `O(n²)` row bands, and each does an `O(m)` compress
  update plus an `O(m)` Kadane pass.
- **Space:** `O(m)` for `colSum`.

**Optimization:** If `m < n`, transpose the matrix (or swap the roles of rows
and columns) so the squared factor lands on the smaller dimension, giving
`O(min(n,m)² · max(n,m))`.

## Key Insights & Edge Cases

- **Incremental compression:** Do not recompute `colSum` from scratch for each
  `bottom`; add one row at a time to keep the update `O(m)` rather than
  `O(n · m)`.
- **All-negative matrix:** Kadane must return the single largest cell, not `0`.
  Initialize the running/best sums with an actual element (`col[0]`), never
  with `0`, and never allow an "empty" rectangle.
- **Single row or single column:** The algorithm degrades gracefully; with one
  row it is just 1D Kadane, with one column each `colSum` has length 1.
- **Non-rectangular inputs:** Assumes a rectangular grid; validate that all
  rows share the same length if inputs are untrusted.
- **Reset per top:** `colSum` must be re-zeroed each time the `top` pointer
  moves; forgetting this bleeds sums across unrelated row bands.
