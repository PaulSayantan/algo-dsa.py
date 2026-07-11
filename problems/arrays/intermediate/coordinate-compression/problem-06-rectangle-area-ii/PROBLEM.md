# Rectangle Area II

**Difficulty:** Hard

**Source:** LeetCode 850 — Rectangle Area II

## Description

You are given a 2D array `rectangles` where `rectangles[i] = [x1, y1, x2, y2]` denotes the
`i`-th axis-aligned rectangle whose bottom-left corner is `(x1, y1)` and top-right corner is
`(x2, y2)`.

Compute the **total area** covered by all `rectangles` on the plane. Any area covered by two
or more rectangles should be counted only **once**.

Return the total area. Because the answer may be large, return it **modulo** `10^9 + 7`.

The classic approach compresses the distinct x-coordinates so the plane splits into a small
number of vertical strips of known width. A sweep line moving up in y then tracks which
strips are currently covered, and multiplies covered width by the vertical distance between
consecutive events.

## Constraints

- `1 <= rectangles.length <= 200`
- `rectangles[i].length == 4`
- `0 <= x1 < x2 <= 10^9`
- `0 <= y1 < y2 <= 10^9`
- The total area may be too large; return it modulo `10^9 + 7`.

## Examples

### Example 1

```
Input:  rectangles = [[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]
Output: 6
```

**Explanation:** The union of the three rectangles covers a region of total area 6. The
overlap between the first two rectangles (the strip `x` in `[1, 2]`, `y` in `[0, 2]`) is
counted only once.

### Example 2

```
Input:  rectangles = [[0, 0, 1000000000, 1000000000]]
Output: 49
```

**Explanation:** The single rectangle has area `10^9 * 10^9 = 10^18`, and
`10^18 mod (10^9 + 7) = 49`.

## Hint

Use **Coordinate Compression** on the x-coordinates to form vertical strips, then run a
sweep line over the horizontal (y) edges, accumulating `covered_width * delta_y`.
