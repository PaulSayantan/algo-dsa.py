# Solution — Largest All-Zero Submatrix

## Brute Force

Enumerate every candidate rectangle by its top-left `(r1, c1)` and bottom-right
`(r2, c2)` corners and test whether it is all zeros.

- Naively checking each rectangle cell-by-cell is O(n²m² · nm) = O(n³m³).
- With a 2D prefix-sum of the matrix you can test "is this rectangle all zeros?"
  in O(1) (its sum must be 0), bringing it down to **O(n²m²)** time and
  O(nm) space.

For a 200 x 200 grid, O(n²m²) is 1.6 * 10^9 — borderline and wasteful.

## Optimal Approach (Per-Row Heights + Histogram)

**Reduce the 2D problem to n independent 1D problems.**

For each row `i`, define a histogram over the columns:

```
height[j] = number of consecutive 0s in column j ending at row i (inclusive)
```

Update rule while scanning rows top to bottom:

```
if grid[i][j] == 0:  height[j] += 1
else:                height[j] = 0     # a 1 breaks the vertical run
```

**Claim.** The largest all-zero rectangle whose *bottom edge sits on row `i`* has
area equal to the **largest rectangle in the histogram `height[]`** for row `i`.

Why: a rectangle of all zeros ending on row `i` spanning columns `[l, r]` can
rise upward by exactly `min(height[l..r])` rows before hitting a `1`. That is
precisely a histogram rectangle over `[l, r]` with limiting height
`min(height[l..r])`. Every all-zero rectangle has *some* bottom row, so taking
the max of the histogram answer across all rows covers every rectangle.

So the algorithm is:

```python
def largest_all_zero_submatrix(grid):
    if not grid or not grid[0]:
        return 0
    m = len(grid[0])
    height = [0] * m
    best = 0
    for row in grid:
        for j in range(m):
            height[j] = height[j] + 1 if row[j] == 0 else 0
        best = max(best, _largest_rect_in_histogram(height))
    return best

def _largest_rect_in_histogram(heights):
    stack = []          # indices, non-decreasing heights
    best = 0
    for i in range(len(heights) + 1):
        h = heights[i] if i < len(heights) else 0   # sentinel
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            left = stack[-1] if stack else -1
            best = max(best, heights[top] * (i - left - 1))
        stack.append(i)
    return best
```

### Worked trace on Example 1

```
grid = [[0, 0, 1],
        [0, 0, 1],
        [0, 0, 0]]
```

- Row 0 `[0,0,1]` → height `[1,1,0]`. Best histogram rect = `1*2 = 2`.
- Row 1 `[0,0,1]` → height `[2,2,0]`. Best histogram rect = `2*2 = 4`.
- Row 2 `[0,0,0]` → height `[3,3,1]`. Columns 0-1 give `3*2 = 6`; adding col 2
  drops the limiting height to 1 → `1*3 = 3`. Best = `6`.

Overall max = **6**, matching the expected output.

- **Time:** O(n·m) — each cell updates one height in O(1), and each row's
  histogram pass is O(m) amortized via the monotonic stack.
- **Space:** O(m) for `height[]` and the stack.

## Key Insights & Edge Cases

- **All-zero vs. all-one.** This finds all-`0` rectangles. The identical
  algorithm on the *complement* (increment height on `1`, reset on `0`) solves
  "Maximal Rectangle" (LeetCode 85), the all-`1` version. Only the reset
  condition changes.
- **A single `1` resets the whole column height** — this is what makes the
  histogram reflect "distance up to the nearest blocking cell".
- **Reset, don't just skip.** If you forget to set `height[j] = 0` on a `1`, you
  would count zeros separated by a `1`, producing rectangles that are not
  actually all-zero.
- **No zeros** → every height stays 0 → answer `0`.
- **Single row / single column** are handled naturally (histogram of length `m`,
  or a 1-wide histogram evaluated `n` times).
- If you also need the rectangle's *coordinates*, record the row `i`, the
  limiting height, and the `[left+1, i-1]` column span at the moment you update
  `best`.
