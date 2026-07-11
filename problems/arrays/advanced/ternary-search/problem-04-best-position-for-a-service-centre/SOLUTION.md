# Solution — Best Position for a Service Centre

## Brute Force

Grid the bounding box `[0, 100] x [0, 100]` finely and evaluate `cost(x, y)` at every
cell, keeping the minimum. Optionally refine the grid around the best cell.

- **Time:** O(G² · n) for a `G x G` grid. Reaching `1e-5` needs a very fine grid, so
  this is slow and only approximate.
- **Space:** O(1).

The cost surface is smooth and bowl-shaped (convex), so a blind grid wastes almost all
of its evaluations far from the optimum.

## Optimal Approach (Nested Ternary Search)

### Why it is unimodal

Each term `sqrt((x - x_i)^2 + (y - y_i)^2)` is the Euclidean distance from `(x, y)` to a
fixed point — a **convex** function of `(x, y)`. A sum of convex functions is convex, so
`cost(x, y)` is convex over the plane. Convexity gives two things we need:

1. Fix any `x`. Then `g_x(y) = cost(x, y)` is a convex function of one variable, hence
   **unimodal** in `y`. Its minimum `h(x) = min_y g_x(y)` is well-defined.
2. The **partial-minimization** `h(x) = min_y cost(x, y)` of a jointly convex function
   is itself **convex** (hence unimodal) in `x`.

So we can minimize over `y` first (inner search) and then over `x` (outer search), and
both searches are over unimodal functions — exactly what ternary search requires.

### The two nested searches

```
outer: ternary-search x in [minX, maxX] to minimize  h(x)
         where h(x) = inner(x)
inner(x): ternary-search y in [minY, maxY] to minimize g_x(y) = cost(x, y),
          return that minimum value
```

Each search runs a fixed number of iterations (e.g. 100) of the standard "compare the
two one-third probes, discard a third" loop for a **minimum**. The bounding box of the
input is a valid, tight search rectangle because the geometric median always lies inside
the convex hull of the points.

### Why it is correct

For a fixed `x`, the inner ternary search returns `h(x) = min_y cost(x, y)` (correct
because `g_x` is unimodal). The outer search then minimizes `h(x)` over `x` (correct
because `h` is unimodal). Since

```
min_{x, y} cost(x, y) = min_x ( min_y cost(x, y) ) = min_x h(x),
```

the nested procedure computes the true global minimum.

### Reference implementation

```python
import math
from typing import List


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        def cost(x: float, y: float) -> float:
            return sum(math.hypot(x - px, y - py) for px, py in positions)

        def best_y(x: float) -> float:            # inner ternary over y
            lo, hi = 0.0, 100.0
            for _ in range(100):
                m1 = lo + (hi - lo) / 3.0
                m2 = hi - (hi - lo) / 3.0
                if cost(x, m1) < cost(x, m2):
                    hi = m2
                else:
                    lo = m1
            return cost(x, (lo + hi) / 2.0)

        lo, hi = 0.0, 100.0                        # outer ternary over x
        for _ in range(100):
            m1 = lo + (hi - lo) / 3.0
            m2 = hi - (hi - lo) / 3.0
            if best_y(m1) < best_y(m2):
                hi = m2
            else:
                lo = m1
        return best_y((lo + hi) / 2.0)
```

- **Time:** O(I² · n) where `I` is the per-axis iteration count — `O(n · log²(range/eps))`.
  With `n <= 50` and `I = 100` this is ~`50 · 100 · 100 · 4 = 2·10^7` distance
  evaluations, comfortably fast.
- **Space:** O(1).

## Key Insights & Edge Cases

- **Joint convexity ⇒ per-axis unimodality ⇒ nesting is valid.** This is the crux: you
  may only nest ternary searches when the partial minimum stays unimodal, which
  convexity guarantees. For a non-convex surface, nesting can lock onto a wrong local
  optimum.
- **Cost of nesting:** the inner search runs on *every* outer probe, so evaluations
  multiply — `O(log²)` factor. Keep `n` and the iteration count modest, or reuse probes.
- **Search box = bounding box.** The geometric median lies within the convex hull, so
  `[minX, maxX] x [minY, maxY]` (or the fixed `[0,100]²` here) always contains the
  optimum.
- **`n == 1`:** the optimum sits on the single point with cost `0` — the searches
  converge there.
- **`n == 2`:** the whole connecting segment is optimal (cost = distance between the two
  points); ternary search happily lands anywhere on it with the correct value.
- **Alternative:** Weiszfeld's iterative algorithm or gradient descent / simulated
  annealing also solve this. Nested ternary is attractive because it needs no
  derivatives and no step-size tuning — only the unimodality guarantee.
