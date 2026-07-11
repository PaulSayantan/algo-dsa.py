# Count Submatrices With All Ones

**Difficulty:** Hard

**Source:** LeetCode 1504 — Count Submatrices With All Ones

## Description

Given an `m x n` binary matrix `mat`, return **the number of submatrices that have all
`1`s**.

A submatrix is any contiguous, axis-aligned rectangular block of cells (of any height and
width). Rectangles of different sizes and positions are counted separately, so a large all-`1`
region contributes many rectangles.

## Constraints

- `1 <= m, n <= 150`
- `mat[i][j]` is either `0` or `1`.

## Examples

### Example 1

```
Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
```

**Explanation:** There are 8 single-cell rectangles (one per `1`), plus wider/taller all-`1`
rectangles such as the bottom-left `2 x 1`, `2 x 2`, and `3 x 1` blocks. Summed over every
size and position, the total is `13`.

### Example 2

```
Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
```

**Explanation:** Counting every all-`1` rectangle of every size and position yields `24`.

### Example 3

```
Input: mat = [[1,0,1]]
Output: 2
```

**Explanation:** The only all-`1` rectangles are the two individual `1` cells; the `0` in the
middle blocks any wider rectangle. Total = `2`.

## Hint

Build per-column **heights** of consecutive `1`s ending at each row (the Maximal Rectangle
first step). Then, for each row, count all-`1` rectangles whose bottom edge is that row using
a **monotonic stack** that accumulates, for each column, how many valid rectangles end there.
