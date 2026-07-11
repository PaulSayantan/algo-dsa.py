# Rotate Image

**Difficulty:** Medium

**Source:** LeetCode 48 — Rotate Image

## Description

You are given an `n × n` 2D `matrix` representing an image. Rotate the image by
**90 degrees clockwise**.

You have to rotate the image **in place**, which means you have to modify the
input 2D matrix directly. **Do not** allocate another 2D matrix and do the
rotation — the intended solution uses only `O(1)` extra memory.

This is the canonical use of the Rotate 90° technique: transpose the matrix
across its main diagonal, then reverse each row.

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

Explanation: Transpose gives `[[1,4,7],[2,5,8],[3,6,9]]`; reversing each row
gives `[[7,4,1],[8,5,2],[9,6,3]]`. The top-left `1` ends up in the top-right
corner, as expected for a clockwise turn.

### Example 2

```
Input:  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

Explanation: The first column `5, 2, 13, 15` (top to bottom) becomes the first
row `15, 13, 2, 5` reversed order — the bottom-left element `15` moves to the
top-left, which is what a 90° clockwise rotation does.

## Hint

Use Rotate 90° (transpose + reverse). Do the transpose in place by swapping the
upper triangle with the lower triangle, then reverse each row. No second matrix
is needed.
