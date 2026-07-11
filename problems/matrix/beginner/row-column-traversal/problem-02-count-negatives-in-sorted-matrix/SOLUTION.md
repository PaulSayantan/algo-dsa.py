# Solution — Count Negative Numbers in a Sorted Matrix

## Brute Force

Ignore the sortedness entirely and just look at every cell. Increment a counter each
time the value is negative.

```python
def countNegatives(self, grid: List[List[int]]) -> int:
    count = 0
    for i in range(len(grid)):          # outer: rows
        for j in range(len(grid[0])):   # inner: columns
            if grid[i][j] < 0:
                count += 1
    return count
```

- **Time:** O(m * n) — one visit per cell.
- **Space:** O(1).

With `m, n <= 100` this is at most 10,000 comparisons, so the plain traversal is fully
within limits. This is the intended Row/Column Traversal answer.

## Optimal Approach (Row/Column Traversal)

The traversal above already touches each cell exactly once, which is the minimum work
required to *count* arbitrary negatives if you make no use of ordering. Its correctness
is immediate: the counter is incremented once for, and only for, each negative cell, so
after the double loop it equals the total number of negatives.

**Step by step** on `[[3,2],[1,0]]`:

1. `grid[0][0]=3` (not < 0), `grid[0][1]=2` (not < 0) -> count stays 0.
2. `grid[1][0]=1` (not < 0), `grid[1][1]=0` (not < 0) -> count stays 0.
3. Return `0`.

- **Time:** O(m * n).
- **Space:** O(1).

### Faster staircase variant (uses the sorted property)

Because each row and column is non-increasing, in every row the negatives form a
suffix. Start at the top-right corner. If the current cell is negative, then everything
below it in that column is also negative, so add the whole remaining column and move
left; otherwise move down.

```python
def countNegatives(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0
    row, col = 0, n - 1
    while row < m and col >= 0:
        if grid[row][col] < 0:
            count += m - row     # this cell and all below it are negative
            col -= 1
        else:
            row += 1
    return count
```

- **Time:** O(m + n) — the pointer only ever moves left or down.
- **Space:** O(1).

## Key Insights & Edge Cases

- The plain Row/Column Traversal is O(m * n) and is the right tool to learn first; the
  staircase walk is the optimization the sortedness unlocks (O(m + n)).
- A single-cell grid such as `[[-1]]` must be handled — both approaches do, since the
  loops run at least once.
- "Negative" means strictly `< 0`; a `0` is **not** counted. Watch the comparison
  operator.
- Rows and columns are all non-empty (`m, n >= 1`), so `len(grid[0])` is safe.
