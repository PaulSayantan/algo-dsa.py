# Count Submatrices With All Ones — Solution

## Brute Force

Enumerate every rectangle by (top, bottom, left, right) and test whether it is all `1`.
With 2-D prefix sums each test is `O(1)`, but there are `O(m^2 * n^2)` rectangles.

- **Time:** `O(m^2 * n^2)` with prefix sums.
- **Space:** `O(m * n)`.

At `m, n <= 150` that is up to `~5 * 10^8` rectangles — borderline and wasteful. Two better
strategies follow; both share the histogram-heights first step.

## Optimal Approach (Per-row heights + monotonic stack counting)

**Step 1 — column heights.** As in Maximal Rectangle, compute `heights[j]` = consecutive `1`s
in column `j` ending at the current row (`0` resets it). Fixing the **bottom edge** of a
rectangle at the current row, we count all-`1` rectangles with that bottom edge, then sum over
all rows — every all-`1` rectangle has a unique bottom edge, so no double counting.

**Step 2 — count rectangles ending at each column with a monotonic stack.** For the current
histogram, define `dp[j]` = the number of all-`1` rectangles whose bottom edge is this row and
whose **right edge is column `j`**. Consider extending leftward from column `j`:

- If we keep a stack of columns with strictly increasing heights, let `p` be the previous
  index on the stack with `heights[p] < heights[j]` (its nearest shorter bar to the left).
- Columns strictly between `p` and `j` are all at least as tall as `heights[j]`, so for those
  columns the limiting height when the rectangle's right edge is `j` is `heights[j]`. They
  contribute `heights[j] * (j - p)` rectangles (choose any left edge in `(p, j]`, any of
  `heights[j]` row-heights).
- Columns at or left of `p` were already counted with limiting height `heights[p]`, captured
  by `dp[p]`.

So:

```
dp[j] = dp[p] + heights[j] * (j - p)          (p = nearest index left of j with a smaller height, else -1; dp[-1] = 0)
```

The monotonic stack finds `p` in amortized `O(1)`. Sum `dp[j]` over all columns for the row,
then over all rows.

**Why it is correct.** Every all-`1` rectangle with bottom edge on this row is uniquely
identified by its right column `j` and is counted in `dp[j]`. Splitting at the nearest shorter
bar `p` partitions those rectangles into (a) those confined to the "plateau" columns
`(p, j]`, whose height is capped at `heights[j]` and left edge ranges over `j - p` positions
across `heights[j]` possible heights, and (b) those that extend past `p`, which are exactly the
rectangles counted by `dp[p]` (same right-edge behavior shifted to column `p`). The two groups
are disjoint and exhaustive, so the recurrence is exact.

```python
def numSubmat(mat):
    m, n = len(mat), len(mat[0])
    heights = [0] * n
    total = 0
    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0
        stack = []          # indices with strictly increasing heights
        dp = [0] * n
        for j in range(n):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                p = stack[-1]
                dp[j] = dp[p] + heights[j] * (j - p)
            else:
                dp[j] = heights[j] * (j + 1)
            stack.append(j)
            total += dp[j]
    return total
```

- **Time:** `O(m * n)` — each column is pushed/popped once per row.
- **Space:** `O(n)` for `heights`, `dp`, and the stack.

**Simpler `O(m^2 * n)` alternative.** Fix a top row `t`. Sweep the bottom row `b` downward,
maintaining for each column the run-length of consecutive `1`s across rows `t..b` (a column is
"alive" only while all of `t..b` are `1`). For each `b`, scan columns left to right tracking
the current run of alive columns and add that run length. This is `O(m^2 * n)` and easier to
get right, and passes at `m, n <= 150`. The stack version above is the linear-in-cells
optimum.

## Key Insights & Edge Cases

- **Same skeleton as Maximal Rectangle.** Both start with per-row column heights; Problem 5
  takes the *max* rectangle via a stack, this one *counts* rectangles via a stack.
- **Bottom-edge decomposition avoids double counting.** Each rectangle is attributed to its
  unique bottom row and, within a row, to its unique right column via `dp[j]`.
- **`>=` when popping.** Popping equal-or-taller bars ensures `p` is the nearest *strictly
  shorter* bar, which is what the plateau argument requires; using `>` would miscount equal
  heights.
- **Integer grid.** `mat` holds ints, so reset height on `0` and accumulate on `1`.
- **All zeros** gives `0`; a single `1` gives `1`; a full all-`1` `m x n` grid gives
  `(m*(m+1)/2) * (n*(n+1)/2)` — a good sanity check.
- **Overflow.** The count can be large; use 64-bit accumulators in fixed-width languages
  (Python integers are unbounded).
