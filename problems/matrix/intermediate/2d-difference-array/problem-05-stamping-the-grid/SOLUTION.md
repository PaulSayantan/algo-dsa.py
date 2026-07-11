# Solution — Stamping the Grid

## Brute Force

For every candidate top-left corner, scan the stamp's `stampHeight x stampWidth`
window to check it contains no `1`. If it is clean, mark every cell of that
window as covered. Finally verify every empty cell is covered.

```python
for i in range(m - sh + 1):
    for j in range(n - sw + 1):
        if window_has_no_one(i, j):   # O(sh*sw)
            mark_window_covered(i, j) # O(sh*sw)
```

- **Time:** `O(m * n * stampHeight * stampWidth)` — checking and stamping each
  window cell-by-cell. With `m*n` up to `2 * 10^5` and large stamps this is far
  too slow.
- **Space:** `O(m*n)`.

Both the "is this window empty?" test and the "mark this window covered" step are
range operations, which is exactly what prefix sums and difference arrays make
`O(1)`.

## Optimal Approach (2D Prefix Sum + 2D Difference Array)

Two matrix layers work together:

### Layer 1 — where can a stamp legally go? (2D prefix sum of occupancy)

Build a prefix-sum table `ps` over the occupied (`1`) cells. For a stamp whose
top-left corner is `(i, j)`, its bottom-right corner is
`(i + sh - 1, j + sw - 1)`. The window is placeable iff:

- it fits inside the grid (`i + sh <= m` and `j + sw <= n`), and
- the rectangle sum of occupied cells inside it is `0` (queried in `O(1)` via the
  prefix-sum table).

### Layer 2 — accumulate coverage (2D difference array)

For each **legal** placement, add `+1` over its `sh x sw` rectangle using the
four-corner difference-array update (`O(1)` per placement). After processing all
placements, a 2D prefix sum over the difference matrix gives each cell's
stamp-coverage count.

### Final check

The grid is stampable iff **every empty cell has coverage `>= 1`**. Occupied
cells are ignored (they must not be covered, and by construction no legal stamp
covers them).

### Why it is correct

A cell is coverable iff *some* legal stamp overlaps it. We greedily place a stamp
at **every** legal top-left corner (overlaps are allowed and free), which is the
maximal possible coverage. If even this maximal coverage misses an empty cell,
no arrangement can cover it, so the answer is `false`. The difference array lets
us realize "place a stamp at every legal position" in `O(#positions)` instead of
`O(#positions * area)`.

### Reference implementation

```python
class Solution:
    def possibleToStamp(self, grid, sh, sw):
        m, n = len(grid), len(grid[0])

        # Layer 1: prefix sum of occupied cells (1-indexed padding)
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = (grid[i][j] + ps[i][j + 1]
                                    + ps[i + 1][j] - ps[i][j])

        # Layer 2: difference array of stamp coverage (padded by 2)
        diff = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(m - sh + 1):
            for j in range(n - sw + 1):
                x2, y2 = i + sh, j + sw          # exclusive corners
                occupied = ps[x2][y2] - ps[i][y2] - ps[x2][j] + ps[i][j]
                if occupied == 0:                # window is empty -> legal
                    diff[i + 1][j + 1]   += 1
                    diff[i + 1][y2 + 1]  -= 1
                    diff[x2 + 1][j + 1]  -= 1
                    diff[x2 + 1][y2 + 1] += 1

        # reconstruct coverage via 2D prefix sum and validate
        cover = [[0] * (n + 2) for _ in range(m + 2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cover[i][j] = (diff[i][j] + cover[i - 1][j]
                               + cover[i][j - 1] - cover[i - 1][j - 1])
                if grid[i - 1][j - 1] == 0 and cover[i][j] == 0:
                    return False
        return True
```

- **Time:** `O(m * n)` — building the prefix sum, iterating every candidate
  corner (`O(1)` work each), and one coverage sweep are all linear in the grid
  size.
- **Space:** `O(m * n)` for the two auxiliary tables.

## Key Insights & Edge Cases

- **Two composed techniques:** the prefix sum answers "can a stamp go here?" in
  `O(1)`; the difference array answers "which cells get covered?" in `O(1)` per
  placement. Neither alone is enough.
- **Greedy stamp-everywhere is optimal** because overlaps are permitted and free
  — maximal coverage is achievable simultaneously.
- **Fitting bounds:** iterate top-left corners only up to `m - sh` and `n - sw`
  so the stamp never leaves the grid. If a stamp is larger than the grid there
  are simply no legal placements, and any empty cell forces `false`.
- **Padding:** the difference array is padded by 2 (indices `y2 + 1` can reach
  `n + 1`), so allocate `(m + 2) x (n + 2)`.
- Coverage-count `> 0` is a boolean signal here (any positive count means
  "covered"); we never need the exact number of overlapping stamps.
- If the grid has **no empty cells**, the answer is trivially `true` (nothing to
  cover). If every cell is empty and stamps fit, it is `true`.
