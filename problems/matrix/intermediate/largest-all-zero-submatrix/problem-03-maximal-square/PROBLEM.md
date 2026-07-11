# Maximal Square

**Difficulty:** Medium

**Source:** LeetCode 221 — Maximal Square

## Description

Given an `m x n` binary matrix filled with `'0'` and `'1'` (as characters), find
the **largest square containing only `'1'`s** and return its **area**.

A square is a rectangle whose width equals its height. This is a constrained
version of the largest all-`1` submatrix problem: instead of maximizing
`width * height` freely, each candidate rectangle is limited to a side of
`min(width, height)`.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`.

## Examples

### Example 1

```
Input:
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
Output: 4
Explanation: The 2 x 2 block at rows 1..2, columns 2..3 is all '1's, giving a
square of side 2 and area 4. No 3 x 3 all-'1' square exists.
```

### Example 2

```
Input:
matrix = [["0","1"],
          ["1","0"]]
Output: 1
Explanation: There is no 2 x 2 all-'1' block, so the biggest square is a single
'1' cell: side 1, area 1.
```

### Example 3

```
Input:
matrix = [["0"]]
Output: 0
Explanation: The only cell is '0', so no all-'1' square exists and the area is 0.
```

## Hint

Use the **Largest All-Zero Submatrix** family: build per-row heights of
consecutive `'1'`s, then in each row's histogram the biggest *square* whose
bottom sits on that row uses side `min(bar_height, width)`. A monotonic stack
gives the widths; cap each candidate to a square. (A famous O(nm) DP also
exists — compare the two.)
