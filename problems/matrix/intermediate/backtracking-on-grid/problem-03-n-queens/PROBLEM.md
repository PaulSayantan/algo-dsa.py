# N-Queens

**Difficulty:** Hard

**Source:** LeetCode 51 — N-Queens

## Description

The **n-queens** puzzle is the problem of placing `n` chess queens on an `n x n` chessboard
so that no two queens attack each other. Two queens attack each other if they share the same
row, the same column, or the same diagonal.

Given an integer `n`, return **all distinct solutions** to the n-queens puzzle. You may
return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where
`'Q'` and `'.'` indicate a queen and an empty space, respectively. Each returned solution is
a list of `n` strings, each of length `n`.

## Constraints

- `1 <= n <= 9`

## Examples

### Example 1

```
Input: n = 4

Output:
[[".Q..",
  "...Q",
  "Q...",
  "..Q."],
 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]]
```

**Explanation:** There are exactly two distinct ways to place 4 non-attacking queens on a
4x4 board. In the first, queens sit at (row, col) = (0,1), (1,3), (2,0), (3,2); no two share
a row, column, or diagonal. The second is the mirror image.

### Example 2

```
Input: n = 1

Output: [["Q"]]
```

**Explanation:** A single queen on a 1x1 board trivially attacks nothing.

### Example 3

```
Input: n = 3

Output: []
```

**Explanation:** It is impossible to place 3 non-attacking queens on a 3x3 board, so the
list of solutions is empty. (There are also 0 solutions for `n = 2`.)

## Hint

Use **Backtracking on Grid**: place one queen per row, and before placing in a column check
that the column and both diagonals are free. Record the placement, recurse to the next row,
then remove it (backtrack) to try the next column.
