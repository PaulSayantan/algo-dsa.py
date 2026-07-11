# Largest Submatrix With Rearrangements — Solution

## Brute Force

Because columns can be permuted, a rectangle is defined by (a) a set of columns and (b) a
contiguous band of rows in which all chosen columns are `1`. Enumerating column subsets is
exponential, so a naive search over subsets is `O(2^n)` and hopeless for `n` up to `10^5`.

Even restricting to "choose a band of rows, then count columns that are all-`1` across that
band" is `O(m^2 * n)` (all `O(m^2)` bands times `O(n)` per band), which is too slow at the
constraint limits.

## Optimal Approach (Per-row heights + sort)

**Step 1 — column heights.** Transform the matrix in place (or in a copy) so that
`matrix[i][j]` becomes the number of consecutive `1`s ending at row `i` in column `j`:

```
if matrix[i][j] == 1 and i > 0:
    matrix[i][j] += matrix[i - 1][j]
```

Now row `i` holds, for each column, how tall a vertical strip of `1`s hangs down to row `i`.
This is precisely the histogram-heights step shared with Maximal Rectangle (Problem 5).

**Step 2 — sort each row and sweep.** Fix the bottom edge of the rectangle at row `i`. Any
rectangle with that bottom edge is determined by choosing some columns and using the minimum
of their heights as the rectangle height. Since columns are freely reorderable, the optimal
choice for a target height is obvious: **sort the row's heights in descending order**. If the
sorted heights are `h[0] >= h[1] >= ... >= h[n-1]`, then using the tallest `k + 1` columns
gives a rectangle of height `h[k]` and width `k + 1`, area `h[k] * (k + 1)`. Take the max
over all `k` and all rows.

**Why it is correct.** For a fixed bottom row and a fixed desired width `w`, you want the `w`
columns with the largest heights, and the rectangle height is the smallest of those, i.e.
the `w`-th largest height. Sorting descending makes the `w`-th largest height exactly
`h[w-1]`, so scanning `k = 0..n-1` and computing `h[k] * (k + 1)` considers the best rectangle
of every width for that bottom row. Every all-`1` rectangle (after any permutation) has some
bottom row and some width, so the global max over rows and widths is the answer.

```python
def largestSubmatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j]:
                matrix[i][j] += matrix[i - 1][j]
    best = 0
    for row in matrix:
        heights = sorted(row, reverse=True)
        for k, h in enumerate(heights):
            best = max(best, h * (k + 1))
    return best
```

- **Time:** `O(m * n log n)` — dominated by sorting each of the `m` rows.
- **Space:** `O(n)` for the per-row sorted copy (or `O(1)` extra if you sort in place and
  restore, though that is rarely worth it).

## Key Insights & Edge Cases

- **Reordering removes the need for a stack.** In Maximal Rectangle the columns are fixed, so
  you need a monotonic stack to find contiguous spans. Here, free permutation means the best
  layout is simply "sort tallest columns together," turning the per-row step into a sort.
- **Height accumulation resets on a `0`.** A `0` cell keeps its height at `0`, correctly
  breaking the vertical run of `1`s.
- **Sort descending, multiply by rank.** `h[k] * (k + 1)` is the whole trick after sorting.
- **Single row or single column** work unchanged — the sort of one element (or a column of
  accumulating heights) is handled by the same loop.
- **All zeros** yield heights all `0`, so the answer is `0`.
- If instead of area you needed the largest all-`1` *square* under column reordering, you
  would compare against `min(h[k], k + 1)` per rank rather than the product.
