# Minimum Distance Between Two Convex Polygons

**Difficulty:** Hard

*Source: Toussaint, "An optimal algorithm for computing the minimum vertex distance
between two crossing convex polygons" / the rotating-calipers minimum-distance
application (1983-84). A staple hard geometry problem on competitive judges.*

## Description

You are given two **disjoint** convex polygons `P` and `Q`, each as vertices in
counter-clockwise order. Compute the **minimum** Euclidean distance between the two
shapes — that is, the closest approach between any point of `P` (boundary or interior)
and any point of `Q`.

Unlike the maximum-distance problem, the closest pair is generally realized by a
**vertex of one polygon and a point in the interior of an edge of the other**, or by two
edges — so you must measure **segment-to-segment** distances, not just vertex-to-vertex.

Return the minimum distance as a floating-point number. (You may assume the polygons do
not overlap; if they did, the answer would be 0.)

## Constraints

- `3 <= |P|, |Q| <= 100_000`
- Vertices are given in counter-clockwise order; both polygons are convex.
- The two polygons are disjoint (their interiors do not intersect).
- `-10^6 <= x, y <= 10^6` for every vertex.
- Answers within `1e-6` relative or absolute error are accepted.

## Examples

### Example 1

```
Input:  P = [(0, 0), (1, 0), (1, 1), (0, 1)]
        Q = [(3, 0), (4, 0), (4, 1), (3, 1)]
Output: 2.0
Explanation: Two unit squares separated horizontally. P's right edge is at x = 1 and
             Q's left edge is at x = 3; the closest points face each other across the
             gap, distance 3 - 1 = 2.
```

### Example 2

```
Input:  P = [(0, 0), (1, 0), (1, 1), (0, 1)]
        Q = [(5, 5), (6, 5), (6, 6), (5, 6)]
Output: 5.656854249492381
Explanation: The squares sit diagonally apart. The closest pair is P's corner (1, 1)
             and Q's corner (5, 5): distance = sqrt(4^2 + 4^2) = sqrt(32) = 4*sqrt(2)
             ≈ 5.6569.
```

## Hint

Bring one supporting line up against each polygon from opposite sides — but here the
calipers are **co-parallel** (same direction), forming the two lines of a moving
"bridge". As you rotate them around both hulls, the co-podal vertex/edge pairs they
touch include the closest features; measure the **segment-to-segment** distance at each
step. This is the **Rotating Calipers on Point Grids** technique applied to two
polygons.
