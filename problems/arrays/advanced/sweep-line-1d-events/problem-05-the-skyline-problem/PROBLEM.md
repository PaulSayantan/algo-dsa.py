# The Skyline Problem

**Difficulty:** Hard

**Source:** LeetCode 218 — "The Skyline Problem"

## Description

A city's skyline is the outer contour formed by all the buildings in that city
when viewed from a distance. You are given the buildings as an array
`buildings` where `buildings[i] = [left_i, right_i, height_i]`:

- `left_i` is the x-coordinate of the left edge of the `i`-th building,
- `right_i` is the x-coordinate of the right edge,
- `height_i` is its height.

All buildings are perfect rectangles grounded on a flat surface at height `0`.

Return the **skyline** as a list of "key points" `[x, y]` sorted by `x`. A key
point is the left endpoint of a horizontal segment of the skyline; the last key
point always has height `0` and marks the right end of the rightmost building.
The ground between buildings is part of the skyline's contour (height `0`).

The output must have **no consecutive horizontal segments of equal height** — a
skyline like `[..., [2, 3], [4, 3], ...]` is invalid and must be collapsed to
`[..., [2, 3], ...]`.

## Constraints

- `1 <= buildings.length <= 10^4`
- `0 <= left_i < right_i <= 2^31 - 1`
- `1 <= height_i <= 2^31 - 1`
- `buildings` is sorted by `left_i` in non-decreasing order.

## Examples

### Example 1

```
Input:  buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
Output: [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
Explanation:
  Left to right, the tallest active building changes at each key point:
  height 10 starts at x=2, is overtaken by 15 at x=3, drops to 12 at x=7
  (when the height-15 building ends), drops to ground 0 at x=12, and so on.
```

### Example 2

```
Input:  buildings = [[0, 2, 3], [2, 5, 3]]
Output: [[0, 3], [5, 0]]
Explanation:
  Two abutting buildings of equal height 3 form one flat top from x=0 to x=5.
  The intermediate point at x=2 is suppressed because the height does not
  change there (no consecutive equal-height segments allowed).
```

### Example 3

```
Input:  buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
Output: [[1, 3], [2, 0]]
Explanation:
  Three buildings share the span [1, 2); the skyline follows the tallest,
  height 3, from x=1, then drops to 0 at x=2.
```

## Hint

Sweep a vertical line across the x-axis processing building **start** and **end**
events in x-order — a classic **Sweep Line (1D events)**. Maintain the multiset
of heights of all buildings currently crossing the line (a max-heap works well):
at each event the skyline height is the current maximum active height, and you
emit a key point only when that maximum **changes**. The subtlety is efficiently
removing a height when its building ends.
