# Solution — Mondriaan's Dream (N×M Domino Count)

## Brute Force

Backtrack over cells: at the first empty cell place a vertical or a horizontal domino,
recurse, and count complete coverings.

- **Time:** exponential, about `O(2^(n·m))` branches in the worst case.
- **Space:** `O(n·m)` recursion depth.

Impossible for a `12 × 12` board (144 cells).

## Optimal Approach — Broken-Profile / Plug DP

This is *the* canonical broken-profile problem. Sweep the grid **cell by cell in row-major
order** and carry a width-`m` bitmask describing the jagged boundary (the "broken profile")
between processed and unprocessed cells.

### State

`dp[mask]` = number of ways to have made all placement decisions for the cells strictly
before the current one, such that the frontier is described by `mask`, where

- **bit `j` = 1**: the cell about to be processed in column `j` is already occupied by a
  **vertical domino** that started one row up.
- **bit `j` = 0**: that cell is still empty.

Orient the sweep so the profile spans the **smaller** side: swap `n, m` if `n < m`, keeping
`2^m` small.

### Transition at cell `(i, j)`

Let `bit = 1 << j`.

- **Cell already filled** (`mask & bit`): a vertical domino from above covers it. Clear the
  bit and advance: new mask `mask ^ bit`.
- **Cell empty** (`bit` clear):
  - **Vertical domino** covering `(i,j)` and `(i+1,j)` — only if `i+1 < n`. New mask
    `mask | bit` (records that the cell below is now occupied).
  - **Horizontal domino** covering `(i,j)` and `(i,j+1)` — only if `j+1 < m` and bit `j+1`
    is clear. New mask `mask | (bit << 1)` (marks column `j+1` so we skip it when we reach
    it this row; because a horizontal domino does not reach downward, that bit is cleared
    again when column `j+1` is processed, freeing the cell below it).

After all `n·m` cells, the answer is `dp[0]`: the empty profile means nothing protrudes past
the board.

### Why it is correct

Anchoring every domino at its first (row-major) uncovered cell makes each tiling appear
exactly once. A domino can only interact with the cell to its right or the cell below, and
both are recorded in the profile, so states with the same mask are indistinguishable for the
future and their counts combine soundly. Demanding the final profile be `0` rejects any
tiling that would push a domino off the board.

### Reference implementation

```python
from collections import defaultdict

def count_tilings(n: int, m: int) -> int:
    if (n * m) % 2 == 1:          # odd area -> impossible
        return 0
    if n < m:                     # keep the profile over the smaller dimension
        n, m = m, n

    dp = defaultdict(int)
    dp[0] = 1
    for i in range(n):
        for j in range(m):
            nd = defaultdict(int)
            bit = 1 << j
            for mask, cnt in dp.items():
                if mask & bit:                       # filled from above -> now free below
                    nd[mask ^ bit] += cnt
                else:
                    if i + 1 < n:                    # vertical domino
                        nd[mask | bit] += cnt
                    if j + 1 < m and not (mask & (bit << 1)):   # horizontal domino
                        nd[mask | (bit << 1)] += cnt
            dp = nd
    return dp[0]
```

Verified outputs: `count_tilings(2,2)=2`, `(3,3)=0`, `(3,4)=11`, `(4,4)=36`,
`(8,8)=12988816`, `(6,6)=6728` — all matching the examples.

### Complexity

- **Time:** `O(n · m · 2^m)` with `m = min(n, m)` — each of the `n·m` cells sweeps up to
  `2^m` masks with `O(1)` work.
- **Space:** `O(2^m)` for two rolling profile maps.

For `12 × 12`, that is `144 · 4096 ≈ 6 × 10^5` mask-visits — instant.

## Key Insights & Edge Cases

- **Odd area** (`n·m` odd) → `0` immediately; the `3×3` example is exactly this.
- **Always sweep the smaller dimension** so `2^m` stays small; the swap is the single most
  important optimization.
- **The horizontal-domino bit** is set on column `j+1` and *cleared* when that column is
  processed in the same row — this is what encodes "occupied here but not below."
- **Empty board / `n = m = 0`** yields `1` (one empty tiling); the loop simply never runs and
  `dp[0] = 1`.
- The exact same skeleton, with the transition set extended, solves tromino tilings and
  boards with holes (see Problems 2 and 4).
- **Result size:** `12 × 12` gives `53,060,477,521,960,000`, which still fits in a signed
  64-bit integer; larger boards need big integers or a modulus.
