# Maximal Rectangle

**Difficulty:** Hard

**Source:** LeetCode 85 — Maximal Rectangle

## Description

Given a `rows x cols` binary matrix filled with the characters `'0'` and `'1'`, find the
largest **rectangle** containing only `'1'`s and return its **area**.

Unlike Maximal Square (Problem 1), the rectangle here need not be a square: any axis-aligned
`h x w` block of all-`1` cells qualifies, and you want the one with the biggest `h * w`.

## Constraints

- `rows == matrix.length`
- `cols == matrix[0].length`
- `1 <= rows, cols <= 200`
- `matrix[i][j]` is `'0'` or `'1'`.

## Examples

### Example 1

```
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 6
```

**Explanation:** The largest all-`1` rectangle covers rows 1-2, columns 2-4 — a `2 x 3` block
— for area `6`. (The largest *square* here is only area 4; allowing non-square rectangles
does better.)

### Example 2

```
Input: matrix = [["0"]]
Output: 0
```

**Explanation:** There are no `1`s, so the largest rectangle has area `0`.

### Example 3

```
Input: matrix = [["1","1"],
                 ["1","1"]]
Output: 4
```

**Explanation:** The whole `2 x 2` grid is all `1`s, giving area `4`.

## Hint

Apply the **Maximal Rectangle** reduction: process rows top to bottom, maintaining per-column
heights of consecutive `1`s, and solve each row as a *largest rectangle in a histogram*
(Problem 3) with a monotonic stack.
