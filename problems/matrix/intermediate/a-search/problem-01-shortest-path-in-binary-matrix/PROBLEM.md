# Shortest Path in Binary Matrix

**Difficulty:** Medium

**Source:** LeetCode 1091 — Shortest Path in Binary Matrix

## Description

Given an `n x n` binary matrix `grid`, return the length of the shortest **clear path**
from the top-left cell `(0, 0)` to the bottom-right cell `(n-1, n-1)`. If there is no
clear path, return `-1`.

A **clear path** is a path such that:

- Every visited cell has value `0`.
- Every pair of consecutive visited cells is **8-directionally connected** (they share
  an edge or a corner).

The **length** of a clear path is the number of visited cells along the path
(including the start and end cells).

## Constraints

- `n == grid.length == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`.

## Examples

### Example 1

```
Input: grid = [[0,1],
               [1,0]]
Output: 2
```

**Explanation:** The path `(0,0) -> (1,1)` uses a single diagonal step between two `0`
cells, visiting `2` cells total.

### Example 2

```
Input: grid = [[0,0,0],
               [1,1,0],
               [1,1,0]]
Output: 4
```

**Explanation:** One shortest clear path is `(0,0) -> (0,1) -> (1,2) -> (2,2)`, which
visits `4` cells. No 3-cell path exists because the left column is blocked by `1`s.

### Example 3

```
Input: grid = [[1,0,0],
               [1,1,0],
               [1,1,0]]
Output: -1
```

**Explanation:** The start cell `(0,0)` itself is a `1`, so no clear path can even
begin; the answer is `-1`.

## Hint

Because you only care about reaching the single corner `(n-1, n-1)`, guide the search
toward it: use **A\* Search** with a priority queue ordered by `g + h`, where `g` is the
number of cells used so far and `h` is a lower bound on the cells still needed. Since
diagonal moves are allowed, the **Chebyshev distance** `max(|dr|, |dc|)` to the goal is
an admissible, consistent heuristic.
