# Solution — Stamping the Grid

## Brute Force

For each candidate top-left `(r, c)`, scan the full `stampHeight x stampWidth`
window to check it contains no `1`; if clean, mark every cell it covers. Finally,
verify no empty cell was left uncovered.

```python
def possibleToStamp(grid, H, W):
    m, n = len(grid), len(grid[0])
    covered = [[False] * n for _ in range(m)]
    for r in range(m - H + 1):
        for c in range(n - W + 1):
            if all(grid[x][y] == 0
                   for x in range(r, r + H)
                   for y in range(c, c + W)):
                for x in range(r, r + H):
                    for y in range(c, c + W):
                        covered[x][y] = True
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not covered[i][j]:
                return False
    return True
```

- **Time:** `O(m * n * H * W)` — checking and marking each window is `O(H*W)`.
  Far too slow for `m * n` up to `2 * 10^5`.
- **Space:** `O(m * n)`.

## Optimal Approach (2D Prefix Sum + 2D Difference Array)

Two range-array tools working together:

**Step 1 — Feasibility via 2D prefix sum.** Build `ps`, the 2D prefix sum of the
*occupied* cells. Then the number of `1`s inside any rectangle is an O(1) query.
A stamp with top-left `(r, c)` and bottom-right `(r+H-1, c+W-1)` is placeable iff
that rectangle sum is `0` (no occupied cell inside) and it fits in the grid.

**Step 2 — Coverage via 2D difference array.** For every placeable stamp, we
must record that its whole rectangle is covered. Doing that cell-by-cell is
`O(H*W)` per stamp; instead stamp the rectangle into a 2D difference array with
the four-corner trick, which is O(1) per stamp:

```
diff[r][c]         += 1
diff[r][c2 + 1]    -= 1
diff[r2 + 1][c]    -= 1
diff[r2 + 1][c2+1] += 1     # r2 = r + H - 1, c2 = c + W - 1
```

**Step 3 — Materialize and check.** 2D-prefix-sum the difference array to get the
coverage count per cell. Every empty cell (`grid[i][j] == 0`) must have coverage
`>= 1`; if any empty cell has coverage `0`, return `false`.

```python
def possibleToStamp(grid, H, W):
    m, n = len(grid), len(grid[0])

    # Step 1: prefix sum of occupied cells.
    ps = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            ps[i + 1][j + 1] = grid[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

    def rect_sum(r1, c1, r2, c2):
        return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]

    # Step 2: stamp every valid placement into a 2D difference array.
    diff = [[0] * (n + 1) for _ in range(m + 1)]
    for r in range(m - H + 1):
        for c in range(n - W + 1):
            r2, c2 = r + H - 1, c + W - 1
            if rect_sum(r, c, r2, c2) == 0:      # window is all empty
                diff[r][c]           += 1
                diff[r][c2 + 1]      -= 1
                diff[r2 + 1][c]      -= 1
                diff[r2 + 1][c2 + 1] += 1

    # Step 3: materialize coverage and verify every empty cell is covered.
    cov = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            cov[i + 1][j + 1] = (diff[i][j] + cov[i][j + 1]
                                 + cov[i + 1][j] - cov[i][j])
            if grid[i][j] == 0 and cov[i + 1][j + 1] == 0:
                return False
    return True
```

- **Time:** `O(m * n)` — prefix sum, one pass over placements (each O(1)), and one
  pass to materialize/check.
- **Space:** `O(m * n)` for the prefix-sum and difference matrices.

**Why it is correct:** Since stamps may overlap freely, the *greedy* choice is to
place a stamp at every position where it legally fits (avoids all `1`s). This
maximizes coverage — any cell coverable by some valid stamp is covered by this
set. An empty cell is coverable iff at least one valid stamp overlaps it, which
is exactly `cov[i][j] >= 1`. The 2D difference array lets us accumulate that
coverage in O(1) per stamp, and the 2D prefix sum inverts it to the true
per-cell count.

## Key Insights & Edge Cases

- **Two prefix-sum systems, opposite directions.** One prefix sum answers a
  *query* (is this window clean?); the difference array + prefix sum performs a
  batch of *updates* (mark these rectangles covered). Recognizing that coverage
  is a range-update problem is the key leap that removes the `O(H*W)`-per-stamp
  cost.
- **Greedy is optimal here** precisely because stamps may overlap and are
  unlimited — there is never a reason *not* to place a legal stamp.
- **Stamp larger than the grid.** If `H > m` or `W > n`, the placement loops are
  empty, no cell gets covered, and the answer is `false` unless the grid has no
  empty cells at all — handled automatically.
- **Occupied cells are never required to be covered**; the final check only
  inspects cells where `grid[i][j] == 0`. Stamps also can't cover a `1` because
  we only place stamps on all-empty windows.
- **Consistent 1-based padding.** Both `ps` and `cov` use `(m+1) x (n+1)` arrays
  so all corner writes/reads stay in bounds; mixing 0-based and 1-based indexing
  between the two is a frequent source of bugs.
