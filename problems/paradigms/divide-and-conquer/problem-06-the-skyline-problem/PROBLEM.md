# The Skyline Problem

**Difficulty:** Hard

**Source:** LeetCode 218 (The Skyline Problem)

## Description

A city's skyline is the outer contour formed by all its buildings when viewed from a
distance. You are given the locations and heights of all the buildings as a list
`buildings` where `buildings[i] = [left_i, right_i, height_i]`:

- `left_i` and `right_i` are the x-coordinates of the left and right edges of the i-th
  building,
- `height_i` is its height,
- all buildings sit on flat ground at height `0`.

Return the **skyline** as a list of **key points** `[x, y]` sorted by x-coordinate. A
key point is the left endpoint of a horizontal segment in the skyline; the last key
point marks where the rightmost building ends and always has height `0`. There must be
**no consecutive horizontal segments of equal height** in the output — merge them into
one.

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
```

Explanation: Rising to `10` at x=2, then a taller building lifts the contour to `15`
at x=3; after it ends at x=7 the contour drops to `12` (the third building), which ends
at x=12 dropping to `0`. The last two buildings form `10` from x=15 and `8` from x=20,
returning to ground `0` at x=24.

### Example 2

```
Input:  buildings = [[0, 2, 3], [2, 5, 3]]
Output: [[0, 3], [5, 0]]
```

Explanation: Two equal-height buildings that touch at x=2 form a single flat segment of
height `3` from x=0 to x=5. The duplicate `[2, 3]` key point is merged away, leaving
just the rise at x=0 and the drop to `0` at x=5.

## Hint

Use **Divide and Conquer**, mirroring merge sort: split the buildings into two halves,
recursively compute each half's skyline, then **merge** the two skylines. The merge
sweeps both contours left to right, tracking the current height on each side and
emitting a key point whenever the running **max** of the two heights changes.
