# Matrix Block Sum

**Difficulty:** Medium

**Source:** LeetCode 1314 — Matrix Block Sum

## Description

Given an `m x n` matrix `mat` and an integer `k`, return a matrix `answer` where
each `answer[i][j]` is the sum of all elements `mat[r][c]` for:

- `i - k <= r <= i + k`, and
- `j - k <= c <= j + k`, and
- `(r, c)` is a valid position in the matrix (indices are **clamped** to the
  grid; out-of-range positions contribute nothing).

In other words, `answer[i][j]` is the sum of the square block of "radius" `k`
(Chebyshev distance `k`) centered at `(i, j)`, cut off at the matrix edges.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n, k <= 100`
- `1 <= mat[i][j] <= 100`

## Examples

### Example 1

```
Input: mat = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], k = 1
Output: [[12, 21, 16],
         [27, 45, 33],
         [24, 39, 28]]
Explanation: answer[0][0] covers rows 0..1 and cols 0..1: 1+2+4+5 = 12.
answer[1][1] covers the whole matrix (rows 0..2, cols 0..2): sum = 45.
answer[2][2] covers rows 1..2 and cols 1..2: 5+6+8+9 = 28.
```

### Example 2

```
Input: mat = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], k = 2
Output: [[45, 45, 45],
         [45, 45, 45],
         [45, 45, 45]]
Explanation: With k = 2 every block reaches all four edges, so every cell's
block is the entire matrix, whose total is 45.
```

## Hint

Build a **2D Prefix Sum (Integral Image)** of `mat`, then for each output cell
clamp the block corners to the grid and answer the block sum in O(1).
