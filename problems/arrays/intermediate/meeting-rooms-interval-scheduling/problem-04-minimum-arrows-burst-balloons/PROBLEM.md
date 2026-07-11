# Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium

**Source:** LeetCode 452 — Minimum Number of Arrows to Burst Balloons

## Description

There are some spherical balloons taped to a flat wall. The balloons are given as an
array `points` where `points[i] = [x_start, x_end]` denotes a balloon whose horizontal
diameter stretches between `x_start` and `x_end` (inclusive).

Arrows are shot upward along the vertical direction from different points on the
x-axis. An arrow shot at coordinate `x` bursts a balloon `[x_start, x_end]` if
`x_start <= x <= x_end`. There is no limit to how far an arrow travels, so a single
arrow can burst every balloon whose interval contains `x`.

Return the **minimum number of arrows** that must be shot to burst all balloons.

## Constraints

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= x_start < x_end <= 2^31 - 1`

## Examples

### Example 1

```
Input:  points = [[10, 16], [2, 8], [1, 6], [7, 12]]
Output: 2
Explanation: One arrow at x = 6 bursts [1, 6] and [2, 8]; a second arrow at x = 12
             bursts [7, 12] and [10, 16]. Two arrows cover all four balloons.
```

### Example 2

```
Input:  points = [[1, 2], [3, 4], [5, 6], [7, 8]]
Output: 4
Explanation: No two balloons overlap, so each needs its own arrow.
```

### Example 3

```
Input:  points = [[1, 2], [2, 3], [3, 4], [4, 5]]
Output: 2
Explanation: An arrow at x = 2 bursts [1, 2] and [2, 3] (they touch at 2). An arrow at
             x = 4 bursts [3, 4] and [4, 5]. Two arrows suffice.
```

## Hint

Use **Meeting Rooms / Interval Scheduling**: sort by end coordinate and fire one arrow
at the end of the earliest-finishing balloon; that arrow clears every balloon it
reaches. Start a new arrow only when a balloon begins past the current arrow's
position.
