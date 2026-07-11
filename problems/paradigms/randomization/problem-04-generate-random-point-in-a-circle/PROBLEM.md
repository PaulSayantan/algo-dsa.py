# Generate Random Point in a Circle

**Difficulty:** Medium

**Source:** LeetCode 478 — Generate Random Point in a Circle

## Description

Given the radius and the position of the center of a circle, implement the function
`randPoint` which generates a **uniformly random** point inside the circle (the boundary is
included).

Implement the `Solution` class:

- `Solution(radius, x_center, y_center)` — Initializes the object with the radius of the
  circle `radius` and the center `(x_center, y_center)`.
- `randPoint()` — Returns a random point `[x, y]` inside the circle. Every point inside (or
  on the boundary of) the circle must be equally likely — i.e. the points are distributed
  **uniformly over the disk's area**.

## Constraints

- `0 < radius <= 10^8`
- `-10^7 <= x_center, y_center <= 10^7`
- At most `3 * 10^4` calls will be made to `randPoint`.

## Examples

### Example 1

```
Input:
["Solution", "randPoint", "randPoint", "randPoint"]
[[1.0, 0.0, 0.0], [], [], []]

Output:
[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
```

**Explanation:**
- `Solution(1.0, 0.0, 0.0)` builds a circle of radius 1 centered at the origin.
- Each `randPoint()` returns a point `[x, y]` with `x^2 + y^2 <= 1`. The three points shown
  all lie inside the unit disk. Any point satisfying the constraint is a valid return; the
  requirement is that the points be spread uniformly over the disk's area.

### Example 2

```
Input:
["Solution", "randPoint", "randPoint"]
[[2.0, 5.0, -3.0], [], []]

Output:
[null, [6.31041, -2.16276], [4.20515, -1.35129]]
```

**Explanation:**
- `Solution(2.0, 5.0, -3.0)` builds a circle of radius 2 centered at `(5, -3)`.
- Each returned point `[x, y]` satisfies `(x - 5)^2 + (y + 3)^2 <= 4`. Both shown points lie
  within that disk. Points must be uniform over the disk's area.

## Hint

Use **Randomization**. A subtle trap: sampling the angle and radius each uniformly bunches
points near the center. Either use *rejection sampling* (sample a uniform point in the
bounding square and reject those outside the circle) or the *inverse-transform* fix
(`r = R * sqrt(U)`) to get true area-uniform points.
