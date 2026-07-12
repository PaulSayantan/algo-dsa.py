# Number of Islands

**Difficulty:** Medium

**Source:** LeetCode 200 — Number of Islands

## Description

Given an `m x n` grid of characters where `'1'` is land and `'0'` is water, return the number of islands. An island is a maximal group of land cells connected 4-directionally (up, down, left, right). Assume all four edges of the grid are surrounded by water.

Constraints: `1 <= m, n <= 300` (an empty grid `[]` counts as `0` islands); each cell is `'0'` or `'1'`.

## Examples

### Example 1

```
Input:  grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
Output: 1
```

**Explanation:** All the land cells are connected into a single island.

### Example 2

```
Input:  grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
Output: 3
```

**Explanation:** The top-left block, the middle cell, and the bottom-right pair form three separate islands.

## Hint

Scan for an unvisited `'1'`, then BFS from it with a FIFO queue to flood the whole connected land component before counting the next island.
