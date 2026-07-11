# Pacific Atlantic Water Flow

**Difficulty:** Medium/Hard

**Source:** LeetCode 417 — Pacific Atlantic Water Flow

## Description

There is an `m x n` rectangular island that borders both the **Pacific Ocean**
and the **Atlantic Ocean**. The Pacific Ocean touches the island's **left** and
**top** edges, and the Atlantic Ocean touches the island's **right** and
**bottom** edges.

The island is partitioned into a grid of square cells. You are given an
`m x n` integer matrix `heights` where `heights[r][c]` represents the height
above sea level of the cell at coordinate `(r, c)`.

Rain water can flow from a cell to a neighboring cell directly north, south,
east, or west **if and only if** the neighboring cell's height is **less than or
equal to** the current cell's height. Water can flow from any cell adjacent to an
ocean into that ocean.

Return a list of grid coordinates `[r, c]` such that rain water can flow from
cell `(r, c)` to **both** the Pacific and Atlantic oceans. The coordinates may be
returned in any order.

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Examples

### Example 1

```
Input: heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Explanation:** Each listed cell has a downhill (non-increasing) path to the
Pacific (top/left edges) and another to the Atlantic (bottom/right edges). For
instance `(0,4)` with height `5` is on both the top edge (Pacific) and the right
edge (Atlantic), so it trivially reaches both. Cell `(2,2)` with height `5` can
flow left/up toward the Pacific and down/right toward the Atlantic. Order of the
returned pairs does not matter.

### Example 2

```
Input: heights = [[1]]
Output: [[0,0]]
```

**Explanation:** A single cell touches all four edges, so it borders both oceans
and water reaches both. The only coordinate is `(0,0)`.

## Hint

Use **Flood Fill (basic DFS/BFS)**, but run it **in reverse**: start from the
ocean-border cells and move to neighbors whose height is **greater than or equal
to** the current cell (climbing uphill). Do one multi-source flood from the
Pacific border and one from the Atlantic border, then return the cells reached by
both.
