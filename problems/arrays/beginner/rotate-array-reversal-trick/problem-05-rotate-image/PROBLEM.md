# Rotate Image

**Difficulty:** Medium

**Source:** LeetCode 48 — Rotate Image

## Description

You are given an `n x n` 2-D `matrix` representing an image. Rotate the image by
**90 degrees clockwise**.

You have to rotate the image **in place**, which means you have to modify the
input 2-D matrix directly. **Do not** allocate another 2-D matrix and do the
rotation into it.

This is the two-dimensional cousin of the reversal trick. A 90° clockwise
rotation factors into two in-place, reversal-style operations: **transpose** the
matrix (reflect across the main diagonal), then **reverse each row** (reflect
horizontally). Each row reversal is the same two-pointer reverse used to rotate
a 1-D array.

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
Output:          [[7,4,1],
                  [8,5,2],
                  [9,6,3]]
```

Explanation: The top row `[1,2,3]` becomes the right column, top-to-bottom; the
first column `[1,4,7]` becomes the top row, right-to-left. That is a 90°
clockwise turn.

### Example 2

```
Input:  matrix = [[5,1,9,11],
                  [2,4,8,10],
                  [13,3,6,7],
                  [15,14,12,16]]
Output:          [[15,13,2,5],
                  [14,3,4,1],
                  [12,6,8,9],
                  [16,7,10,11]]
```

Explanation: Rotating the 4×4 image a quarter turn clockwise moves the leftmost
column `[5,2,13,15]` to the top row (reading bottom-to-top: `15,13,2,5`).

## Hint

Use the 2-D form of the **Rotate Array (reversal trick)**: transpose the matrix
(swap `matrix[i][j]` with `matrix[j][i]`), then reverse each row using the same
two-pointer reverse that rotates a 1-D array.
