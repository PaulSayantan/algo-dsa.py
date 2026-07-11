# Solution — Diagonal Traverse (LeetCode 498)

## Brute Force

Collect every anti-diagonal into its own list by scanning the whole matrix once per
diagonal (checking `i + j == d`), reverse alternate lists, then concatenate.

- **Time:** `O((m + n) * m * n)` because of the repeated full scans.
- **Space:** `O(m * n)` for the buckets and output.

Correct, but the repeated scanning is wasteful — we can group in a single pass.

## Optimal Approach (Diagonal / Zig-Zag Traversal)

**Key identity:** cells on the same anti-diagonal share `i + j`. There are
`m + n - 1` diagonals with ids `0 .. m + n - 2`.

**Plan:** build each diagonal top-to-bottom (increasing `i`), then decide its
emission direction from the parity of the diagonal id `d`:

- `d` even -> emit **bottom-to-top** (reverse) = the up-right sweep.
- `d` odd  -> emit **top-to-bottom** (as built) = the down-left sweep.

```python
def findDiagonalOrder(mat):
    m, n = len(mat), len(mat[0])
    res = []
    for d in range(m + n - 1):
        diag = []
        i_lo = max(0, d - (n - 1))
        i_hi = min(m - 1, d)
        for i in range(i_lo, i_hi + 1):
            diag.append(mat[i][d - i])   # j = d - i, built top-to-bottom
        if d % 2 == 0:
            diag.reverse()               # up-right on even diagonals
        res.extend(diag)
    return res
```

**Why the parity rule is correct.** The zig-zag must start at `(0,0)` moving
up-right. Diagonal `d0` has a single cell, so "up-right" just emits it. Diagonal
`d1` must go down-left, i.e. increasing `i` — that is exactly the top-to-bottom order
we built, so we leave odd diagonals untouched. Diagonal `d2` goes up-right again =
decreasing `i` = the reverse of the built list, so we reverse even diagonals. Since
directions strictly alternate and the parity of `d` alternates in lockstep, the
even/odd rule keeps the snake consistent for every diagonal.

**Trace on `[[1,2,3],[4,5,6],[7,8,9]]`:**

| `d` | built top-to-bottom | parity | emitted    |
|-----|---------------------|--------|------------|
| 0   | [1]                 | even   | 1          |
| 1   | [2, 4]              | odd    | 2, 4       |
| 2   | [3, 5, 7]           | even   | 7, 5, 3    |
| 3   | [6, 8]              | odd    | 6, 8       |
| 4   | [9]                 | even   | 9          |

Result: `[1, 2, 4, 7, 5, 3, 6, 8, 9]`. ✔

- **Time:** `O(m * n)` — with the tightened `i_lo..i_hi` window each cell is touched
  once; each `reverse` is linear in the diagonal length, summing to `O(m * n)`.
- **Space:** `O(min(m, n))` for one diagonal buffer, plus `O(m * n)` for the output.

### O(1)-buffer walking variant

You can avoid the per-diagonal list by simulating the walk with a direction flag,
moving `(i, j)` by `(-1, +1)` going up-right and `(+1, -1)` going down-left, and
"bouncing" off the walls. When you hit a wall you step to the start of the next
diagonal (right if possible, else down for the up-direction; down if possible, else
right for the down-direction). This emits directly into the result with `O(1)` extra
space but is fiddlier to get right than the bucket-and-reverse version.

## Key Insights & Edge Cases

- **Parity == direction.** Tying the emission direction to `d % 2` is what turns a
  plain diagonal scan into a zig-zag.
- **Single row / single column:** every diagonal has length 1, so reversing does
  nothing and the output is just the flattened matrix — no special case needed.
- **Which parity goes up?** LeetCode 498 starts up-right at the top-left, so *even*
  diagonals go up. If a problem starts the other way, swap the parity check.
- **Wall-bounce bugs** (in the `O(1)` variant): when moving up and you are already in
  the top row, prefer moving right before moving down; the symmetric care is needed
  for the down direction. Getting this order wrong duplicates or skips corner cells.
