# 01 Matrix

**Difficulty:** Medium

**Source:** LeetCode 542 — 01 Matrix

## Description

Given an `m x n` binary matrix `mat`, return the distance of the **nearest `0`**
for each cell.

The distance between two adjacent cells is `1`, where adjacency is
**4-directional** (up, down, left, right).

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
- There is at least one `0` in `mat`.

## Examples

### Example 1

```
Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]
Output:      [[0,0,0],
              [0,1,0],
              [0,0,0]]
```

**Explanation:** Every `1` cell (only the center here) is exactly 1 step away
from a `0`, and every `0` has distance `0`.

### Example 2

```
Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]
Output:      [[0,0,0],
              [0,1,0],
              [1,2,1]]
```

**Explanation:** The center `1` at `(1,1)` is 1 step from the `0` directly above
it. The cell `(2,1)` is 2 steps from the nearest `0` (down from `(1,1)` then to a
`0`, or via a neighbouring column), while `(2,0)` and `(2,2)` are 1 step from the
`0`s above them.

## Hint

Instead of running a separate BFS from every `1` (slow), seed a single BFS queue
with **all `0` cells at once** and let the wave spread outward. This
**multi-source Lee Algorithm** fills every cell with its true nearest-zero
distance in one O(m×n) pass.
