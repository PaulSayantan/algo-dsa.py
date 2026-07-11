# Solution — Spiral Matrix II

## Brute Force

Simulate with a direction vector and a `visited`/zero-initialized grid: start at
`(0, 0)` heading right and write `1, 2, 3, ...`; when the next cell is off-grid
or already filled (non-zero), rotate the direction clockwise. Stop after writing
`n^2`.

- **Time:** `O(n^2)` — each cell written once.
- **Space:** `O(n^2)` for the output (unavoidable); the "already filled" test
  reuses the grid itself, so no extra structure is strictly required, but the
  turn-on-collision logic is easier to get wrong than the boundary method.

## Optimal Approach (Spiral Traversal, writing mode)

This is the inverse of "Spiral Matrix": instead of *reading* cells into a list,
we *write* an incrementing counter into cells while walking the identical
four-boundary spiral.

Initialize an `n x n` grid of zeros, a counter `val = 1`, and boundaries
`top = left = 0`, `bottom = right = n - 1`. Each ring:

1. Left -> right along row `top`, writing `val++`; then `top += 1`.
2. Top -> bottom along column `right`, writing `val++`; then `right -= 1`.
3. Right -> left along row `bottom` (if `top <= bottom`), writing `val++`; then `bottom -= 1`.
4. Bottom -> top along column `left` (if `left <= right`), writing `val++`; then `left += 1`.

Loop while `val <= n * n` (equivalently, while `top <= bottom and left <= right`).

```python
def generateMatrix(n):
    grid = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    val = 1
    while top <= bottom and left <= right:
        for col in range(left, right + 1):     # top row
            grid[top][col] = val; val += 1
        top += 1
        for row in range(top, bottom + 1):     # right col
            grid[row][right] = val; val += 1
        right -= 1
        if top <= bottom:                      # bottom row
            for col in range(right, left - 1, -1):
                grid[bottom][col] = val; val += 1
            bottom -= 1
        if left <= right:                      # left col
            for row in range(bottom, top - 1, -1):
                grid[row][left] = val; val += 1
            left += 1
    return grid
```

**Why it's correct:** because `n` is fixed and the matrix is square, the counter
increases by exactly one per cell and the boundaries visit each cell once in
clockwise order — identical to the read-order of Spiral Matrix. So cell `k` in
the spiral receives value `k`.

- **Time:** `O(n^2)`.
- **Space:** `O(1)` extra beyond the required `n x n` output.

## Key Insights & Edge Cases

- **Square matrix simplifies things.** Since `m == n`, you could even drop the
  bottom/left guards for `n >= 2`, but keeping them makes `n == 1` and any reuse
  on rectangular grids safe.
- **`n == 1`:** the top-row pass writes `grid[0][0] = 1`, then `top` exceeds
  `bottom` and the loop stops. Output `[[1]]`.
- **Center cell of odd `n`:** for `n = 3` the value `9` (= `n^2`) is written by
  the fourth pass reaching the center — verify it is not skipped by an
  over-eager guard.
- **Off-by-one in reverse ranges** (`range(right, left - 1, -1)`) is the most
  common bug; test with `n = 4` where the inner `2 x 2` ring `13,14,15,16` must
  spiral correctly.
