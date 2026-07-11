# Maximal Square

**Difficulty:** Medium

**Source:** LeetCode 221 — Maximal Square

## Description

Given an `m x n` binary `matrix` filled with `0`s and `1`s, find the largest square
containing only `1`s and **return its area**.

The entries of the matrix are given as the characters `'0'` and `'1'`.

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`.

## Examples

### Example 1

```
Input: matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
Output: 4
```

**Explanation:** The largest all-ones square has side length 2 (for example the
block spanning rows 1-2 and columns 2-3), so its area is `2 * 2 = 4`.

### Example 2

```
Input: matrix = [["0","1"],
                 ["1","0"]]
Output: 1
```

**Explanation:** No 2x2 all-ones block exists, but individual `1` cells form
1x1 squares, so the maximal area is `1`.

### Example 3

```
Input: matrix = [["0"]]
Output: 0
```

**Explanation:** There are no `1`s at all, so the largest all-ones square has area
`0`.

## Hint

Use **Dynamic Programming on Grid**: let `dp[i][j]` be the side length of the
largest all-ones square whose *bottom-right corner* is `(i, j)`. A `1` cell can
extend a square only as far as the smallest square its top, left, and top-left
neighbors already support.
