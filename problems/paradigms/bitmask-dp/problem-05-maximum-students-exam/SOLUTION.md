# Maximum Students Taking Exam — Solution

## Brute Force

Enumerate every subset of the good seats across the whole grid (`2^(m*n)`
possibilities), check all adjacency and diagonal constraints, and keep the
largest valid subset.

- **Time:** `O(2^(m*n) * m * n)`. With `m = n = 8` that is `2^64` subsets —
  utterly infeasible.
- **Space:** `O(m * n)`.

The constraints only ever link a seat to seats **in its own row** (left/right)
and **in the row directly above** (upper-left/upper-right). Nothing couples a
row to rows two or more above it. That locality is exactly what row-by-row
bitmask DP exploits.

## Optimal Approach (Row-by-row profile Bitmask DP)

### Encode each row as a mask

For a row with `n <= 8` columns, a seating choice is an `n`-bit integer `mask`
where bit `c` set means "a student sits in column `c`."

Precompute, per row `r`, the seats that are **broken** as a mask `broken[r]`
(bit `c` set means seat `(r, c)` is `'#'`).

A `mask` is **valid within row `r`** iff:

1. **Only good seats used:** `mask & broken[r] == 0`.
2. **No horizontal adjacency:** `mask & (mask << 1) == 0` (no two set bits are
   side by side).

### Compatibility between consecutive rows

Let `prev` be the seating mask of row `r-1` and `cur` be a valid mask of
row `r`. The diagonal-front rule says a student in `cur` at column `c` conflicts
with a student in `prev` at column `c-1` (upper-left) or column `c+1`
(upper-right). Expressed with bit shifts, `prev` and `cur` are **compatible**
iff:

```
cur & (prev << 1) == 0    # no upper-left conflict
cur & (prev >> 1) == 0    # no upper-right conflict
```

(There is no restriction on a student being directly above another — the "front
and behind" seats are allowed.)

### DP definition

Let `dp[r][mask]` = the maximum number of students seated in rows `0..r` such
that row `r`'s seating is exactly `mask` (a valid within-row mask).

- **Base case (row 0):** `dp[0][mask] = popcount(mask)` for every valid `mask`.
- **Transition:** for each valid `cur` in row `r` and each valid `prev` in
  row `r-1` that is compatible with `cur`:

  ```
  dp[r][cur] = max(dp[r][cur], dp[r-1][prev] + popcount(cur))
  ```

- **Answer:** `max(dp[m-1][mask])` over all valid masks of the last row.

Only the previous row matters, so keep two rolling maps of size `2^n`.

### Why it is correct

The cheating relation only connects a seat to its own row and the row above, so
a full valid seating is valid **iff** every row's mask is internally valid and
every adjacent pair of row masks is compatible. The DP considers exactly these
constraints layer by layer and maximizes the running student count; by optimal
substructure, the best arrangement for rows `0..r` ending in `cur` extends some
best arrangement for rows `0..r-1` ending in a compatible `prev`.

### Reference implementation

```python
class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        broken = []
        for r in range(m):
            b = 0
            for c in range(n):
                if seats[r][c] == '#':
                    b |= (1 << c)
            broken.append(b)

        full = 1 << n

        def valid(mask, r):
            if mask & broken[r]:          # sits on a broken seat
                return False
            if mask & (mask << 1):        # horizontal neighbours
                return False
            return True

        NEG = float("-inf")
        prev_dp = {0: 0}                  # "row -1": empty, 0 students
        for r in range(m):
            cur_dp = {}
            for mask in range(full):
                if not valid(mask, r):
                    continue
                best = NEG
                for pmask, pval in prev_dp.items():
                    if mask & (pmask << 1):   # upper-left conflict
                        continue
                    if mask & (pmask >> 1):   # upper-right conflict
                        continue
                    if pval > best:
                        best = pval
                if best == NEG:
                    continue
                cur_dp[mask] = best + bin(mask).count("1")
            prev_dp = cur_dp if cur_dp else {0: max(prev_dp.values())}
        return max(prev_dp.values())
```

- **Time:** `O(m * 4^n)` — for each of `m` rows, up to `2^n` current masks each
  paired with up to `2^n` previous masks. With `n = 8`: `m * 65536`, tiny.
  (Restricting to horizontally-valid masks shrinks this a lot in practice.)
- **Space:** `O(2^n)` per rolling layer.

## Key Insights & Edge Cases

- **Mask per row, not per grid.** The universe for the bitmask is a single
  row's columns (`<= 8`), so states are `2^n`, not `2^(m*n)`.
- **Shift tricks encode the geometry.** `mask & (mask << 1)` detects horizontal
  neighbours; `cur & (prev << 1)` / `cur & (prev >> 1)` detect the two diagonal
  fronts. Directly-above seats are intentionally allowed.
- **Broken seats** are filtered by `mask & broken[r] == 0`; a row can even be
  entirely broken (only the empty mask `0` is valid there).
- **Empty mask is always valid**, letting a row seat nobody — important when a
  row is fully broken or when skipping a row yields a better global optimum.
- **Rolling arrays** keep memory at `O(2^n)`; you never need all `m` layers at
  once because only the immediately previous row constrains the current one.
- **`popcount` via `bin(mask).count("1")`** (or precomputed) gives each mask's
  student count.
