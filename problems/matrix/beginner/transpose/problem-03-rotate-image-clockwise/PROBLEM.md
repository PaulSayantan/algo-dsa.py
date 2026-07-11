# Rotate Image (90° Clockwise)

**Difficulty:** Medium

**Source:** LeetCode 48 — Rotate Image

## Description

You are given an `n x n` 2-D `matrix` representing an image. Rotate the image
by **90 degrees clockwise**.

You must rotate the image **in place**, which means you have to modify the input
2-D matrix directly. **Do not** allocate another 2-D matrix and do the rotation
(you may use `O(1)` extra scalars).

After a 90° clockwise rotation, the element originally at `(i, j)` moves to
`(j, n - 1 - i)`. Equivalently, the first column (read bottom-to-top) becomes
the first row.

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

**Explanation:** The left column `[1,4,7]` (top-to-bottom) becomes the top row
`[7,4,1]` — i.e. it is read bottom-to-top. Every element rotates a quarter turn
clockwise about the center.

### Example 2

```
Input:  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

**Explanation:** For the 4x4 image, the first column `[5,2,13,15]` read
bottom-to-top becomes the first output row `[15,13,2,5]`.

### Example 3

```
Input:  matrix = [[1]]
Output: [[1]]
```

**Explanation:** A single-element image is unchanged by rotation.

## Hint

A 90° clockwise rotation equals a **Transpose** followed by reversing each row.
Both steps can be done in place with `O(1)` extra space.
