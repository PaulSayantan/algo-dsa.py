# Solution — Parquet Tiling with Holes

## Brute Force

Backtrack over free cells: at the first uncovered free cell, try a vertical or horizontal
domino onto adjacent free cells, recurse, and count complete coverings. Holes are simply
skipped.

- **Time:** exponential, `O(2^(free cells))` in the worst case.
- **Space:** `O(n·m)` recursion depth.

Fine for tiny boards, hopeless near `12 × 12`.

## Optimal Approach — Broken-Profile / Plug DP

This is Mondriaan's Dream (Problem 3) plus obstacles. The only new idea is how a hole
participates in the cell-by-cell sweep.

### State

Sweep the grid cell by cell in row-major order with a width-`m` profile:

- **bit `j` = 1**: the cell about to be processed in column `j` is already occupied by a
  vertical domino from the row above.
- **bit `j` = 0**: that cell is still empty.

Transpose so the profile spans the **smaller** dimension.

### Handling a hole

Treat a hole `(i,j)` as a cell that must be *left uncovered*:

- We must **not** have a vertical domino from above landing on it. So if the incoming mask
  has bit `j` set (something from above claimed this cell), that state is **invalid** and is
  dropped — a vertical domino that would end on a hole was illegal to place.
- We place **nothing** on the hole and it protrudes **nothing** downward, so the mask passes
  through unchanged (with bit `j` staying `0`).

Concretely, at a hole we keep only states with bit `j` clear and forward them with the same
mask.

### Transition at a free cell `(i, j)`

Identical to the hole-free count, with neighbor cells required to be free:

- **Filled from above** (`mask & bit`): clear the bit → `mask ^ bit`.
- **Empty:**
  - **Vertical domino** if `i+1 < n` and `(i+1,j)` is free → `mask | bit`.
  - **Horizontal domino** if `j+1 < m`, bit `j+1` clear, and `(i,j+1)` is free →
    `mask | (bit << 1)`.

The answer is `dp[0]` after the final cell.

### Why it is correct

Anchoring each domino at its first row-major free cell counts every tiling once. Dropping
states where a vertical domino would land on a hole enforces "holes stay empty"; forwarding
the mask untouched over a hole models "the hole covers itself and pushes nothing down."
Everything else — profile semantics, the requirement that the terminal profile be `0` —
carries over verbatim from Mondriaan's Dream, so the DP remains sound and complete.

### Reference implementation

```python
from collections import defaultdict
from typing import List

def count_tilings(grid: List[str]) -> int:
    n, m = len(grid), len(grid[0])
    blocked = [[grid[i][j] == '#' for j in range(m)] for i in range(n)]
    if n < m:                                   # profile over the smaller side
        blocked = [[blocked[i][j] for i in range(n)] for j in range(m)]
        n, m = m, n
    if sum(not blocked[i][j] for i in range(n) for j in range(m)) % 2:
        return 0                                # odd number of free cells

    dp = defaultdict(int)
    dp[0] = 1
    for i in range(n):
        for j in range(m):
            nd = defaultdict(int)
            bit = 1 << j
            for mask, cnt in dp.items():
                if blocked[i][j]:               # hole: must be uncovered
                    if not (mask & bit):        # a vertical domino from above would be illegal
                        nd[mask] += cnt
                    continue
                if mask & bit:                  # covered from above
                    nd[mask ^ bit] += cnt
                else:
                    if i + 1 < n and not blocked[i + 1][j]:                 # vertical
                        nd[mask | bit] += cnt
                    if j + 1 < m and not (mask & (bit << 1)) and not blocked[i][j + 1]:
                        nd[mask | (bit << 1)] += cnt                         # horizontal
            dp = nd
    return dp[0]
```

Verified: `36` (no holes), `18` (two top-left holes), `5` (3×4 with two corner holes), and
`0` (mutilated 4×4) — matching all four examples.

### Complexity

- **Time:** `O(n · m · 2^m)` with `m = min(n, m)`.
- **Space:** `O(2^m)` for two rolling profile maps.

## Key Insights & Edge Cases

- **Illegal vertical onto a hole** is the crux: silently dropping states with `bit j` set at
  a hole is what forbids covering it. Forgetting this over-counts.
- **Parity / coloring pruning:** an odd free-cell count is instantly `0`; the mutilated-board
  example is `0` for the deeper checkerboard-coloring reason (each domino covers one cell of
  each color, but the two removed corners share a color).
- **Transpose first** so `2^m` uses the smaller dimension — critical when, say, `n = 12,
  m = 3`.
- **A fully blocked board** (all `#`) has `free = 0`, which is even, and the sweep forwards
  `dp[0] = 1` — one valid (empty) tiling.
- **Neighbor checks** (`not blocked[...]`) are what keep dominoes off holes; without them a
  domino could straddle a hole.
- Same skeleton as Problem 3; only the per-cell branch set changed. That reusability is the
  whole point of the broken-profile pattern.
