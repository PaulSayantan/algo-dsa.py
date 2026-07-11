# Minimum Cost Path

**Difficulty:** Medium

**Source:** GeeksforGeeks — Minimum Cost Path (4-directional variant); a weighted
generalization of LeetCode 64 "Minimum Path Sum".

## Description

You are given a 2-D grid `grid` of size `m x n` where every cell holds a
**non-negative cost**. Starting from the top-left cell `(0, 0)`, you want to
reach the bottom-right cell `(m - 1, n - 1)`.

From a cell you may move to any of its **4 orthogonal neighbours** (up, down,
left, right) as long as you stay inside the grid. The **cost of a path** is the
sum of the values of every cell you visit, **including** the start cell and the
destination cell. Return the minimum possible path cost.

Because you may move in all four directions (not just right and down), a cheaper
route may need to detour sideways or upward around expensive regions, so a
simple row-by-row dynamic program is not sufficient.

## Constraints

- `1 <= m, n <= 500`
- `0 <= grid[i][j] <= 10^4`
- The start and destination cells are always traversable (there are no walls;
  every cell just has a cost).

## Examples

### Example 1

```
Input: grid = [[1, 3, 1],
               [1, 5, 1],
               [4, 2, 1]]
Output: 7
```

**Explanation:** The cheapest route is `(0,0) -> (0,1) -> (0,2) -> (1,2) ->
(2,2)`, i.e. cells `1 + 3 + 1 + 1 + 1 = 7`. Every alternative (for example going
down the left column, `1 + 1 + 4 + 2 + 1 = 9`) costs more.

### Example 2

```
Input: grid = [[1, 1, 1],
               [9, 9, 1],
               [1, 1, 1],
               [1, 9, 9],
               [1, 1, 1]]
Output: 11
```

**Explanation:** Rows 1 and 3 are almost entirely blocked by cost-9 cells. The
only cheap gap in row 1 is column 2, and the only cheap gap in row 3 is column
0, so the path must pass through `(1,2)` and `(3,0)`. Between them it crosses
row 2 sideways (a **left** move): `(0,0) (0,1) (0,2) (1,2) (2,2) (2,1) (2,0)
(3,0) (4,0) (4,1) (4,2)` — 11 cells of value 1, total `11`. A straight
right/down route would have to pay a `9`.

### Example 3

```
Input: grid = [[5]]
Output: 5
```

**Explanation:** The start is also the destination, and its own cost still
counts, so the answer is `5`.

## Hint

Cells have different, non-negative costs, so this is a weighted shortest-path
problem — use **Dijkstra on the grid** with a min-heap keyed by accumulated
cost. Add a cell's value when you relax into it, and settle a cell the first
time it is popped.
