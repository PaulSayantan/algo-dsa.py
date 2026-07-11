# Minimum Cost to Make at Least One Valid Path in a Grid

**Difficulty:** Hard

**Source:** LeetCode 1368 — Minimum Cost to Make at Least One Valid Path in a Grid

## Description

Given an `m x n` grid, each cell has a sign pointing to the next cell you should
visit if you are currently on this cell. The sign of `grid[i][j]` can be:

- `1` — go **right**, to `(i, j + 1)`
- `2` — go **left**, to `(i, j - 1)`
- `3` — go **down**, to `(i + 1, j)`
- `4` — go **up**, to `(i - 1, j)`

Notice that there could be some signs on the cells of the grid that point
outside the grid. You will initially start at the upper-left cell `(0, 0)`. A
**valid path** in the grid is a path that starts from `(0, 0)`, ends at
`(m - 1, n - 1)`, and follows the signs on each visited cell.

The valid path does not have to be the shortest path. You can modify the sign of
a cell with `cost = 1`. You may modify the sign of a cell **once at most**.
Return the **minimum cost** to make the grid have at least one valid path.

Intuition: moving in the direction the current cell's sign already points is
**free**; moving in any other direction costs `1` (you change that cell's sign).
You want the cheapest way to carve out a route from the top-left to the
bottom-right corner.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `1 <= grid[i][j] <= 4`

## Examples

### Example 1

```
Input: grid = [[1, 1, 1, 1],
               [2, 2, 2, 2],
               [1, 1, 1, 1],
               [2, 2, 2, 2]]
Output: 3
```

**Explanation:** Row 0 points right, row 1 left, row 2 right, row 3 left. Follow
the signs right across row 0 to `(0,3)` (free), then you must change a sign to go
**down** into row 1 (cost 1); follow left to `(1,0)`, change to go down (cost 1);
follow right to `(2,3)`, change to go down (cost 1) and you land on the target
`(3,3)`. Three sign changes, so the cost is `3`.

### Example 2

```
Input: grid = [[1, 1, 3],
               [3, 2, 2],
               [1, 1, 4]]
Output: 0
```

**Explanation:** Starting at `(0,0)` and always obeying the signs traces
`(0,0) -> (0,1) -> (0,2) -> (1,2) -> (1,1) -> (1,0) -> (2,0) -> (2,1) -> (2,2)`,
which ends exactly on the bottom-right corner. No sign needs changing, so the
cost is `0`.

### Example 3

```
Input: grid = [[1, 2],
               [4, 3]]
Output: 1
```

**Explanation:** `(0,0)` points right to `(0,1)` for free. From `(0,1)` the sign
points left (back to the start), so to reach the target `(1,1)` you change the
sign at `(0,1)` to **down** (cost 1). One change, so the cost is `1`.

## Hint

Following a cell's existing sign costs `0`; going against it costs `1` — every
move has weight `0` or `1`. That is precisely the case for **0-1 BFS**: use a
deque, appending free moves to the **front** and paid moves to the **back**, so
the deque stays ordered by cost and each cell is finalized in O(1) amortised
time.
