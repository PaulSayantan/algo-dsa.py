# Rotate Image (90° Counterclockwise)

**Difficulty:** Medium

**Source:** Variant of LeetCode 48 — Rotate Image (counterclockwise direction)

## Description

You are given an `n x n` 2-D `matrix` representing an image. Rotate the image
by **90 degrees counterclockwise** (also called anticlockwise).

You must rotate the image **in place** — modify the input matrix directly using
only `O(1)` extra scalar space. Do **not** allocate a second 2-D matrix.

After a 90° counterclockwise rotation, the element originally at `(i, j)` moves
to `(n - 1 - j, i)`. Equivalently, the last column (read top-to-bottom) becomes
the first row.

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Examples

### Example 1

```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[3,6,9],[2,5,8],[1,4,7]]
```

**Explanation:** The top row `[1,2,3]` becomes the left column read
bottom-to-top: `1` moves to the bottom-left. The rightmost column `[3,6,9]`
becomes the top row.

### Example 2

```
Input:  matrix = [[1,2],[3,4]]
Output: [[2,4],[1,3]]
```

**Explanation:** For the 2x2 image, the right column `[2,4]` (top-to-bottom)
becomes the top output row `[2,4]`, and the left column `[1,3]` becomes the
bottom row `[1,3]`.

### Example 3

```
Input:  matrix = [[42]]
Output: [[42]]
```

**Explanation:** A single-element image is unchanged by rotation.

## Hint

A 90° counterclockwise rotation equals a **Transpose** followed by reversing
each column (equivalently, reversing the order of the rows). Both steps are
in place with `O(1)` extra space.
