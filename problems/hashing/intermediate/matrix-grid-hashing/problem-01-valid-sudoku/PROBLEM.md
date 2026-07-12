# Valid Sudoku

**Difficulty:** Medium

**Source:** LeetCode 36 — Valid Sudoku

## Description

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be checked: each row, each column, and each of the nine 3x3 boxes must contain the digits 1-9 without repetition. Empty cells are '.'.

## Examples

### Example 1

```
Input:  valid board
Output: true
```

## Hint

Insert (v,'row',r), (v,'col',c), (v,'box',r//3,c//3) into a set; a repeat means invalid.
