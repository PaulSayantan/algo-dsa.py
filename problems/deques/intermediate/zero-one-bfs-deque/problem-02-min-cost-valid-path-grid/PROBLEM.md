# Minimum Cost to Make at Least One Valid Path in a Grid

**Difficulty:** Hard

**Source:** LeetCode 1368 — Minimum Cost to Make at Least One Valid Path in a Grid

## Description

Each cell of an `m x n` `grid` holds an arrow: `1` = right, `2` = left, `3` = down, `4` = up. Starting at the top-left cell `(0,0)`, you follow the arrows for free; changing a cell's arrow to any of the four directions costs `1` and may be done at most once per cell. Return the minimum total cost to reach the bottom-right cell `(m-1, n-1)`. Model each cell as a node: moving in the arrow's direction is a weight-0 edge, any other move is weight-1, then run 0-1 BFS.

## Examples

### Example 1

```
Input:  grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
```

### Example 2

```
Input:  grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
```

## Hint

From each cell, the arrow direction is a 0-cost edge; the other three directions cost 1. Run 0-1 BFS.
