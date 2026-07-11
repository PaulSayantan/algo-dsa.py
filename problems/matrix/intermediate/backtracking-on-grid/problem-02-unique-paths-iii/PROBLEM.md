# Unique Paths III

**Difficulty:** Hard

**Source:** LeetCode 980 — Unique Paths III

## Description

You are given an `m x n` integer grid where each cell is one of the following values:

- `1` — the **starting** square (there is exactly one).
- `2` — the **ending** square (there is exactly one).
- `0` — an **empty** square that you can walk over.
- `-1` — an **obstacle** that you cannot walk over.

Return the number of **4-directional** walks (up, down, left, right) from the starting
square to the ending square that **walk over every non-obstacle square exactly once**.

In other words, a valid path must start at `1`, end at `2`, and cover **all** empty squares
(`0`) as well — no empty square may be skipped, and no square may be visited twice.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 20`
- `1 <= m * n <= 20`
- `-1 <= grid[i][j] <= 2`
- There is exactly one starting cell and exactly one ending cell.

## Examples

### Example 1

```
Input:
grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]

Output: 2
```

**Explanation:** There are two walks that cover every non-obstacle square exactly once:
1. `(0,0) (0,1) (0,2) (0,3) (1,3) (1,2) (1,1) (1,0) (2,0) (2,1) (2,2)`
2. `(0,0) (1,0) (2,0) (2,1) (1,1) (0,1) (0,2) (1,2) (1,3) (0,3)` ... continuing to `(2,2)`.

### Example 2

```
Input:
grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,0,2]]

Output: 4
```

**Explanation:** With no obstacle in the bottom-right, there are four distinct
"snake"-style walks that visit all 12 squares exactly once and end at `2`.

### Example 3

```
Input:
grid = [[0,1],
        [2,0]]

Output: 0
```

**Explanation:** From the start `1` at `(0,1)` the only way to reach the end `2` at `(1,0)`
would skip one of the two empty squares, so no walk covers every non-obstacle square exactly
once. The answer is `0`.

## Hint

Use **Backtracking on Grid**: DFS from the start cell, mark cells visited and track how many
non-obstacle squares remain; only count a path when you land on the end cell with **zero**
squares left, un-marking each cell as you backtrack.
