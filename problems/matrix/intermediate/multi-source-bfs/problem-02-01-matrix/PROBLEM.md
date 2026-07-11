# 01 Matrix

**Difficulty:** Medium

**Source:** LeetCode 542 — 01 Matrix

## Description

Given an `m x n` binary matrix `mat`, return a matrix of the **same size** where each
entry is the distance from that cell to the **nearest** `0`.

The distance between two adjacent cells is `1`, and moves are allowed in the four
cardinal directions (up, down, left, right).

Every cell that already contains a `0` has distance `0`. Every cell containing a `1`
should be replaced by the length of the shortest path (in cells) to any `0`.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j]` is either `0` or `1`.
- There is **at least one** `0` in `mat`.

## Examples

### Example 1

```
Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]
Output:      [[0,0,0],
              [0,1,0],
              [0,0,0]]
```

**Explanation:** The only `1` is at `(1,1)`; each of its four neighbors is a `0`, so
its nearest-zero distance is `1`. Every other cell is already `0`.

### Example 2

```
Input: mat = [[0,0,0],
              [0,1,0],
              [1,1,1]]
Output:      [[0,0,0],
              [0,1,0],
              [1,2,1]]
```

**Explanation:** Cell `(1,1)` is one step from the `0` above it. Cells `(2,0)` and
`(2,2)` are one step from a `0` in row 1. Cell `(2,1)` is two steps from the nearest
`0` (e.g. `(2,1) -> (2,0) -> (1,0)` or `(2,1) -> (1,1) -> (0,1)`), so it is `2`.

## Hint

Rather than run a search from each `1`, invert the problem: seed a queue with **every
`0`** and run a single **Multi-Source BFS** outward. The BFS distance recorded when a
`1` is first reached is its distance to the nearest `0`.
