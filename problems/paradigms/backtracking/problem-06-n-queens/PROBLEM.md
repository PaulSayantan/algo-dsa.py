# N-Queens

**Difficulty:** Hard

**Source:** LeetCode 51 — "N-Queens"

## Description

The **n-queens** puzzle is the problem of placing `n` chess queens on an
`n x n` chessboard so that **no two queens attack each other**. Two queens
attack each other if they share the same row, the same column, or the same
diagonal.

Given an integer `n`, return *all distinct solutions to the n-queens puzzle*.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens'
placement, where `'Q'` and `'.'` indicate a queen and an empty space,
respectively. Each element of the output is a list of `n` strings, each string
of length `n`, describing one valid board.

## Constraints

- `1 <= n <= 9`

## Examples

### Example 1

```
Input:  n = 4
Output: [[".Q..",
          "...Q",
          "Q...",
          "..Q."],

         ["..Q.",
          "Q...",
          "...Q",
          ".Q.."]]
Explanation: There are exactly two distinct ways to place 4 non-attacking
queens on a 4x4 board. In the first, the queens sit at columns (1,3,0,2) for
rows 0..3; in the second at columns (2,0,3,1). No two queens share a row,
column, or diagonal in either board.
```

### Example 2

```
Input:  n = 1
Output: [["Q"]]
Explanation: A single queen on a 1x1 board trivially attacks nothing, so there
is exactly one solution.
```

## Hint

Use **Backtracking**: place one queen per row. Before placing in a column,
check it is not already occupied and neither diagonal through it is threatened;
recurse to the next row, then remove the queen (undo) to try the next column.
