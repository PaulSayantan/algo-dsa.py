# Sudoku Solver

**Difficulty:** Hard

**Source:** LeetCode 37 — Sudoku Solver

## Description

Write a program to solve a Sudoku puzzle by filling the empty cells.

A Sudoku solution must satisfy **all** of the following rules:

1. Each of the digits `1-9` must occur exactly once in each **row**.
2. Each of the digits `1-9` must occur exactly once in each **column**.
3. Each of the digits `1-9` must occur exactly once in each of the nine `3 x 3`
   **sub-boxes** of the grid.

The `'.'` character indicates empty cells. You must fill them **in place** so that the
completed `board` is a valid Sudoku solution. The puzzle is guaranteed to have a unique
solution.

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `'1'`-`'9'` or `'.'`.
- It is guaranteed that the input board has exactly one solution.

## Examples

### Example 1

```
Input:
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

Output:
board = [["5","3","4","6","7","8","9","1","2"],
         ["6","7","2","1","9","5","3","4","8"],
         ["1","9","8","3","4","2","5","6","7"],
         ["8","5","9","7","6","1","4","2","3"],
         ["4","2","6","8","5","3","7","9","1"],
         ["7","1","3","9","2","4","8","5","6"],
         ["9","6","1","5","3","7","2","8","4"],
         ["2","8","7","4","1","9","6","3","5"],
         ["3","4","5","2","8","6","1","7","9"]]
```

**Explanation:** Every `'.'` has been replaced by a digit so that each row, each column, and
each `3x3` box contains the digits `1-9` exactly once. For instance the top-left box reads
`5 3 4 / 6 7 2 / 1 9 8`, a permutation of `1-9`.

### Example 2

```
Input:
board = [["1","2","3","4","5","6","7","8","."],
         ["4","5","6","7","8","9","1","2","3"],
         ["7","8","9","1","2","3","4","5","6"],
         ["2","3","4","5","6","7","8","9","1"],
         ["5","6","7","8","9","1","2","3","4"],
         ["8","9","1","2","3","4","5","6","7"],
         ["3","4","5","6","7","8","9","1","2"],
         ["6","7","8","9","1","2","3","4","5"],
         ["9","1","2","3","4","5","6","7","8"]]

Output: the single empty cell at (0,8) is filled with "9".
```

**Explanation:** Only one cell is empty. Row 0 already contains `1-8`, column 8 already
contains `3,6,1,4,7,2,5,8`, and the top-right box contains `7,8,1,2,4,5`; the only digit
that fits all three constraints is `9`.

## Hint

Use **Backtracking on Grid**: find the next empty cell, try each digit `1-9` that does not
already appear in its row, column, or `3x3` box, recurse, and reset the cell to `'.'` if the
recursion fails — undo and try the next digit.
