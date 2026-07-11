# Solution — Row with Maximum Number of 1s

## Brute Force

Count the `1`s in every row and track the maximum.

```python
best_row, best_count = -1, 0
for i, row in enumerate(mat):
    ones = sum(row)
    if ones > best_count:
        best_count, best_row = ones, i
return best_row
```

- **Time:** `O(m · n)`.
- **Space:** `O(1)`.

Because each row is sorted, you can binary-search each row for the first `1`
instead of summing: `O(m · log n)`. Better, but still per-row and it does not
exploit relationships between rows. The staircase walk removes the `log`.

## Optimal Approach — Staircase / Saddleback Search

Each row is `0…0 1…1`, so the count of `1`s in a row equals `n - (index of its
first 1)`. The row with the most `1`s is the one whose **first `1` sits furthest
left**. A staircase walk finds that leftmost boundary in a single sweep.

Start at the **top-right** corner `(r, c) = (0, n - 1)` and keep `best = -1`:

1. **`mat[r][c] == 1`** → this row has a `1` at least this far left, and it beats
   (or ties, favoring the smaller index we reached first) any row seen so far.
   Record `best = r` and push the frontier further left: `c -= 1`.
2. **`mat[r][c] == 0`** → this row has no `1` at column `c` or to its left of the
   current frontier, so it cannot improve on the current `best`. Drop down a row:
   `r += 1`.

Stop when `r == m` (past the last row) or `c < 0` (frontier walked off the left
edge — a full row of `1`s was found). Return `best`.

### Worked trace on Example 1

`n = 4`. Start at `(0, 3)`, `best = -1`.

| Step | (r, c) | mat[r][c] | Action | best |
|------|--------|-----------|--------|------|
| 1 | (0, 3) | 1 | one → best=0, c-- | 0 |
| 2 | (0, 2) | 0 | zero → r++ | 0 |
| 3 | (1, 2) | 1 | one → best=1, c-- | 1 |
| 4 | (1, 1) | 1 | one → best=1, c-- | 1 |
| 5 | (1, 0) | 0 | zero → r++ | 1 |
| 6 | (2, 0) | 0 | zero → r++ | 1 |
| 7 | (3, 0) | 0 | zero → r++ | 1 |
| — | r = 4 | — | stop | **1** |

Answer `1`, as expected.

### Reference implementation

```python
def rowWithMax1s(mat):
    m, n = len(mat), len(mat[0])
    r, c = 0, n - 1          # top-right corner
    best = -1
    while r < m and c >= 0:
        if mat[r][c] == 1:
            best = r          # this row reaches at least this far left
            c -= 1            # try to push the frontier further left
        else:
            r += 1            # this row can't beat current best; go down
    return best
```

### Why it is correct

The pointer `c` is the current best (leftmost) `1`-frontier. We only ever move it
left, and only when a row actually has a `1` there — so whenever `c` advances, the
row that caused it (`best`) genuinely has more `1`s than any previously recorded
row. When a cell is `0`, monotonicity within the row means every column `< c` in
that row is also `0` up to the frontier, so that row cannot have a `1` further left
than the current frontier; we discard it and move down. A row with fewer `1`s
(first `1` to the right of the frontier) shows a `0` at column `c` and is skipped
without updating `best`. The first row to reach the minimal frontier wins ties,
matching the "smallest index" rule.

Note this problem only requires each **row** to be sorted — the columns need not
be sorted. The staircase walk still works, illustrating that the technique needs
just enough monotonicity to eliminate a line per step.

### Complexity

- **Time:** `O(m + n)` — `c` only decreases (`≤ n` moves) and `r` only increases
  (`≤ m` moves).
- **Space:** `O(1)`.

## Key Insights & Edge Cases

- **No 1s anywhere** → `best` never updates and we return `-1`.
- **A full row of 1s** drives `c` to `-1`, ending the walk early — correct, since
  no row can have more than `n` ones.
- **Ties:** because we scan rows top-down and only move left on a strict advance of
  the frontier, the earliest (smallest-index) row that reaches the minimal
  frontier is the one recorded.
- The equivalent bottom-left start also works: move right on `0`, up on `1`.
- Same shape as counting problems (2, 4, 5): the walk converts a 2D scan into a
  monotone 1D frontier.
