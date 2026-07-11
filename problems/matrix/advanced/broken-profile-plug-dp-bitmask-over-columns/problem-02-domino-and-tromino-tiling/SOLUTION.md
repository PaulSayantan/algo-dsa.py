# Solution — Domino and Tromino Tiling (LeetCode 790)

## Brute Force

Backtrack over cells: at the first uncovered cell, try each legal piece (vertical domino,
horizontal domino, and the four L-tromino orientations that cover this cell), recurse, and
count complete coverings.

- **Time:** exponential in `n`, roughly `O(6^n)` in the worst branching.
- **Space:** `O(n)` recursion depth.

Correct but far too slow for `n = 1000`.

## Optimal Approach — Broken-Profile / Plug DP

### State: a per-column profile

Process the board **column by column**. Because a piece placed in column `c` can only
protrude one cell to the right (into column `c+1`), all the interaction between decided and
undecided columns is captured by a **2-bit profile**:

- `cur` — the mask of cells in the **current** column that are *already filled* by pieces
  that started in the previous column.
- `nxt` — the mask of cells in the **next** column that a piece started in the current
  column will fill.

`dp[cur]` = number of ways to have tiled columns `0 … c-1` completely and left exactly the
cells in `cur` of column `c` pre-filled.

### Transition — completely fill one column

For each incoming `cur`, enumerate every way to cover **all** the still-empty cells of the
current column, choosing which cells of the next column each piece pushes into. The pieces
that can cover the topmost empty cell `(row, c)`:

1. **Vertical domino** — fills both rows of the current column (needs both free).
2. **Horizontal domino** — fills `(row, c)` and `(row, c+1)`: sets bit `row` of `nxt`.
3. **L-tromino, both current cells + top of next** — fills the whole current column plus
   `(0, c+1)`.
4. **L-tromino, both current cells + bottom of next** — current column plus `(1, c+1)`.
5. **L-tromino, one current cell + both next cells** — fills `(row, c)` and both cells of
   the next column.

A column is a valid stopping point only when **all** its cells end up filled (`cur` becomes
`0b11`). Precompute `trans[cur]` = list of reachable `nxt` masks (there are only 4 possible
`cur` values). After processing all `n` columns, the answer is `dp[0]` — no debt pushed
past the last column.

### Why it is correct

Filling the current column greedily at its topmost empty cell anchors every piece uniquely,
so each global tiling is generated exactly once. The 2-bit `nxt` mask captures the *only*
way the current column can affect the future (a rightward protrusion), so states with equal
profiles are interchangeable — the DP soundly merges their counts. Requiring `cur == 0b11`
before advancing guarantees no cell is ever left uncovered.

### Reference implementation

```python
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        def transitions(cur: int) -> list[int]:
            out = []
            def rec(row: int, filled: int, nxt: int) -> None:
                if row == 2:
                    if filled == 0b11:          # column fully covered
                        out.append(nxt)
                    return
                bit = 1 << row
                if filled & bit:                # already covered -> next row
                    rec(row + 1, filled, nxt); return
                # 1) vertical domino
                if row == 0 and not (filled & 0b10):
                    rec(2, 0b11, nxt)
                # 2) horizontal domino -> pushes into next column
                if not (nxt & bit):
                    rec(row + 1, filled | bit, nxt | bit)
                # 3) L: both current cells + top of next column
                if row == 0 and not (filled & 0b10) and not (nxt & 0b01):
                    rec(2, 0b11, nxt | 0b01)
                # 4) L: both current cells + bottom of next column
                if row == 0 and not (filled & 0b10) and not (nxt & 0b10):
                    rec(2, 0b11, nxt | 0b10)
                # 5) L: this current cell + both next-column cells
                if (nxt & 0b11) == 0:
                    rec(row + 1, filled | bit, 0b11)
            rec(0, cur, 0)
            return out

        trans = {cur: transitions(cur) for cur in range(4)}
        dp = {0: 1}
        for _ in range(n):
            nd = {}
            for cur, w in dp.items():
                for nxt in trans[cur]:
                    nd[nxt] = (nd.get(nxt, 0) + w) % MOD
            dp = nd
        return dp.get(0, 0) % MOD
```

Verified: it returns `1, 2, 5, 11, 24, 53, 117, 258` for `n = 1 … 8`, matching the examples.

### Closed-form / classic recurrence (for reference)

The same counts satisfy `f(n) = 2·f(n-1) + f(n-3)` with `f(0)=1, f(1)=1, f(2)=2`. Many
editorial solutions derive that recurrence directly; the broken-profile DP *rediscovers* it
mechanically and generalizes to boards taller than 2 rows.

- **Time:** `O(n)` — a constant number of profiles (`≤ 4`) with `O(1)` transitions per
  column.
- **Space:** `O(1)` extra (two rolling profile maps).

## Key Insights & Edge Cases

- **`n = 1`** → only a vertical domino fits (a tromino needs 3 cells) → answer `1`.
- **`n = 2`** → answer `2`; trominoes cannot fill a `2 × 2` region without leaving a gap.
- **Modulus:** take `% (10^9 + 7)` on every addition to avoid overflow in languages with
  fixed-width integers.
- **The only difference from Problem 1** is the enrichment of the transition set with the
  four tromino placements; the sweep and the profile bookkeeping are identical.
- **Distinct-tiling rule:** two tilings differ iff some pair of adjacent cells is split by a
  tile in one but not the other — exactly what the anchored enumeration counts.
