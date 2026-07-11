# Solution — Maximum Dominoes on a Grid with Obstacles

## Brute Force

Backtrack over free cells: at the first cell, either leave it empty or place a domino onto a
free neighbor, recurse, and track the best count. Alternatively, model the free cells as a
bipartite graph (checkerboard coloring) and run maximum bipartite matching.

- **Backtracking time:** exponential, `O(3^(free cells))` in the worst case.
- **Matching time:** `O(V·E)` with Hopcroft–Karp / Hungarian on the grid graph — polynomial,
  but heavier to implement than the DP for small grids.

## Optimal Approach — Broken-Profile / Plug DP (with `max`)

The maximum number of dominoes equals the maximum matching of the "free-cell adjacency"
grid graph. On a narrow grid the broken-profile sweep computes it directly, changing only two
things versus the tiling **count**: we store a **maximum** (not a sum) per profile, and we add
a **"leave this cell uncovered"** transition so partial packings are legal.

### State

Sweep cell by cell in row-major order over a width-`m` profile (`m = min(n, m)`), where

- **bit `j` = 1**: the cell about to be processed in column `j` is already covered by a
  vertical domino from the row above,
- **bit `j` = 0**: it is not.

`dp[mask]` = the **maximum** number of dominoes placed among all decisions made for cells
before the current one, consistent with frontier `mask`. Unreachable profiles hold `-∞`.

### Transition at cell `(i, j)`

Let `bit = 1 << j`.

- **Blocked cell:** it cannot be covered. Any state with `bit` set is invalid (a vertical
  domino from above would land on it), so drop it; forward states with `bit` clear unchanged.
- **Free cell already covered from above** (`mask & bit`): clear the bit, value unchanged →
  `dp'[mask ^ bit] = max(..., dp[mask])`.
- **Free and empty** (`bit` clear) — three choices:
  1. **Leave it uncovered:** value unchanged → `dp'[mask] = max(..., dp[mask])`.
  2. **Vertical domino** if `i+1 < n` and `(i+1,j)` free: `dp'[mask | bit] = max(..., dp[mask] + 1)`.
  3. **Horizontal domino** if `j+1 < m`, bit `j+1` clear, `(i,j+1)` free:
     `dp'[mask | (bit << 1)] = max(..., dp[mask] + 1)`.

The answer is `dp[0]` after the last cell.

### Why it is correct

Anchoring each domino at its first row-major free cell means every placement configuration is
generated exactly once, and the added "leave uncovered" branch makes the search range over
*all* partial packings — so the true optimum is reachable. Because the profile fully captures
how the processed region constrains the unprocessed region (a piece reaches only right or
down), two states with equal profile are interchangeable and keeping only the larger value is
safe (an exchange/dominance argument): any completion of the smaller-valued state is also a
completion of the larger-valued one with an equal-or-greater total. Taking `max` therefore
never discards an optimum.

### Reference implementation

```python
from collections import defaultdict
from typing import List

def max_dominoes(grid: List[str]) -> int:
    NEG = float("-inf")
    n, m = len(grid), len(grid[0])
    blocked = [[grid[i][j] == '#' for j in range(m)] for i in range(n)]
    if n < m:                                   # profile over the smaller side
        blocked = [[blocked[i][j] for i in range(n)] for j in range(m)]
        n, m = m, n

    dp = defaultdict(lambda: NEG)
    dp[0] = 0
    for i in range(n):
        for j in range(m):
            nd = defaultdict(lambda: NEG)
            bit = 1 << j
            for mask, val in dp.items():
                if val == NEG:
                    continue
                if blocked[i][j]:               # obstacle: never covered
                    if not (mask & bit):
                        nd[mask] = max(nd[mask], val)
                    continue
                if mask & bit:                  # covered from above
                    nd[mask ^ bit] = max(nd[mask ^ bit], val)
                else:
                    nd[mask] = max(nd[mask], val)                     # leave empty
                    if i + 1 < n and not blocked[i + 1][j]:           # vertical (+1)
                        nd[mask | bit] = max(nd[mask | bit], val + 1)
                    if j + 1 < m and not (mask & (bit << 1)) and not blocked[i][j + 1]:
                        nd[mask | (bit << 1)] = max(nd[mask | (bit << 1)], val + 1)  # horizontal (+1)
            dp = nd
    return dp[0]
```

Verified: `max_dominoes(["...","..."]) = 3`, `(["...",".#."]) = 2`,
`(["#..",".#.","..#"]) = 2`, and a `4×4` empty board `= 8` — matching all examples.

### Complexity

- **Time:** `O(n · m · 2^m)` with `m = min(n, m)`.
- **Space:** `O(2^m)` for two rolling profile maps.

## Key Insights & Edge Cases

- **`max` vs `sum`** is the whole change from a counting DP: swap the aggregation and seed
  unreachable states with `-∞`.
- **The extra "leave empty" branch** is essential — without it you would only count *perfect*
  tilings and report `-∞`/failure whenever the free region cannot be fully packed.
- **This equals maximum bipartite matching** on the grid graph (König's theorem territory);
  the broken-profile DP is the simplest route when a grid dimension is `≤ ~16`.
- **All-blocked or single-cell boards** yield `0`; the DP forwards `dp[0] = 0`.
- **Obstacles** are handled exactly as in Problem 4: forbid vertical dominoes landing on them
  and require neighbor cells to be free.
- **Transpose to the smaller dimension** first to keep `2^m` tiny.
