# Solution — Count Negative Numbers in a Sorted Matrix

## Brute Force

Iterate over every cell and increment a counter when the value is negative.

```python
count = 0
for row in grid:
    for value in row:
        if value < 0:
            count += 1
return count
```

- **Time:** `O(m · n)`.
- **Space:** `O(1)`.

A per-row improvement: because each row is sorted non-increasing, binary-search
each row for the first negative → `O(m · log n)`. Correct, but ignores the column
structure. The staircase walk is `O(m + n)` and needs no `log`.

## Optimal Approach — Staircase / Saddleback Search

The matrix is sorted **non-increasing** along both axes, so all negatives sit in a
staircase-shaped block anchored at the bottom-right. We trace the border between
non-negatives and negatives.

Start at the **bottom-left** corner `(r, c) = (m - 1, 0)` and keep a running
`count`:

1. **`grid[r][c] < 0`** → since the row is sorted non-increasing (values only get
   smaller as `c` grows), *every* cell from `c` to the end of this row is also
   negative. Add `n - c` to `count`, then move **up** one row: `r -= 1`.
2. **`grid[r][c] >= 0`** → this cell is non-negative; because the column is sorted
   non-increasing (values get smaller downward), there is no negative at or above
   `(r, c)` in this column. Move **right** one column: `c += 1`.

Stop when `r < 0` (walked off the top) or `c == n` (walked off the right edge).

### Worked trace on Example 1

`grid` is `4x4`, so `n = 4`. Start at `(3, 0)`.

| Step | (r, c) | grid[r][c] | Action | count |
|------|--------|-----------|--------|-------|
| 1 | (3, 0) | -1 | negative → add `4 - 0 = 4`, r-- | 4 |
| 2 | (2, 0) | 1 | non-neg → c++ | 4 |
| 3 | (2, 1) | 1 | non-neg → c++ | 4 |
| 4 | (2, 2) | -1 | negative → add `4 - 2 = 2`, r-- | 6 |
| 5 | (1, 2) | 1 | non-neg → c++ | 6 |
| 6 | (1, 3) | -1 | negative → add `4 - 3 = 1`, r-- | 7 |
| 7 | (0, 3) | -1 | negative → add `4 - 3 = 1`, r-- | 8 |
| — | r = -1 | — | stop | **8** |

Matches the expected output `8`.

### Reference implementation

```python
def countNegatives(grid):
    m, n = len(grid), len(grid[0])
    r, c = m - 1, 0          # bottom-left corner
    count = 0
    while r >= 0 and c < n:
        if grid[r][c] < 0:
            count += n - c   # rest of this row is negative too
            r -= 1
        else:
            c += 1
    return count
```

### Why it is correct

The bottom-left corner is the *smallest* value in its row and the *largest* in its
column. When we see a negative there, monotonicity guarantees the whole tail of
the row is negative, so we can count `n - c` cells in one shot and never revisit
that row. When we see a non-negative, everything above it in the column is `>=`
it, hence non-negative, so we safely skip the entire column above and move right.
Each row contributes its negatives exactly once.

### Complexity

- **Time:** `O(m + n)` — `r` only decreases and `c` only increases.
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **Non-increasing** order (largest first) is the mirror of the classic ascending
  Young tableau, so the natural corner here is the **bottom-left**. Starting
  top-right also works but you would count `m - r` down a column instead.
- Counting `n - c` (not just `1`) per negative cell is what collapses the work to
  a single pass — the key difference from a plain search.
- All-negative matrix → answer is `m * n`; all-non-negative → answer is `0`. The
  walk handles both without special cases.
- `1 x 1` grids: one comparison decides the count.
