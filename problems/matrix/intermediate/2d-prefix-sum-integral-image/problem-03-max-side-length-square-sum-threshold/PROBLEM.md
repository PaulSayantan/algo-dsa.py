# Maximum Side Length of a Square with Sum Less Than or Equal to Threshold

**Difficulty:** Medium

**Source:** LeetCode 1292 — Maximum Side Length of a Square with Sum Less than or Equal to Threshold

## Description

Given an `m x n` matrix `mat` and an integer `threshold`, return the maximum
side length of a square whose sum is **less than or equal to** `threshold`. If
there is no such square, return `0`.

The square must be axis-aligned and lie entirely within the matrix.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 300`
- `0 <= mat[i][j] <= 10^4`
- `0 <= threshold <= 10^5`

## Examples

### Example 1

```
Input: mat = [[1, 1, 3, 2, 4, 3, 2],
              [1, 1, 3, 2, 4, 3, 2],
              [1, 1, 3, 2, 4, 3, 2]], threshold = 4
Output: 2
Explanation: The maximum side length of a square with sum <= 4 is 2, e.g. the
top-left 2x2 square [[1, 1], [1, 1]] has sum 4. No 3x3 square has sum <= 4.
```

### Example 2

```
Input: mat = [[2, 2, 2, 2],
              [2, 2, 2, 2],
              [2, 2, 2, 2],
              [2, 2, 2, 2]], threshold = 1
Output: 0
Explanation: Even a single cell has value 2 > 1, so no square (not even 1x1)
qualifies. Return 0.
```

### Example 3

```
Input: mat = [[1, 1, 1, 1],
              [1, 0, 0, 0],
              [1, 0, 0, 0]], threshold = 6
Output: 3
Explanation: The 3x3 square at the top-left has sum
(1+1+1) + (1+0+0) + (1+0+0) = 6 <= 6. No larger square fits (the matrix is only
3 rows tall).
```

## Hint

Build a **2D Prefix Sum (Integral Image)** so any square's sum is an O(1)
lookup, then find the largest workable side length (linear scan or binary search
over the side, since a valid side `L` implies every side `< L` is also valid).
