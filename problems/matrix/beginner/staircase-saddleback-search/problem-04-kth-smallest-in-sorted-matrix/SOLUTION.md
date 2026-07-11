# Solution — Kth Smallest Element in a Sorted Matrix

## Brute Force

Flatten all `n^2` values, sort, and index position `k - 1`.

```python
flat = sorted(v for row in matrix for v in row)
return flat[k - 1]
```

- **Time:** `O(n^2 log n)`.
- **Space:** `O(n^2)` for the flattened list — which the problem explicitly asks
  us to beat.

A heap-based merge of the `n` sorted rows (like merging `k` lists) gets
`O(k log n)` time and `O(n)` space, but it can be slow when `k` is near `n^2`.

## Optimal Approach — Binary Search on Value + Staircase Count

The key realization: we do not binary-search a position, we **binary-search the
answer value**. Define

```
count_le(x) = number of matrix entries that are <= x
```

`count_le` is non-decreasing in `x`. The k-th smallest element is the **smallest
value `x` such that `count_le(x) >= k`**. We find it by bisecting the value range
`[matrix[0][0], matrix[n-1][n-1]]`.

### Counting with a staircase walk — the saddleback part

To evaluate `count_le(x)` in `O(n)`, walk the **bottom-left** corner
`(r, c) = (n - 1, 0)`:

- **`matrix[r][c] <= x`** → because the column is ascending, every entry from row
  `0` to row `r` in column `c` is also `<= x`. Add `r + 1` to the count and move
  **right**: `c += 1`.
- **`matrix[r][c] > x`** → this entry (and everything below it, already off-grid)
  is too big; move **up**: `r -= 1`.

Stop when `r < 0` or `c == n`. This is the same staircase walk as the search
problems, repurposed to *count* a region in `O(n)`.

```python
def count_le(matrix, x):
    n = len(matrix)
    r, c = n - 1, 0          # bottom-left corner
    count = 0
    while r >= 0 and c < n:
        if matrix[r][c] <= x:
            count += r + 1   # whole column above (rows 0..r) is <= x
            c += 1
        else:
            r -= 1
    return count
```

### Binary search driver

```python
def kthSmallest(matrix, k):
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[n - 1][n - 1]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if count_le(matrix, mid) >= k:
            hi = mid          # enough values <= mid; answer is mid or smaller
        else:
            lo = mid + 1      # too few; answer is strictly larger
    return lo
```

### Why the returned value is actually in the matrix

`lo` converges to the smallest `x` with `count_le(x) >= k`. That value must be an
actual matrix entry: if `x` were not present, then `count_le(x) == count_le(x-1)`,
so `x - 1` would also satisfy `>= k`, contradicting minimality. Hence `lo` lands
on a real element — the k-th smallest.

### Worked trace on Example 1

`matrix` diagonal range: `lo = 1`, `hi = 15`, `k = 8`.

- `mid = 8`: `count_le(8)` walks `12>8↑, 10>8↑, 1<=8 (+1) →, 5<=8 (+1) →, 9>8↑,
  off-grid` → count `2` (values 1, 5). `2 < 8` → `lo = 9`.
- `mid = 12`: `count_le(12) = 6` (1,5,9,10,11,12). `6 < 8` → `lo = 13`.
- `mid = 14`: `count_le(14) = 8` (adds 13,13,12... = 1,5,9,10,11,12,13,13). `8 >= 8`
  → `hi = 14`.
- `mid = 13`: `count_le(13) = 8`. `8 >= 8` → `hi = 13`.
- Now `lo = hi = 13` → return **13**. Matches expected output.

### Complexity

- **Time:** `O(n · log(hi - lo))`. Each `count_le` is `O(n)` (staircase walk), and
  binary search runs `O(log(range))` iterations. With `n <= 300` and a `2·10^9`
  value range, this is about `300 · 31` cell visits.
- **Space:** `O(1)` beyond the input.

## Key Insights & Edge Cases

- **Search the value, not an index.** The matrix is not globally sorted, so there
  is no single array to bisect — but the *value axis* is monotone for `count_le`.
- **Duplicates count individually.** `count_le` counts every entry `<= x`,
  including repeats, so Example 3 correctly returns `1` for `k = 2`.
- **Use `hi = mid` (not `mid - 1`)** when `count_le(mid) >= k`, because `mid`
  itself may be the answer. Getting this boundary right is the usual bug source.
- **`k = 1`** returns `matrix[0][0]`; **`k = n^2`** returns `matrix[n-1][n-1]`.
- The staircase `count_le` is a reusable primitive — the exact same routine powers
  Problem 5 over an implicit multiplication table.
