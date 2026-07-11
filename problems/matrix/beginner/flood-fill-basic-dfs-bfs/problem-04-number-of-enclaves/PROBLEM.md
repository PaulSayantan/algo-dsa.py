# Number of Enclaves

**Difficulty:** Medium

**Source:** LeetCode 1020 — Number of Enclaves

## Description

You are given an `m x n` binary matrix `grid`, where `0` represents a sea cell
and `1` represents a land cell.

A **move** consists of walking from one land cell to another adjacent
(**4-directionally**) land cell or walking off the boundary of the `grid`.

Return the number of land cells in `grid` for which we **cannot** walk off the
boundary of the grid in any number of moves.

In other words, count the land cells that are **not** connected (through other
land cells, 4-directionally) to any border of the grid.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 500`
- `grid[i][j]` is either `0` or `1`.

## Examples

### Example 1

```
Input: grid = [
  [0,0,0,0],
  [1,0,1,0],
  [0,1,1,0],
  [0,0,0,0]
]
Output: 3
```

**Explanation:** The land cell at `(1,0)` sits on the left border, so it can walk
off the grid and does not count. The remaining land cells `(1,2)`, `(2,1)`, and
`(2,2)` are connected to each other but not to any border, so they are trapped.
That is `3` enclave cells.

### Example 2

```
Input: grid = [
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,0],
  [0,0,0,0]
]
Output: 0
```

**Explanation:** Every land cell is part of a component that touches the top
border (the group at `(0,1)`–`(0,2)` reaches the top edge, and the column of `1`s
below is connected to it). Since all land can walk off the boundary, there are
`0` enclaves.

## Hint

Use **Flood Fill (basic DFS/BFS)**: flood-fill starting from every land cell on
the four borders to eliminate all land that can escape. Whatever land remains is
trapped — count it.
