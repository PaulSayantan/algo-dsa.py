# Solution — Difference of Distinct Values on Diagonals (LeetCode 2711)

## Brute Force

For every cell `(r, c)`, walk up-left collecting distinct values into a set and walk
down-right collecting distinct values into another set, then take the absolute
difference of the two set sizes.

```python
def differenceOfDistinctValues(grid):
    m, n = len(grid), len(grid[0])
    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            top = set()
            x, y = i - 1, j - 1
            while x >= 0 and y >= 0:
                top.add(grid[x][y]); x -= 1; y -= 1
            bot = set()
            x, y = i + 1, j + 1
            while x < m and y < n:
                bot.add(grid[x][y]); x += 1; y += 1
            ans[i][j] = abs(len(top) - len(bot))
    return ans
```

- **Time:** `O(m * n * min(m, n))` — each cell walks a diagonal of length up to
  `min(m, n)`.
- **Space:** `O(min(m, n))` for the two sets (plus the output).

Given the constraints (`m, n <= 50`) this is already fast enough and is the cleanest
correct solution. It also *is* the diagonal-walking technique — the "optimal" version
below just removes redundant re-walking.

## Optimal Approach (Diagonal / Zig-Zag Traversal, prefix/suffix sets)

**Key identity:** all cells on one main diagonal share `i - j`. Process each diagonal
once, computing a **prefix set** of distinct values as you move down-right, so
`topLeft[r][c]` is the size of the prefix set *before* `(r, c)`. Then walk the same
diagonal backward to compute the **suffix set** for `bottomRight`.

Algorithm per diagonal (fix `i - j = k`, list its cells in order of increasing `i`):

1. Forward pass: keep a set `seen`. For each cell in order, record
   `topLeft = len(seen)` **then** add the cell's value to `seen`.
2. Backward pass: keep a set `seen`. For each cell in reverse order, record
   `bottomRight = len(seen)` **then** add the cell's value.
3. `answer = |topLeft - bottomRight|`.

```python
def differenceOfDistinctValues(grid):
    m, n = len(grid), len(grid[0])
    ans = [[0] * n for _ in range(m)]
    for k in range(-(n - 1), m):                 # each main diagonal i - j = k
        cells = [(i, i - k) for i in range(max(0, k), min(m, n + k))]
        seen = set()
        for (i, j) in cells:                      # forward: above-left
            ans[i][j] = len(seen)                 # topLeft count for now
            seen.add(grid[i][j])
        seen = set()
        for (i, j) in reversed(cells):            # backward: below-right
            ans[i][j] = abs(ans[i][j] - len(seen))
            seen.add(grid[i][j])
    return ans
```

**Why it is correct.** On a fixed diagonal, the cells above-left of `(r, c)` are
exactly those that come *before* it in increasing-`i` order, so the forward prefix
set (measured before inserting the current cell) is precisely `topLeft`. Symmetric-
ally, the cells below-right come *after* it, so the backward suffix set gives
`bottomRight`. Storing `topLeft` first and combining it with `bottomRight` during the
backward pass yields the required absolute difference in place.

**Trace on the diagonal `i - j = 0` of `[[1,2,3],[3,1,5],[3,2,1]]`** — cells
`(0,0)=1, (1,1)=1, (2,2)=1`:

- Forward: at `(0,0)` seen=∅ -> topLeft 0; add 1. At `(1,1)` seen={1} -> topLeft 1;
  add 1. At `(2,2)` seen={1} -> topLeft 1.
- Backward: at `(2,2)` seen=∅ -> bottomRight 0 -> `|1-0|=1`; add 1. At `(1,1)`
  seen={1} -> bottomRight 1 -> `|1-1|=0`; add 1. At `(0,0)` seen={1} -> bottomRight 1
  -> `|0-1|=1`.

So along the main diagonal `answer` is `1, 0, 1`, matching row-wise
`answer[0][0]=1, answer[1][1]=0, answer[2][2]=1`. ✔

- **Time:** `O(m * n)` — each cell is touched twice (one forward, one backward pass).
- **Space:** `O(min(m, n))` for the running set, plus the output matrix.

## Key Insights & Edge Cases

- **`i - j` groups the `\` diagonals**, ranging from `-(n-1)` to `m-1`. Getting these
  bounds right is the only tricky indexing part; the cell list
  `[(i, i-k)]` for valid `i` avoids manual boundary juggling.
- **Record-before-insert** is essential: `topLeft`/`bottomRight` must exclude the
  current cell itself (they count values *strictly* above-left / below-right).
- **Single cell / single row / single column:** every diagonal that matters has
  length 1, so both counts are 0 and the answer is 0 — handled with no special case.
- **Distinct, not total:** use a `set`, not a counter — duplicates on the diagonal
  collapse to one (see the all-`5` example).
