# Special Positions in a Binary Matrix

**Difficulty:** Easy/Medium

**Source:** LeetCode 1582 — Special Positions in a Binary Matrix

## Description

Given an `m x n` binary matrix `mat`, return the number of **special** positions in
`mat`.

A position `(i, j)` is called **special** if `mat[i][j] == 1` and **all** other
elements in row `i` and column `j` are `0` (rows and columns are 0-indexed). In other
words, the cell holds a 1 and it is the *only* 1 in its entire row **and** the only 1 in
its entire column.

## Constraints

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 100`
- `mat[i][j]` is either `0` or `1`.

## Examples

### Example 1

```
Input:  mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
```

**Explanation:** `(1, 2)` is a special position because `mat[1][2] == 1` and all other
elements in row 1 and column 2 are 0. The 1s at `(0,0)` and `(2,0)` share column 0, so
neither of them is special.

### Example 2

```
Input:  mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
```

**Explanation:** `(0,0)`, `(1,1)`, and `(2,2)` are all special — each is the sole 1 in
both its row and its column (an identity matrix).

### Example 3

```
Input:  mat = [[0,0,0,1],[1,0,0,0],[0,1,1,0],[0,0,0,0]]
Output: 2
```

**Explanation:** `(0,3)` is special (row 0 and column 3 each contain exactly this one
1), and `(1,0)` is special (row 1 and column 0 each contain exactly this one 1). The 1s
at `(2,1)` and `(2,2)` share row 2, so neither is special. The total is 2.

## Hint

Use **Row/Column Traversal**: first sweep the grid to compute the sum of each row and
the sum of each column. Then sweep again and count cells that hold a 1 whose row sum and
column sum are both exactly 1.
