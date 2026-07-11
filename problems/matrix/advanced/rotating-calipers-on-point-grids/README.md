# Rotating Calipers on Point Grids

**Rotating calipers** is a computational-geometry technique for answering *extremal
pair* questions on a set of points in the plane. You first build the **convex hull**
of the points (a grid / cloud of 2-D coordinates), then sweep a pair (or more) of
parallel support lines — the "calipers" — around the hull. As the calipers rotate
through a full turn, the vertices they touch (the *antipodal* / *co-podal* pairs)
enumerate exactly the pairs that can be extremal for the quantity you care about:
farthest pair, minimum width, tightest bounding rectangle, closest/farthest pair of
two convex bodies, and so on.

## Why it works

On a convex polygon, the vertex that is farthest in a given direction is a *monotone*
function of that direction. So instead of testing all `O(n^2)` pairs of vertices, you
walk one pointer forward as you rotate the supporting line. Each pointer advances at
most once around the hull, so after the hull is built the sweep is **linear**.

## When to reach for it

- You need the **diameter** (farthest pair) of a point set.
- You need the **minimum width**, **minimum-area** or **minimum-perimeter enclosing
  rectangle** of a shape (Toussaint's algorithm — the optimal rectangle always shares
  an edge with the hull).
- You need the **minimum or maximum distance between two convex polygons**.
- More generally: any "extremal over all pairs, but the answer lives on the convex
  hull" problem.

## Complexity

| Phase | Time | Space |
|-------|------|-------|
| Convex hull (Andrew's monotone chain) | `O(n log n)` | `O(n)` |
| Caliper sweep | `O(h)` where `h` = hull size ≤ `n` | `O(1)` extra |
| **Total** | **`O(n log n)`** (dominated by the sort) | **`O(n)`** |

If the points arrive already sorted (or the hull is given), the sweep itself is
`O(n)`.

## Problems

| # | Problem | Summary | Difficulty |
|---|---------|---------|------------|
| 1 | [Farthest Pair of Points (Diameter)](problem-01-farthest-pair-of-points/PROBLEM.md) | Largest distance between any two of `n` points | Easy |
| 2 | [Minimum Width of a Convex Polygon](problem-02-minimum-width-of-convex-polygon/PROBLEM.md) | Smallest slab (pair of parallel lines) containing the polygon | Medium |
| 3 | [Minimum-Area Bounding Rectangle](problem-03-minimum-area-bounding-rectangle/PROBLEM.md) | Smallest-area (possibly rotated) rectangle enclosing all points | Medium |
| 4 | [Maximum Distance Between Two Convex Polygons](problem-04-maximum-distance-between-two-convex-polygons/PROBLEM.md) | Farthest pair of vertices, one from each polygon | Hard |
| 5 | [Minimum Distance Between Two Convex Polygons](problem-05-minimum-distance-between-two-convex-polygons/PROBLEM.md) | Closest approach of two disjoint convex shapes | Hard |

Each problem folder contains `PROBLEM.md` (statement), `solution.py` (empty template to
fill in), and `SOLUTION.md` (answer key with brute force + rotating-calipers approach).
