# Maximum Distance Between Two Convex Polygons

**Difficulty:** Hard

*Source: Toussaint, "Solving geometric problems with the rotating calipers" (1983) —
the "maximum distance between two convex polygons" application. A classic
competitive-geometry exercise.*

## Description

You are given two convex polygons `P` and `Q`, each as a list of vertices in
counter-clockwise order. Find the **maximum** Euclidean distance between a point of `P`
and a point of `Q`.

Because both polygons are convex, the farthest pair is always a pair of **vertices**
(one from each polygon), so you only need to consider vertex-vertex distances — never
interior or edge-interior points.

Return the maximum distance as a floating-point value.

## Constraints

- `3 <= |P|, |Q| <= 100_000`
- Vertices are given in counter-clockwise order and each polygon is strictly convex
  (no three consecutive collinear vertices).
- `-10^6 <= x, y <= 10^6` for every vertex.
- Answers within `1e-6` relative or absolute error are accepted.

## Examples

### Example 1

```
Input:  P = [(0, 0), (1, 0), (1, 1), (0, 1)]
        Q = [(3, 0), (4, 0), (4, 1), (3, 1)]
Output: 4.123105625617661
Explanation: Two unit squares. The farthest pair is P's top-left corner (0, 1) and
             Q's bottom-right corner (4, 0): distance = sqrt(4^2 + 1^2) = sqrt(17)
             ≈ 4.1231. (Equivalently (0,0)-(4,1) also gives sqrt(17).)
```

### Example 2

```
Input:  P = [(0, 0), (1, 0), (1, 1), (0, 1)]
        Q = [(5, 5), (6, 5), (6, 6), (5, 6)]
Output: 8.48528137423857
Explanation: The farthest pair is P's corner (0, 0) and Q's corner (6, 6):
             distance = sqrt(6^2 + 6^2) = sqrt(72) = 6*sqrt(2) ≈ 8.4853.
```

## Hint

Place a pair of parallel supporting lines, one on each polygon, on **opposite** sides,
and rotate them together through a full turn. The vertices they touch form the
*anti-podal* vertex pairs across the two polygons — the **Rotating Calipers on Point
Grids** technique — and the farthest pair is among them, found in `O(|P| + |Q|)` after
you have the hulls.
