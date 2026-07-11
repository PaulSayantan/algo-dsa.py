# Solution — Rectangle Area II

## Brute Force

The literal grid approach — allocate a boolean cell for every integer coordinate
and mark covered cells — is impossible here: coordinates reach `10^9`, so a grid
would need `10^18` cells. Even iterating rectangle interiors is out. Some naive
alternatives:

- **Pairwise inclusion–exclusion** over all subsets of rectangles is
  exponential (`O(2^R)`) and infeasible.
- **Sum of areas minus pairwise overlaps** is wrong for three-or-more-way
  overlaps unless you carry the full inclusion–exclusion series.

We need a structural approach. Coordinate compression + 2D difference array
turns this into a small, exact grid problem.

## Optimal Approach (Coordinate Compression + 2D Difference Array)

### Idea

Only the **distinct x-coordinates and y-coordinates** of rectangle edges matter.
Between two consecutive distinct x-values (and two consecutive y-values), the
covered/uncovered status is constant. So compress coordinates into a grid of at
most `2R x 2R` **cells**, where each cell represents a real sub-rectangle of the
plane with a known width and height.

### Steps

1. Collect and sort the unique x-coordinates `xs` and y-coordinates `ys` across
   all rectangles. There are at most `2R` of each.
2. Create a difference grid `diff` of size `(len(xs)+1) x (len(ys)+1)` over the
   **cell indices** (a cell `(i, j)` spans `[xs[i], xs[i+1]) x [ys[j], ys[j+1])`).
3. For each rectangle, map its real corners to cell indices via binary search:
   `xi1 = index_of(x1)`, `xi2 = index_of(x2)`, similarly for y. Mark the cell
   range `[xi1, xi2-1] x [yi1, yi2-1]` with `+1` using the four-corner
   difference-array update (`O(1)` per rectangle):

   ```
   diff[xi1][yi1]   += 1
   diff[xi2][yi1]   -= 1
   diff[xi1][yi2]   -= 1
   diff[xi2][yi2]   += 1
   ```

   (Here `xi2`/`yi2` are already the "one past the last covered cell" indices,
   because a rectangle ending at coordinate `xs[xi2]` covers cells up to index
   `xi2 - 1`.)
4. Run the 2D prefix sum over `diff`. Cell `(i, j)` is **covered** iff its value
   is `> 0`.
5. For each covered cell add its real area
   `(xs[i+1] - xs[i]) * (ys[j+1] - ys[j])` to the total.
6. Return the total modulo `10^9 + 7`.

### Why it is correct

Coordinate compression preserves geometry: within one compressed cell the entire
sub-rectangle is uniformly inside-or-outside every rectangle, so a single
coverage count per cell is exact. The difference array marks exactly the cells
each rectangle spans; the prefix sum turns those marks into per-cell coverage
counts. Summing the true dimensions of covered cells yields the union area with
each region counted once — a positive count means "covered," and we add the area
regardless of how many rectangles overlap there.

### Reference implementation

```python
from bisect import bisect_left

class Solution:
    def rectangleArea(self, rectangles):
        MOD = 10 ** 9 + 7
        xs = sorted({x for r in rectangles for x in (r[0], r[2])})
        ys = sorted({y for r in rectangles for y in (r[1], r[3])})
        xi = {v: i for i, v in enumerate(xs)}
        yi = {v: i for i, v in enumerate(ys)}

        nx, ny = len(xs), len(ys)
        diff = [[0] * (ny + 1) for _ in range(nx + 1)]

        for x1, y1, x2, y2 in rectangles:
            a, b = xi[x1], xi[x2]     # cell columns [a, b)
            c, d = yi[y1], yi[y2]     # cell rows    [c, d)
            diff[a][c] += 1
            diff[b][c] -= 1
            diff[a][d] -= 1
            diff[b][d] += 1

        total = 0
        for i in range(nx):
            for j in range(ny):
                top    = diff[i - 1][j] if i else 0
                left   = diff[i][j - 1] if j else 0
                corner = diff[i - 1][j - 1] if (i and j) else 0
                diff[i][j] += top + left - corner
                if diff[i][j] > 0 and i + 1 < nx and j + 1 < ny:
                    w = xs[i + 1] - xs[i]
                    h = ys[j + 1] - ys[j]
                    total += w * h
        return total % MOD
```

- **Time:** `O(R log R + R^2)` — sorting/compression plus filling and sweeping a
  grid of `O(R^2)` cells. With `R <= 200`, this is tiny (`~4 * 10^4` cells).
- **Space:** `O(R^2)` for the compressed difference grid.

## Key Insights & Edge Cases

- **Compress, don't allocate:** the coordinate range is `10^9`, so you must map
  edges to indices. The number of meaningful cells is `O(R^2)`, not
  `O(coord^2)`.
- **Coverage is boolean for area:** cells covered by 1 or 100 rectangles both
  contribute their area exactly once — test `> 0`, never add the count.
- **Apply the modulo only at the end** (or on the accumulator) — but multiply
  widths/heights as true integers first, since the problem guarantees the raw
  total fits in 64 bits.
- The rightmost `xs` value and topmost `ys` value have no cell to their right/
  top; the `i + 1 < nx` / `j + 1 < ny` guard (or padding) prevents indexing past
  the last real cell.
- This is the difference-array counterpart to the classic **sweep-line +
  segment tree** solution; the diff-array version is simpler to code and fast
  enough because `R` is small.
- A single rectangle returns its own area; identical duplicated rectangles
  return that area once.
