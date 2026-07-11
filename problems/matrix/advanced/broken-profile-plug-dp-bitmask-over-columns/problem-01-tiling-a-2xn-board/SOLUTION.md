# Solution — Tiling a 2×N Board

## Brute Force

Enumerate every way to place dominoes by backtracking over cells: at the first empty cell,
try a vertical domino, try a horizontal domino, recurse, and count complete coverings.

- **Time:** exponential — roughly `O(2^n)` distinct placement branches for a `2 × n` board.
- **Space:** `O(n)` recursion depth.

Fine for tiny `n`, hopeless for `n = 60`.

## Optimal Approach — Broken-Profile / Plug DP

### The frontier and its mask

Sweep the `2 × n` board **cell by cell** in row-major order: `(0,0), (0,1), …, (0,n-1),
(1,0), …`. Wait — for tiling problems it is cleaner to sweep **column by column**, and
within a column, top cell then bottom cell. Because the board is only 2 tall, a natural
and equivalent view processes the board **column by column with a 2-bit profile** that
says which cells of the *current* column are already filled by a horizontal domino that
started in the previous column.

We use the general cell-by-cell broken-profile formulation so it transfers directly to
wider boards later. Between processed and unprocessed cells sits a frontier that spans
`m = 2` columns, so a 2-bit mask describes it:

- **bit `j` = 1**: the cell just ahead of the frontier in column `j` is already occupied
  (a vertical domino placed one row earlier "plugs" down into it).
- **bit `j` = 0**: that cell is still empty.

### Transition at cell `(i, j)` with incoming mask

Let `k` be the linear index of `(i, j)` and let `mask` be the profile before processing it.

1. **Cell already filled** (`mask` has bit `j` set): a vertical domino from the row above
   covers it. Clear bit `j` and advance: `mask & ~(1<<j)`.
2. **Cell empty** (bit `j` clear), two choices:
   - **Vertical domino** covering `(i,j)` and `(i+1,j)`. Only if `i+1 < 2`. Set bit `j`:
     `mask | (1<<j)` — recording that the cell below is now filled.
   - **Horizontal domino** covering `(i,j)` and `(i,j+1)`. Only if `j+1 < m` and bit `j+1`
     is clear. Mark column `j+1` as filled on the frontier: `mask | (1<<(j+1))`.

Accumulate the incoming count into the new mask. The answer is the count of the empty
profile (`mask = 0`) after the last cell.

### Why it is correct

Every domino is anchored at its **topmost-then-leftmost** cell, so each tiling is counted
exactly once. The profile records *all* interaction between decided and undecided cells: a
piece can only reach one cell down or one cell right, both captured by the mask. Since the
future depends solely on the profile, summing counts over identical profiles loses no
information — this is the optimal-substructure/overlapping-subproblems condition for DP.

### Reference implementation

Here is the clean, self-contained broken-profile sweep. `cur` is the filled-mask of the
column being processed; `nxt` remembers which cells of the *next* column a horizontal
domino has already claimed. We process the two cells of a column, then roll forward.

```python
from functools import lru_cache

def count_tilings(n: int) -> int:
    @lru_cache(maxsize=None)
    def fill(col: int, row: int, cur: int, nxt: int) -> int:
        # cur = filled cells of current column; nxt = cells of next column claimed
        # by a horizontal domino started in this column.
        if row == 2:                                   # column finished
            if col + 1 == n:
                return 1 if nxt == 0 else 0            # last column must not owe anything
            return fill(col + 1, 0, nxt, 0)           # carry nxt -> cur of next column
        if cur & (1 << row):                          # already filled -> skip
            return fill(col, row + 1, cur, nxt)
        total = 0
        # vertical domino: fills (row, row+1) of the current column
        if row + 1 < 2 and not (cur & (1 << (row + 1))):
            total += fill(col, row + 2, cur | (1 << row) | (1 << (row + 1)), nxt)
        # horizontal domino: fills this cell now and the same row of the next column
        if col + 1 < n and not (nxt & (1 << row)):
            total += fill(col, row + 1, cur | (1 << row), nxt | (1 << row))
        return total

    return fill(0, 0, 0, 0)
```

This returns `1, 2, 3, 5, 8, …` for `n = 1, 2, 3, 4, 5` (the Fibonacci numbers), matching
the examples. The cell-by-cell row-major variant used in Problem 3 generalizes the same
`cur`/`nxt` bookkeeping into a single width-`m` profile integer.

- **Time:** `O(n · 2^2) = O(n)` — width-2 profile, constant states per column.
- **Space:** `O(n · 2^2)` for memoization, reducible to `O(1)` extra with rolling states.

## Key Insights & Edge Cases

- **Anchor rule kills double counting.** Only place a piece whose top-left-most cell is the
  current empty cell; this guarantees each tiling is enumerated once.
- **`n = 1`** → single vertical domino → answer `1`. The DP naturally yields this.
- **Parity:** a `2 × n` board always has an even number of cells, so a full tiling always
  exists; no board here is untileable.
- **Why bother with the mask for a Fibonacci problem?** The point is the *pattern*: the
  identical sweep with a width-`m` profile solves the `N × M` count (Problem 3) and boards
  with holes (Problem 4) with almost no change — only the transition set widens.
- Always let the **profile span the smaller dimension** (here rows = 2) to keep `2^width`
  tiny.
