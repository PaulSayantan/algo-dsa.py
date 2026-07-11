# Surrounded Regions — Solution

## Brute Force

For each `'O'`, run a search to determine whether its region touches the border;
if it does not, flip the whole region. Restarting a search per `'O'` region
without sharing work (or re-scanning repeatedly) is quadratic in the worst case.

- **Time:** `O((m * n)^2)` worst case.
- **Space:** `O(m * n)`.

## Optimal Approach (Flood Fill from the borders)

The trick is identical in spirit to Number of Enclaves: it is hard to directly
find "surrounded" regions, but easy to find the **safe** ones — the `'O'`s
connected to the border. So:

1. **Mark safe cells.** For every `'O'` on the four borders, flood-fill its
   connected `'O'` region and mark each cell with a temporary sentinel such as
   `'#'`.
2. **Sweep and flip.** Traverse the whole board:
   - Any remaining `'O'` was never reached from the border → it is surrounded →
     flip to `'X'`.
   - Any `'#'` was safe → restore to `'O'`.

Why it is correct: an `'O'` survives iff its region touches the border. The
border-seeded fills mark exactly the union of all border-connected `'O'` regions
(reachability through `'O'`s is symmetric), so unmarked `'O'`s are precisely the
surrounded ones.

### Step by step

```python
def solve(self, board):
    if not board or not board[0]:
        return
    m, n = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            return
        board[r][c] = '#'  # mark safe
        dfs(r + 1, c); dfs(r - 1, c)
        dfs(r, c + 1); dfs(r, c - 1)

    # 1. flood from border 'O's
    for r in range(m):
        dfs(r, 0); dfs(r, n - 1)
    for c in range(n):
        dfs(0, c); dfs(m - 1, c)

    # 2. flip surrounded, restore safe
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'
```

- **Time:** `O(m * n)` — border seeding plus fills touch each cell a constant
  number of times, and the final sweep is one pass.
- **Space:** `O(m * n)` worst-case traversal depth. The sentinel avoids a
  separate visited matrix.

## Key Insights & Edge Cases

- **Mark safe, then invert.** Do not try to detect surrounded regions directly;
  seed the fill from the border and everything unmarked at the end is surrounded.
- **Use a sentinel** (`'#'`) so you can distinguish "safe `'O'`" from "surrounded
  `'O'`" in the final sweep, then restore it.
- **Border `'O'`s are always safe**, including single border `'O'`s with no
  neighbors.
- **Tiny boards** (`1 x 1`, or a single row/column): every `'O'` is on the border
  and therefore safe — nothing is captured.
- Prefer iterative BFS/DFS for `200 x 200` boards to avoid recursion limits.
