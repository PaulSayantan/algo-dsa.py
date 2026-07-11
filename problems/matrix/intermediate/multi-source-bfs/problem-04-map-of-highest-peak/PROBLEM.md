# Map of Highest Peak

**Difficulty:** Medium

**Source:** LeetCode 1765 — Map of Highest Peak

## Description

You are given an integer matrix `isWater` of size `m x n` that represents a map of land
and water cells:

- `isWater[i][j] == 0` means cell `(i, j)` is **land**.
- `isWater[i][j] == 1` means cell `(i, j)` is **water**.

You must assign each cell a **height** (a non-negative integer) subject to these rules:

1. The height of every cell must be **non-negative**.
2. Every **water** cell must have height `0`.
3. Any two **adjacent** cells (sharing a side, i.e. 4-directionally) must differ in
   height by **at most 1**.

Find an assignment of heights that **maximizes the maximum height** in the matrix, and
return an integer matrix `height` of size `m x n` giving such an assignment. If several
assignments achieve the maximum, return **any** of them.

It can be shown that the height of a cell in the optimal assignment equals its distance
(in 4-directional steps) to the nearest water cell.

## Constraints

- `m == isWater.length`
- `n == isWater[i].length`
- `1 <= m, n <= 1000`
- `isWater[i][j]` is `0` or `1`.
- There is **at least one** water cell.

## Examples

### Example 1

```
Input:  isWater = [[0, 1],
                   [0, 0]]

Output: height  = [[1, 0],
                   [2, 1]]
```

**Explanation:** The single water cell `(0,1)` has height `0`. Cell `(0,0)` and cell
`(1,1)` are each 1 step from water, so they get height `1`. Cell `(1,0)` is 2 steps
from the nearest water (via `(0,0)` or `(1,1)`), so it gets height `2`. Adjacent cells
never differ by more than 1, and the maximum height, 2, is as large as possible.

### Example 2

```
Input:  isWater = [[0, 0, 1],
                   [1, 0, 0],
                   [0, 0, 0]]

Output: height  = [[1, 1, 0],
                   [0, 1, 1],
                   [1, 2, 2]]
```

**Explanation:** The water cells at `(0,2)` and `(1,0)` get height `0`. Every other
cell is labeled with its distance to the nearest of those two water cells. For
instance `(2,1)` is 2 steps away from either water cell and gets height `2`; adjacent
differences stay within 1, and 2 is the largest achievable peak.

## Hint

The constraint "adjacent cells differ by at most 1" combined with "water is 0" means
the maximum possible height of a cell equals its distance to the nearest water. Seed a
queue with **all** water cells and run one **Multi-Source BFS** to compute those
distances.
