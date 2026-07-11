# Path With Minimum Effort

**Difficulty:** Medium

**Source:** LeetCode 1631 — Path With Minimum Effort

## Description

You are a hiker preparing for an upcoming hike. You are given `heights`, a 2-D
array of size `rows x columns`, where `heights[row][col]` represents the height
of the cell `(row, col)`. You start at the top-left cell `(0, 0)` and want to
travel to the bottom-right cell `(rows - 1, columns - 1)` (0-indexed). You can
move up, down, left, or right, and you wish to find a route that requires the
**minimum effort**.

A route's **effort** is the **maximum absolute difference in heights between two
consecutive cells** along the route. Return the minimum effort required to
travel from the top-left cell to the bottom-right cell.

In other words, you are not summing costs along the path — you are minimising the
single **worst** step (the largest height jump) you are forced to take. This is a
*bottleneck* / *minimax* shortest-path objective.

## Constraints

- `rows == heights.length`
- `columns == heights[i].length`
- `1 <= rows, columns <= 100`
- `1 <= heights[i][j] <= 10^6`

## Examples

### Example 1

```
Input: heights = [[1, 2, 2],
                  [3, 8, 2],
                  [5, 3, 5]]
Output: 2
```

**Explanation:** The route `[1, 3, 5, 3, 5]` (down the left column, then across
the bottom row) has consecutive differences `2, 2, 2, 2`, so its effort is `2`.
This is better than the straight right-then-down route `[1, 2, 2, 2, 5]`, whose
last step `2 -> 5` gives an effort of `3`.

### Example 2

```
Input: heights = [[1, 2, 3],
                  [3, 8, 4],
                  [5, 3, 5]]
Output: 1
```

**Explanation:** The route `[1, 2, 3, 4, 5]` (across the top row, then down the
right column) has every consecutive difference equal to `1`, so its effort is
`1`, and no route can do better than a difference of `1`.

### Example 3

```
Input: heights = [[1, 2, 1, 1, 1],
                  [1, 2, 1, 2, 1],
                  [1, 2, 1, 2, 1],
                  [1, 2, 1, 2, 1],
                  [1, 1, 1, 2, 1]]
Output: 0
```

**Explanation:** There is a snake-shaped route that only ever steps between
cells of height `1` (down column 0, across the bottom, up column 2, across the
top, down column 4). Every step has difference `0`, so the effort is `0`.

## Hint

You are minimising the **maximum edge** on the path, not the sum. Run **Dijkstra
on the grid** but relax with `effort[nb] = min(effort[nb], max(effort[cur],
abs(height difference)))` — replace the usual `+` with `max`. (Binary search on
the answer plus BFS/DFS also works.)
