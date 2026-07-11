# Word Search

**Difficulty:** Medium

**Source:** LeetCode 79 — "Word Search"

## Description

Given an `m x n` grid of characters `board` and a string `word`, return `true`
if `word` exists in the grid.

The word can be constructed from letters of **sequentially adjacent** cells,
where adjacent cells are **horizontally or vertically neighboring**. The **same
letter cell may not be used more than once** in a single word.

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist of only lowercase and uppercase English letters.

## Examples

### Example 1

```
Input:  board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]],
        word  = "ABCCED"
Output: true
Explanation: Start at (0,0)='A' -> (0,1)='B' -> (0,2)='C' -> (1,2)='C'
-> (2,2)='E' -> (2,1)='D'. Every step moves to an orthogonally adjacent,
previously-unused cell, spelling "ABCCED".
```

### Example 2

```
Input:  board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]],
        word  = "ABCB"
Output: false
Explanation: After A(0,0) -> B(0,1) -> C(0,2), the only remaining 'B' is the
cell we already used at (0,1); reusing a cell is forbidden, so no path spells
"ABCB".
```

## Hint

Use **Backtracking**: from each cell that matches `word[0]`, do a DFS that marks
the current cell as visited, tries the four neighbors for the next letter, and
un-marks the cell when it returns (so other search paths can still use it).
