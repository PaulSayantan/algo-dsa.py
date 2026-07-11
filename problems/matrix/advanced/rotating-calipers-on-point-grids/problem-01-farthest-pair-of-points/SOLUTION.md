# Solution — Farthest Pair of Points (Diameter)

## Brute Force

Try every pair and keep the maximum squared distance.

```python
def farthest_pair_sq(points):
    best = 0
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dx = points[i][0] - points[j][0]
            dy = points[i][1] - points[j][1]
            best = max(best, dx * dx + dy * dy)
    return best
```

- **Time:** `O(n^2)` — every pair examined.
- **Space:** `O(1)` extra.

This is fine for `n` up to a few thousand but blows up at `n = 100_000`
(`~10^10` pairs).

## Optimal Approach — Rotating Calipers on Point Grids

### Key fact

The two points that achieve the diameter are always **vertices of the convex hull**,
and they form an **antipodal pair**: there exist two *parallel* supporting lines, one
touching each point, with the whole set between them. There are only `O(h)` antipodal
pairs on a hull of `h` vertices, so if we can enumerate them we skip the quadratic
blow-up.

### Steps

1. **Build the convex hull** with Andrew's monotone chain (`O(n log n)`), producing the
   hull vertices in counter-clockwise (CCW) order, call it `H` with `h` vertices.
   - Handle degenerate cases: if all points are collinear (`h < 3`), the diameter is
     just the distance between the two extreme hull endpoints — the brute-force scan
     over the (few) hull points still works, or you can special-case it.

2. **Sweep the calipers.** Use two pointers `i` (an edge of the hull) and `j` (the
   current farthest vertex from that edge). As `i` walks each edge `H[i] -> H[i+1]`,
   advance `j` forward while doing so increases the perpendicular distance from vertex
   `H[j]` to the edge — measured with the 2-D cross product:

   ```
   area(a, b, c) = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
   ```

   `|area(H[i], H[i+1], H[j])|` is proportional to the distance of `H[j]` from the
   edge. For each edge, the antipodal vertex (and its neighbors) are candidates for the
   diameter; measure `dist^2(H[i], H[j])` and `dist^2(H[i+1], H[j])` and keep the max.

3. Because `j` only ever moves forward and wraps around once, the total work in the
   sweep is `O(h)`.

### Reference implementation

```python
def farthest_pair_sq(points):
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    def convex_hull(pts):
        pts = sorted(set(pts))
        if len(pts) <= 2:
            return pts
        lower = []
        for p in pts:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        upper = []
        for p in reversed(pts):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return lower[:-1] + upper[:-1]          # CCW, no repeated endpoints

    def dist2(a, b):
        return (a[0]-b[0])**2 + (a[1]-b[1])**2

    h = convex_hull(points)
    m = len(h)
    if m == 1:
        return 0
    if m == 2:
        return dist2(h[0], h[1])

    best = 0
    j = 1
    for i in range(m):
        ni = (i + 1) % m
        # advance j while the next vertex is farther from edge (h[i], h[ni])
        while (abs(cross(h[i], h[ni], h[(j + 1) % m]))
               > abs(cross(h[i], h[ni], h[j]))):
            j = (j + 1) % m
        best = max(best, dist2(h[i], h[j]), dist2(h[ni], h[j]))
    return best
```

- **Time:** `O(n log n)` for the hull sort; the sweep is `O(h) = O(n)`.
- **Space:** `O(n)` for the hull.

### Why it is correct

For a fixed hull edge, the vertex maximizing perpendicular distance is unique and
moves monotonically as the edge rotates (convexity). The diameter endpoints must be an
antipodal pair, and every antipodal pair is visited exactly once during the full turn,
so the maximum over the visited candidates equals the true diameter.

## Key Insights & Edge Cases

- **Return squared distance** to stay in exact integer arithmetic; take the square root
  only if the caller wants the actual distance.
- **Duplicate / collinear points:** deduplicate before hull construction; the `<= 0`
  in the cross-product test drops collinear hull points so interior collinear points
  never become vertices.
- **Fewer than 3 hull points:** `m == 1` (all identical, though the problem forbids it)
  returns 0; `m == 2` returns the single pairwise distance.
- **Off-by-one in the sweep:** compare `H[j+1]` against `H[j]` using strict `>`; using
  `>=` can cause `j` to loop endlessly on parallel edges.
- The same skeleton — hull + monotone caliper pointer — is reused in the other problems
  in this folder (width, bounding rectangle, polygon-to-polygon distance).
