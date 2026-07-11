# Minimum-Area Bounding Rectangle

**Difficulty:** Medium

*Source: Toussaint's "Solving geometric problems with the rotating calipers" (1983).
Also known as the minimum-area enclosing rectangle / "smallest bounding box"; appears
in OpenCV as `cv2.minAreaRect` and in many contest problem sets.*

## Description

You are given `n` points on the plane. Find the rectangle of **smallest area** that
contains all of them. Unlike an axis-aligned bounding box, this rectangle may be
**rotated to any orientation**.

Return the minimum area as a floating-point number.

The crucial theorem: the minimum-area enclosing rectangle of a convex polygon always
has **one side collinear with an edge of the polygon**. This reduces an
infinite-orientation search to checking only the `h` edges of the convex hull.

## Constraints

- `1 <= n <= 100_000`
- `-10^6 <= x_i, y_i <= 10^6`
- If all points are collinear (or there are fewer than 3 distinct points), the minimum
  enclosing rectangle degenerates to a segment of area `0`.
- Answers within `1e-6` relative or absolute error are accepted.

## Examples

### Example 1

```
Input:  points = [(1, 0), (0, 1), (-1, 0), (0, -1)]
Output: 2.0
Explanation: A diamond (a unit square rotated 45 degrees). Aligning a rectangle side
             with any hull edge, e.g. the edge (1,0)-(0,1) of direction (-1,1), yields
             a square of side sqrt(2), so the area is (sqrt(2))^2 = 2. The axis-aligned
             bounding box is 2-by-2 = 4, which is larger, so the tilted rectangle wins.
```

### Example 2

```
Input:  points = [(0, 0), (4, 0), (4, 2), (0, 2)]
Output: 8.0
Explanation: The points already form a 4-by-2 rectangle; the minimum enclosing
             rectangle is the rectangle itself, area 4 * 2 = 8.
```

## Hint

Sweep four mutually perpendicular calipers (two pairs of parallel lines) around the
convex hull. Fix one caliper flush with each hull edge in turn and slide the other
three to touch their extreme vertices — the **Rotating Calipers on Point Grids**
technique — computing the width times height for that orientation.
