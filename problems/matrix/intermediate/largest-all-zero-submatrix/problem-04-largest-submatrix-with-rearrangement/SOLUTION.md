# Solution — Largest Submatrix With Rearrangements

## Brute Force

Try every subset/ordering of columns and every band of rows, checking whether
the resulting block is all `1`s. Even ignoring row bands, there are up to `n!`
column orderings — factorial and hopeless. Any straightforward enumeration of
(row-band × column-subset) is exponential.

- **Time:** exponential (column permutations / subsets).
- **Space:** O(m·n).

## Optimal Approach (Per-Row Heights + Sort)

**Step 1 — heights (same as largest-all-zero-submatrix).** Convert `matrix` in
place into a height matrix where `matrix[i][j]` becomes the number of consecutive
`1`s in column `j` ending at row `i`:

```
if original matrix[i][j] == 1 and i > 0:
    matrix[i][j] += matrix[i-1][j]     # extend the run from above
elif original matrix[i][j] == 0:
    matrix[i][j] = 0                   # a 0 breaks the run
```

**Step 2 — exploit the free column reordering by sorting.** Consider any single
row `i` as the *bottom* of the submatrix. Row `i` now holds, for each column, how
tall an all-`1` bar rises above that column. Because we may permute columns
arbitrarily, we can place any `k+1` columns next to each other. The tallest
all-`1` rectangle of width `k+1` that uses this row as its base is limited by the
**(k+1)-th largest** height. So:

1. Take row `i`'s heights and **sort them in descending order**.
2. For each position `k` (0-indexed), the first `k+1` sorted heights are all
   `>= heights_sorted[k]`, so a rectangle of width `k+1` and height
   `heights_sorted[k]` is all `1`s. Its area is `(k + 1) * heights_sorted[k]`.
3. The best for row `i` is the max over `k`. The answer is the max over all rows.

```python
def largestSubmatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    # Step 1: build column heights in place.
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j]:
                matrix[i][j] += matrix[i - 1][j]
    # Step 2: sort each row's heights, evaluate widths.
    best = 0
    for row in matrix:
        row_sorted = sorted(row, reverse=True)
        for k, h in enumerate(row_sorted):
            best = max(best, (k + 1) * h)
    return best
```

**Why sorting replaces the monotonic stack.** In the fixed-column problems the
stack was needed because a rectangle had to occupy a *contiguous* span of
columns limited by the shortest bar in that span. Here columns are free to move,
so contiguity is irrelevant — we simply want the largest set of columns all at
least some height, which sorting descending exposes directly.

### Worked trace on Example 1

```
matrix = [[0, 0, 1],
          [1, 1, 1],
          [1, 0, 1]]
```

Heights after step 1:

```
row 0: [0, 0, 1]
row 1: [1, 1, 2]
row 2: [2, 0, 3]
```

- row 0 sorted `[1,0,0]` → best `1*1 = 1`.
- row 1 sorted `[2,1,1]` → `1*2=2`, `2*1=2`, `3*1=3` → best `3`.
- row 2 sorted `[3,2,0]` → `1*3=3`, `2*2=4`, `3*0=0` → best `4`.

Overall max = **4**, matching the expected output.

- **Time:** O(m·n) to build heights + O(m · n log n) for the per-row sorts =
  **O(m · n log n)**. (Counting sort per row would make it O(m·n) since heights
  are bounded by `m`.)
- **Space:** O(1) extra if you sort rows in place (O(n) for a copy otherwise).

## Key Insights & Edge Cases

- **Reordering ⇒ sort, not stack.** This is the key distinction from problems 1-3.
  The height-building phase is identical; only the "combine columns" phase
  differs.
- **In-place height build** mutates the input; make a copy first if the caller
  needs the original matrix preserved.
- **Single row** → heights equal the row itself; sorting groups the `1`s, so the
  answer is (count of 1s) × 1.
- **All zeros** → heights all 0 → answer 0. **All ones** → answer `m * n`.
- Counting sort per row (values in `0..m`) removes the log factor for a strict
  O(m·n) solution if needed.
