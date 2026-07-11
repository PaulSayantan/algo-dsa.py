# Maximal Square

**Difficulty:** Medium

**Source:** LeetCode 221 — Maximal Square

## Description

Given an `m x n` binary matrix filled with the characters `'0'` and `'1'`, find the
largest **square** containing only `'1'`s and return its **area**.

A square submatrix is a contiguous block of cells with equal width and height, all of whose
entries are `'1'`. The answer is the area (side length squared) of the largest such square,
or `0` if the matrix contains no `'1'`.

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

**Explanation:** The largest all-`1` square has side length 2 (rows 1-2, columns 2-3), so
its area is `2 * 2 = 4`. No 3x3 all-`1` block exists.

### Example 2

```
Input: matrix = [["0","1"],
                 ["1","0"]]
Output: 1
```

**Explanation:** No 2x2 block is all `1`s, but single `1` cells exist, so the largest square
has side 1 and area `1`.

### Example 3

```
Input: matrix = [["0"]]
Output: 0
```

**Explanation:** There are no `1`s at all, so the largest square has area `0`.

## Hint

Use the **Largest Square** dynamic programming idea: let `dp[i][j]` be the side of the
largest all-`1` square whose bottom-right corner is at `(i, j)`, and combine the three
neighbors above, to the left, and diagonally up-left.
