# Rotate Matrix Counter-Clockwise

**Difficulty:** Medium

**Source:** GeeksforGeeks — Rotate a matrix by 90 degrees (anti-clockwise);
classic interview variant of LeetCode 48.

## Description

You are given an `n × n` 2D `matrix`. Rotate the matrix by **90 degrees
counter-clockwise (anti-clockwise)** in place, modifying the input directly and
using only `O(1)` extra memory.

A counter-clockwise quarter-turn moves the top-right corner to the top-left, the
top-left corner to the bottom-left, and so on. This is the mirror image of the
clockwise rotation, and the Rotate 90° technique adapts to it by changing which
reverse you apply: transpose, then reverse the **order of the rows** (instead of
reversing each row).

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

Explanation: Transpose gives `[[1,4,7],[2,5,8],[3,6,9]]`; reversing the *order
of the rows* gives `[[3,6,9],[2,5,8],[1,4,7]]`. The top-right `3` has moved to
the top-left corner, as expected for a counter-clockwise turn.

### Example 2

```
Input:  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
Output: [[4,8,12,16],[3,7,11,15],[2,6,10,14],[1,5,9,13]]
```

Explanation: The last column `4, 8, 12, 16` (top to bottom) becomes the first
row in the same order — a 90° counter-clockwise rotation sends the rightmost
column to the top.

## Hint

Use Rotate 90° (transpose + reverse), but for the counter-clockwise direction:
transpose in place, then reverse the *order of the rows* (top row becomes bottom
row). Equivalently, reverse each row first and then transpose.
