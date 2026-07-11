# Solution — Minimum Width of a Convex Polygon

## Brute Force

The width for a *fixed* orientation equals the spread of the points when projected onto
the direction perpendicular to the slab. A naive method tries many discrete angles,
projects all points, and takes the min-max spread — but discretizing angles is both
slow and inexact.

A cleaner brute force uses the structural fact directly: for every **pair** of hull
edges (or every edge paired with every vertex), compute a candidate width. For each
hull edge, scan all `h` vertices to find the maximum perpendicular distance:

```python
def minimum_width(points):
    h = convex_hull(points)          # CCW
    n = len(h)
    best = float('inf')
    for i in range(n):
        a, b = h[i], h[(i + 1) % n]
        L = dist(a, b)
        far = max(abs(cross(a, b, h[k])) / L for k in range(n))
        best = min(best, far)
    return best
```

- **Time:** `O(h^2)` for the nested edge/vertex scan (plus `O(n log n)` for the hull).
- **Space:** `O(n)`.

Correct, but the inner scan re-examines all vertices for every edge.

## Optimal Approach — Rotating Calipers on Point Grids

### Key fact (Toussaint)

The minimum-width slab always has **one of its two lines flush with a convex-hull
edge**, and the opposite line passes through the single hull vertex that is farthest
(perpendicularly) from that edge. So we only need, per edge, its unique *antipodal*
vertex — and that vertex advances **monotonically** as the edge rotates around the
hull. This turns the `O(h^2)` scan into a single linear pass.

### Steps

1. Build the convex hull in CCW order (`O(n log n)`). If `h < 3` the width is 0
   (degenerate / collinear), which the constraints exclude but which you should still
   guard against.

2. Initialize a pointer `j` to the vertex farthest from the first edge. Walk `i` over
   every edge `H[i] -> H[i+1]`. Before recording a candidate, advance `j` while the
   next vertex is strictly farther from the current edge:

   ```
   while |area(H[i], H[i+1], H[j+1])| > |area(H[i], H[i+1], H[j])|:
       j = j + 1   (mod h)
   ```

   Here `area(a,b,c)` is the signed cross product; dividing by `|edge|` gives the true
   perpendicular distance, but for the *advance* test the un-normalized cross product
   suffices because the edge is fixed inside the loop.

3. For each edge, the candidate width is
   `|area(H[i], H[i+1], H[j])| / length(H[i] -> H[i+1])`. Keep the minimum.

Because `j` only moves forward and wraps once, the sweep is `O(h)`.

### Reference implementation

```python
import math

def minimum_width(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    def convex_hull(pts):
        pts = sorted(set(pts))
        if len(pts) <= 2:
            return pts
        lo = []
        for p in pts:
            while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
                lo.pop()
            lo.append(p)
        up = []
        for p in reversed(pts):
            while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
                up.pop()
            up.append(p)
        return lo[:-1] + up[:-1]

    h = convex_hull(points)
    n = len(h)
    if n < 3:
        return 0.0

    best = float('inf')
    j = 1
    for i in range(n):
        ni = (i + 1) % n
        while (abs(cross(h[i], h[ni], h[(j + 1) % n]))
               > abs(cross(h[i], h[ni], h[j]))):
            j = (j + 1) % n
        edge_len = math.hypot(h[ni][0]-h[i][0], h[ni][1]-h[i][1])
        best = min(best, abs(cross(h[i], h[ni], h[j])) / edge_len)
    return best
```

- **Time:** `O(n log n)` (hull sort dominates); sweep `O(h)`.
- **Space:** `O(n)`.

### Why it is correct

Width as a function of orientation is piecewise-sinusoidal and its minima occur at
orientations where a support line coincides with a hull edge (otherwise you could rotate
slightly to shrink the slab). Enumerating all edge-flush orientations therefore captures
the global minimum, and the antipodal vertex per edge is exactly the far support point.

## Key Insights & Edge Cases

- **Antipodal vertex is unique per edge** on a strictly convex hull; on hulls with
  parallel edges use strict `>` in the advance test to avoid infinite loops.
- **Normalize by edge length** to get an actual distance — the raw cross product is
  *twice the triangle area*, not a distance.
- **Collinear input** yields `h < 3`; width is 0 and there is no meaningful slab.
- **Numerical care:** keep integer cross products where possible and only divide (float)
  when producing the final distance; compare candidates with a tolerance if needed.
- Width is the classic dual of the **diameter** (Problem 1): diameter maximizes over
  antipodal *point* pairs, width minimizes over antipodal *edge–vertex* pairs.
