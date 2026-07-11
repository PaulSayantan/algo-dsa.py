# Solution — Number of Submatrices That Sum to Target

## Brute Force

Build a 2D prefix-sum table and iterate over all `(top, bottom, left, right)`
quadruples, incrementing a counter whenever the rectangle sum equals `target`.

- **Time:** `O(n² · m²)` with `O(1)` sum lookups.
- **Space:** `O(n · m)` for the prefix table.

For `n = m = 100` that is `10⁸` rectangles — borderline but wasteful. We can do
better by replacing the inner column double-loop with a hash-map pass.

## Optimal Approach — Kadane 2D reduction + prefix-sum hash map

Keep the Kadane 2D skeleton (fix rows, compress columns), but the 1D
subroutine becomes the classic **"count subarrays with sum = target"** using a
running prefix sum and a hash map — the same trick as LeetCode 560.

**Step by step:**

1. For each `top` row, reset `colSum = [0] * m`.
2. For each `bottom >= top`, add row `bottom` into `colSum` so that `colSum[c]`
   is the sum of column `c` over rows `top..bottom`.
3. Now count contiguous subarrays of `colSum` that sum to `target`. Walk the
   prefix sum `pre`; the number of subarrays ending at the current index with
   sum `target` equals how many earlier prefixes equal `pre - target`. A hash
   map `seen` counts prefix-sum frequencies (seeded with `seen[0] = 1` for the
   empty prefix).
4. Add those counts across all row bands.

```python
from collections import defaultdict

def numSubmatrixSumTarget(matrix, target):
    n, m = len(matrix), len(matrix[0])
    total = 0
    for top in range(n):
        col = [0] * m
        for bottom in range(top, n):
            for c in range(m):
                col[c] += matrix[bottom][c]      # compress the row band
            # --- count 1D subarrays of col summing to target ---
            seen = defaultdict(int)
            seen[0] = 1
            pre = 0
            for x in col:
                pre += x
                total += seen[pre - target]
                seen[pre] += 1
    return total
```

**Why it is correct.** Fixing `(top, bottom)` restricts attention to submatrices
whose vertical extent is exactly those rows; such a submatrix's sum equals the
sum of a contiguous slice of `colSum`. A contiguous slice `(left, right]` has sum
`pre[right] - pre[left]`, which equals `target` exactly when a prior prefix
`pre[left] = pre[right] - target` exists. The hash map counts every such prior
prefix, so it counts every qualifying column band for that row pair. Since every
submatrix has a unique row band, summing over all `(top, bottom)` pairs counts
each qualifying submatrix exactly once.

- **Time:** `O(n² · m)` — `O(n²)` row bands times an `O(m)` compress + `O(m)`
  hash-map pass.
- **Space:** `O(m)` for `colSum` and the hash map.

**Optimization:** Transpose so the squared factor is on the smaller dimension:
`O(min(n,m)² · max(n,m))`.

## Key Insights & Edge Cases

- **Seed `seen[0] = 1`:** This accounts for column bands that start at index `0`
  (a prefix that itself equals `target`). Forgetting it undercounts.
- **Reset `seen` per row band:** The hash map must be cleared for every
  `(top, bottom)` pair — prefixes from one band are meaningless for another.
- **Counting, not maximizing:** Unlike max-sum problems, negative and positive
  contributions both matter and there is no "restart"; use the prefix-sum map,
  not Kadane's extend-or-restart.
- **Duplicates count separately:** Two submatrices with identical values but
  different coordinates are distinct; the coordinate-based enumeration handles
  this automatically.
- **`target` can be negative or large:** `pre - target` may be any integer;
  Python ints handle it, but in fixed-width languages use 64-bit sums (up to
  `100 · 100 · 1000 = 10⁷` magnitude, well within 32-bit, yet safer to be
  explicit).
