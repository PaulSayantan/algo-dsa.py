# Pacific Atlantic Water Flow

**Difficulty:** Medium/Hard

**Source:** LeetCode 417 — Pacific Atlantic Water Flow

## Description

There is an `m x n` rectangular island that borders both the **Pacific Ocean**
and the **Atlantic Ocean**. The Pacific Ocean touches the island's **left and
top** edges, and the Atlantic Ocean touches the island's **right and bottom**
edges.

The island is partitioned into a grid of square cells. You are given an
`m x n` integer matrix `heights` where `heights[r][c]` represents the height
above sea level of the cell at `(r, c)`.

Rain water can flow from a cell to a neighboring cell **4-directionally** if the
neighboring cell's height is **less than or equal to** the current cell's height.
Water can flow from any cell adjacent to an ocean directly into that ocean.

Return a list of grid coordinates `[r, c]` such that rain water can flow from
cell `(r, c)` to **both** the Pacific and Atlantic oceans.

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Examples

### Example 1

```
Input:  heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

**Explanation:** Each listed cell can reach both oceans by flowing along
non-increasing height paths. For example, from `(0,4)` (height 5) water flows
right/up into the Pacific and down into the Atlantic. (Any ordering of the same
set of coordinates is accepted.)

### Example 2

```
Input:  heights = [[1]]
Output: [[0,0]]
```

**Explanation:** The single cell touches every border, so it borders both oceans
and trivially flows to both.

## Hint

Instead of testing each cell forward to both oceans, run a **reverse Grid
DFS / BFS** from the ocean-border cells inward (moving to neighbors of
**greater-or-equal** height); the answer is the intersection of the two
border-reachable sets.
