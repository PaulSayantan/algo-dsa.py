# Solution — Spiral Matrix III

## Brute Force

You might try to precompute the four shrinking boundaries as in Spiral Matrix,
but that fails here: the start cell is arbitrary and the spiral grows *outward*,
often extending past the grid on some sides before others. A naive fix — testing
every one of the (up to `(2*max(rows,cols))^2`) lattice points against the grid
and sorting them by spiral index — is awkward and error-prone.

- **Time:** effectively `O(max(rows, cols)^2)` positions examined.
- **Space:** `O(rows * cols)` for the output.

The clean way is to simulate the outward spiral directly, which has the same
asymptotic cost but is far simpler to reason about.

## Optimal Approach (outward-growing Spiral Traversal)

The outward spiral has a beautiful regularity. Facing east and turning
clockwise (east -> south -> west -> north), the number of steps you take before
each turn follows the pattern:

```
1, 1, 2, 2, 3, 3, 4, 4, ...
```

That is: go 1 east, 1 south, 2 west, 2 north, 3 east, 3 south, 4 west, 4 north,
and so on. The step length increases by one after **every two** direction
changes.

Algorithm:

1. Record the start cell `(rStart, cStart)`.
2. Keep a direction index into `[(0,1), (1,0), (0,-1), (-1,0)]` (E, S, W, N),
   and a current `step` length starting at 1.
3. Repeat: for two consecutive directions, walk `step` cells one at a time;
   after each unit move, if the new cell is inside the grid, record it. After
   those two directions, increment `step` by 1.
4. Stop as soon as the output holds `rows * cols` cells.

```python
def spiralMatrixIII(rows, cols, rStart, cStart):
    res = [[rStart, cStart]]
    total = rows * cols
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # E, S, W, N
    r, c, step, d = rStart, cStart, 1, 0
    while len(res) < total:
        for _ in range(2):                      # two directions per step size
            dr, dc = dirs[d]
            for _ in range(step):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            d = (d + 1) % 4
        step += 1
    return res
```

**Why the `1,1,2,2,...` pattern is correct:** each outward ring adds one cell of
"reach" on each side. Going east then south covers the new right and bottom
edges of the enlarged square at the current step length; the next west and north
passes (one longer, hence the increment after two turns) cover the new left and
top edges. Every grid cell is eventually enclosed, so the loop terminates once
all `rows * cols` cells are collected.

- **Time:** `O(max(rows, cols)^2)` — the spiral may wander outside the grid, so
  it takes up to about `(2 * max(rows, cols))^2` unit moves, but only `rows *
  cols` of them are recorded.
- **Space:** `O(1)` extra beyond the required output list.

## Key Insights & Edge Cases

- **Two directions per step length.** The single most common bug is incrementing
  `step` after every direction instead of after every *two* directions. The
  inner `for _ in range(2)` is what enforces the `1,1,2,2,...` cadence.
- **Record inside the inner loop, one cell at a time.** You must bounds-check
  each unit move, not just the endpoint of a run, because a single run can dip
  in and out of the grid.
- **Start cell counts immediately** and is added before the loop; do not
  re-add it.
- **Single cell** `rows = cols = 1`: `res` already has the start cell and
  `len(res) == total`, so the loop body never runs.
- **Start in a corner** (e.g. `(0,0)`): the first westward/northward passes go
  fully out of bounds and record nothing, but the walk still eventually sweeps
  the whole grid — Example 3 confirms `2 x 2` from `(0,0)` yields all four cells.
- **Termination is guaranteed** because `step` grows without bound, so the spiral
  must eventually enclose the entire grid.
