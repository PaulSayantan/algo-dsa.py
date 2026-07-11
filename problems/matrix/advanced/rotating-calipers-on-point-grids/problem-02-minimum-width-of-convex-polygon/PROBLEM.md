# Minimum Width of a Convex Polygon

**Difficulty:** Medium

*Source: Classic computational-geometry problem ("width of a convex polygon" /
"minimum slab"). Toussaint, 1983. Appears in competitive judges as "narrowest
corridor" / "thinnest strip" variants.*

## Description

You are given `n` points on the plane. Consider the smallest **slab** — the region
between two parallel lines — that fully contains all the points. The distance between
those two parallel lines, minimized over all possible orientations, is called the
**width** of the point set (equivalently, the width of its convex hull).

Return this minimum width as a floating-point number. Intuitively, it is the smallest
gap through which the shape could pass if translated straight through a slot.

A well-known fact makes this tractable: **for at least one optimal orientation, one of
the two supporting lines is collinear with an edge of the convex hull.** So it suffices
to consider each hull edge as one caliper line and find the hull vertex farthest from
it.

## Constraints

- `3 <= n <= 100_000`
- `-10^6 <= x_i, y_i <= 10^6`
- The points are not all collinear (so the hull has positive area and a finite width).
- Answers within `1e-6` relative or absolute error are accepted.

## Examples

### Example 1

```
Input:  points = [(0, 0), (4, 0), (4, 2), (0, 2)]
Output: 2.0
Explanation: A 4-by-2 axis-aligned rectangle. The narrowest slab is bounded by the two
             long horizontal edges (y = 0 and y = 2), giving width 2. Any tilted slab
             is wider.
```

### Example 2

```
Input:  points = [(0, 0), (4, 0), (0, 3)]
Output: 2.4
Explanation: A right triangle with legs 4 and 3 and hypotenuse 5. The width equals the
             shortest altitude, which is the altitude to the hypotenuse:
             (2 * area) / hypotenuse = (2 * 6) / 5 = 12/5 = 2.4.
```

## Hint

The optimal slab always has one line flush with a hull edge. Build the convex hull,
then rotate a pair of parallel calipers around it, tracking for each edge the antipodal
vertex of maximum perpendicular distance — the **Rotating Calipers on Point Grids**
technique — and take the minimum of those distances.
